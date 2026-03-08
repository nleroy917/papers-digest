# paper-digest — Claude Code Plan

A GitHub Actions project that generates a weekly research digest of arXiv and HuggingFace papers, summarized by Claude, committed as markdown files.

---

## Project Structure

```
paper-digest/
├── .github/
│   └── workflows/
│       └── weekly-digest.yml   # cron job, runs every Monday 07:00 UTC
├── scripts/
│   └── digest.py               # main script
├── digests/
│   └── README.md               # placeholder so folder is tracked by git
└── README.md
```

---

## Files to Create

### `scripts/digest.py`

Main script. Does the following in order:

1. **Fetch arXiv papers** — queries `cs.IR`, `cs.LG`, `cs.CL` via the arXiv Atom API, pulls last 8 days, deduplicates by title
2. **Keyword filter** — keeps only papers whose title/abstract contain relevant terms (vector search, ANN, hybrid search, SPLADE, ColBERT, RAG, embeddings, reranking, etc.)
3. **Fetch HuggingFace Papers** — hits `https://huggingface.co/api/daily_papers?date=YYYY-MM-DD` for each of the last 8 days, same keyword filter applied
4. **Deduplicate** across both sources, cap at 30 papers before sending to Claude (filter by citation or your own heuristic if needed to get under the cap)
5. **Summarize with Claude** (`claude-opus-4-5`, max_tokens=4096) — prompt asks Claude to:
   - Filter to most relevant papers for vector search / IR practitioners
   - Group into 3–5 thematic clusters (e.g. Sparse & Hybrid Retrieval, ANN & Indexing, Embeddings, RAG, Evals)
   - Write 2–3 sentence summaries per paper
   - Score relevance 1–3 (3 = directly relevant to Qdrant's space)
   - Pick 1–2 "highlights" worth a deep read
   - Return **only valid JSON** (no markdown fences)
6. **Render markdown** — highlights section first, then clusters with relevance stars, authors, date, source
7. **Write to** `digests/YYYY/week-WW/digest.md` relative to repo root

Key config constants at top of file:
```python
ARXIV_CATEGORIES = ["cs.IR", "cs.LG", "cs.CL"]
KEYWORDS = [...]          # filter terms
MAX_ARXIV_RESULTS = 60    # per category, before filter
MAX_PAPERS_TO_SUMMARIZE = 30  # cap sent to Claude
```

Claude JSON output schema:
```json
{
  "week": "2026-W10",
  "highlights": [{ "title": "...", "url": "...", "reason": "..." }],
  "clusters": [{
    "theme": "...",
    "papers": [{
      "title": "...", "url": "...", "authors": [],
      "published": "YYYY-MM-DD", "source": "...",
      "relevance": 3, "summary": "..."
    }]
  }]
}
```

---

### `.github/workflows/weekly-digest.yml`

- Trigger: `schedule` cron `0 7 * * 1` (Monday 07:00 UTC) + `workflow_dispatch` for manual runs
- Permissions: `contents: write`
- Steps:
  1. `actions/checkout@v4`
  2. `actions/setup-python@v5` with Python 3.12
  3. `pip install anthropic`
  4. `python scripts/digest.py` with `ANTHROPIC_API_KEY` from secrets
  5. `git add digests/` → commit `"digest: YYYY-WWW"` if diff exists → `git push`

---

### `README.md`

Document:
- What the project does
- Setup steps: fork repo → add `ANTHROPIC_API_KEY` secret → trigger manual run
- Where digests are written (`digests/YYYY/week-WW/digest.md`)
- How to run locally: `pip install anthropic && python scripts/digest.py`
- Config table for the key constants in `digest.py`

---

### `digests/README.md`

One-liner placeholder so the `digests/` folder is committed to git before the first run.

---

## Setup Instructions (after creating files)

```bash
# 1. Init repo
git init paper-digest
cd paper-digest

# 2. Create the files above

# 3. Test locally
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python scripts/digest.py
# → digests/YYYY/week-WW/digest.md should appear

# 4. Commit and push
git add .
git commit -m "init: paper-digest"
git remote add origin https://github.com/YOUR_USERNAME/paper-digest.git
git push -u origin main

# 5. Add secret in GitHub
# Settings → Secrets and variables → Actions → New repository secret
# Name: ANTHROPIC_API_KEY
# Value: sk-ant-...

# 6. Trigger first run
# Actions tab → Weekly Research Digest → Run workflow
```

---

## Notes

- Only dependency is `anthropic` — stdlib only otherwise (urllib, xml.etree, json, datetime)
- arXiv rate limits are generous; no auth needed
- HuggingFace Papers API is public; no auth needed
- The GitHub Action commits back to the repo using the default `GITHUB_TOKEN` — no extra tokens needed beyond the Anthropic key
- If Claude returns malformed JSON, the script will raise — worth adding a try/except around the parse in `summarize_with_claude` if you want it to be fault-tolerant
- Adjust `KEYWORDS` over time as you discover what's worth tracking
- Make comments in the code all lowercase, sensible and concise and refrain from `--- Here is a comment ---` style comments. Use inline comments where appropriate.