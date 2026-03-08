"""Weekly research digest: fetches papers from arXiv + HuggingFace, summarizes with Claude."""

import json
import os
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

import anthropic

ARXIV_CATEGORIES = ["cs.IR", "cs.LG", "cs.CL"]
KEYWORDS = [
    "vector search", "vector database", "approximate nearest neighbor", "ANN",
    "hybrid search", "SPLADE", "ColBERT", "dense retrieval", "sparse retrieval",
    "RAG", "retrieval-augmented", "retrieval augmented",
    "embedding", "embeddings", "sentence embedding",
    "reranking", "re-ranking", "cross-encoder",
    "information retrieval", "neural search", "semantic search",
    "HNSW", "IVF", "quantization", "product quantization",
    "knowledge graph", "entity linking",
    "BM25", "learned sparse", "late interaction",
    "multi-vector", "matryoshka", "binary embedding",
]
MAX_ARXIV_RESULTS = 60  # per category, before filter
MAX_PAPERS_TO_SUMMARIZE = 30  # cap sent to claude
LOOKBACK_DAYS = 8

ARXIV_API = "http://export.arxiv.org/api/query"
HF_PAPERS_API = "https://huggingface.co/api/daily_papers"
ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}


def fetch_arxiv_papers(category: str, start_date: str, end_date: str) -> list[dict]:
    """fetch papers from a single arxiv category within date range."""
    query = (
        f"cat:{category} AND submittedDate:[{start_date} TO {end_date}]"
    )
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": 0,
        "max_results": MAX_ARXIV_RESULTS,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"{ARXIV_API}?{params}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        xml_data = resp.read()

    root = ET.fromstring(xml_data)
    papers = []
    for entry in root.findall("atom:entry", ARXIV_NS):
        title = entry.findtext("atom:title", "", ARXIV_NS).strip()
        title = re.sub(r"\s+", " ", title)
        abstract = entry.findtext("atom:summary", "", ARXIV_NS).strip()
        authors = [a.findtext("atom:name", "", ARXIV_NS) for a in entry.findall("atom:author", ARXIV_NS)]
        link = entry.findtext("atom:id", "", ARXIV_NS).strip()
        published = entry.findtext("atom:published", "", ARXIV_NS)[:10]
        papers.append({
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "url": link,
            "published": published,
            "source": f"arXiv ({category})",
        })
    return papers


def fetch_hf_papers(date_str: str) -> list[dict]:
    """fetch papers from huggingface daily papers for a given date."""
    url = f"{HF_PAPERS_API}?date={date_str}"
    req = urllib.request.Request(url, headers={"User-Agent": "paper-digest/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except Exception:
        return []

    papers = []
    for item in data:
        paper = item.get("paper", {})
        title = paper.get("title", "").strip()
        abstract = paper.get("summary", "").strip()
        authors = [a.get("name", "") for a in paper.get("authors", [])]
        arxiv_id = paper.get("id", "")
        url = f"https://huggingface.co/papers/{arxiv_id}" if arxiv_id else ""
        published = paper.get("publishedAt", "")[:10]
        papers.append({
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "url": url,
            "published": published,
            "source": "HuggingFace",
        })
    return papers


def matches_keywords(paper: dict) -> bool:
    """check if title or abstract contains any relevant keyword."""
    text = (paper["title"] + " " + paper["abstract"]).lower()
    return any(kw.lower() in text for kw in KEYWORDS)


def deduplicate(papers: list[dict]) -> list[dict]:
    """deduplicate papers by normalized title."""
    seen = set()
    unique = []
    for p in papers:
        key = re.sub(r"\W+", "", p["title"].lower())
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


def collect_papers() -> list[dict]:
    """gather papers from all sources, filter, deduplicate, and cap."""
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=LOOKBACK_DAYS)
    # arxiv date format for query: YYYYMMDDHHNN
    start_str = start.strftime("%Y%m%d0000")
    end_str = now.strftime("%Y%m%d2359")

    all_papers = []

    # arxiv
    for cat in ARXIV_CATEGORIES:
        print(f"fetching arXiv {cat}...")
        all_papers.extend(fetch_arxiv_papers(cat, start_str, end_str))

    # huggingface
    for day_offset in range(LOOKBACK_DAYS):
        date = (now - timedelta(days=day_offset)).strftime("%Y-%m-%d")
        print(f"fetching HuggingFace papers for {date}...")
        all_papers.extend(fetch_hf_papers(date))

    print(f"total fetched: {len(all_papers)}")

    filtered = [p for p in all_papers if matches_keywords(p)]
    print(f"after keyword filter: {len(filtered)}")

    unique = deduplicate(filtered)
    print(f"after dedup: {len(unique)}")

    # cap
    if len(unique) > MAX_PAPERS_TO_SUMMARIZE:
        unique = unique[:MAX_PAPERS_TO_SUMMARIZE]
        print(f"capped at {MAX_PAPERS_TO_SUMMARIZE}")

    return unique


def summarize_with_claude(papers: list[dict]) -> dict:
    """send papers to claude for clustering and summarization."""
    now = datetime.now(timezone.utc)
    week_label = now.strftime("%G-W%V")

    papers_for_prompt = [
        {"title": p["title"], "url": p["url"], "authors": p["authors"][:5],
         "published": p["published"], "source": p["source"], "abstract": p["abstract"][:500]}
        for p in papers
    ]

    prompt = f"""You are a research digest curator for engineers working on vector search, information retrieval, and RAG systems (think Qdrant, Pinecone, Weaviate users).

Here are {len(papers_for_prompt)} recent papers. Analyze them and return a JSON object with this exact structure:

{{
  "week": "{week_label}",
  "highlights": [
    {{"title": "...", "url": "...", "reason": "one sentence on why this is a must-read"}}
  ],
  "clusters": [
    {{
      "theme": "short theme name (e.g. Sparse & Hybrid Retrieval)",
      "papers": [
        {{
          "title": "...",
          "url": "...",
          "authors": ["first author", "..."],
          "published": "YYYY-MM-DD",
          "source": "arXiv (cs.IR) or HuggingFace",
          "relevance": 3,
          "summary": "2-3 sentence summary focusing on what's new and why it matters"
        }}
      ]
    }}
  ]
}}

Guidelines:
- Pick 1-2 highlights worth a deep read
- Group into 3-5 thematic clusters
- Score relevance 1-3 (3 = directly relevant to vector search / IR practitioners)
- Drop papers that are not relevant at all
- Return ONLY valid JSON, no markdown fences, no commentary

Papers:
{json.dumps(papers_for_prompt, indent=2)}"""

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-opus-4-5-20250514",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    return json.loads(raw)


def render_markdown(digest: dict) -> str:
    """render the claude digest json into a readable markdown file."""
    lines = [f"# Research Digest — {digest['week']}", ""]

    # highlights
    if digest.get("highlights"):
        lines.append("## Highlights")
        lines.append("")
        for h in digest["highlights"]:
            lines.append(f"- **[{h['title']}]({h['url']})** — {h['reason']}")
        lines.append("")

    # clusters
    for cluster in digest.get("clusters", []):
        lines.append(f"## {cluster['theme']}")
        lines.append("")
        for p in cluster.get("papers", []):
            stars = p.get("relevance", 1) * "\u2b50"
            author_str = ", ".join(p.get("authors", [])[:3])
            if len(p.get("authors", [])) > 3:
                author_str += " et al."
            lines.append(f"### [{p['title']}]({p['url']})")
            lines.append(f"_{author_str} | {p.get('published', '')} | {p.get('source', '')} | {stars}_")
            lines.append("")
            lines.append(p.get("summary", ""))
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def write_digest(markdown: str) -> Path:
    """write digest to digests/YYYY/week-WW/digest.md."""
    now = datetime.now(timezone.utc)
    year = now.strftime("%G")
    week = now.strftime("%V")

    repo_root = Path(__file__).resolve().parent.parent
    digest_dir = repo_root / "digests" / year / f"week-{week}"
    digest_dir.mkdir(parents=True, exist_ok=True)
    path = digest_dir / "digest.md"
    path.write_text(markdown, encoding="utf-8")
    return path


def main():
    papers = collect_papers()
    if not papers:
        print("no relevant papers found this week, skipping digest.")
        return

    print(f"\nsummarizing {len(papers)} papers with claude...")
    digest = summarize_with_claude(papers)

    markdown = render_markdown(digest)
    path = write_digest(markdown)
    print(f"\ndigest written to {path}")


if __name__ == "__main__":
    main()
