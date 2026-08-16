# paper-digest

Automated weekly research digest of arXiv and HuggingFace papers on vector search, information retrieval, and RAG — summarized and clustered by Claude.

A GitHub Actions workflow runs every Monday, fetches recent papers, filters by relevance, sends them to Claude for summarization, and commits the resulting digest as a markdown file.

## Setup

1. Fork this repo
2. Add your `ANTHROPIC_API_KEY` as a repository secret (Settings → Secrets and variables → Actions)
3. Trigger a manual run from the Actions tab → **Weekly Research Digest** → Run workflow

Digests are written to `digests/YYYY/week-WW/digest.md`.

## Discord notifications

To post each newly published digest to a Discord channel, create a channel webhook and add its URL as the `DISCORD_WEBHOOK_URL` repository secret. The weekly workflow then posts every paper title, links to the committed Markdown file on GitHub, and attaches `digest.md` for reading directly in Discord. If the secret is absent, digest generation and publishing continue without a notification.

## Run locally

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python scripts/digest.py
```

## Configuration

Constants at the top of `scripts/digest.py`:

| Constant | Default | Description |
|---|---|---|
| `ARXIV_CATEGORIES` | `cs.IR`, `cs.LG`, `cs.CL` | arXiv categories to query |
| `KEYWORDS` | see source | Terms used to filter papers by title/abstract |
| `MAX_ARXIV_RESULTS` | 60 | Max results fetched per category |
| `MAX_PAPERS_TO_SUMMARIZE` | 30 | Cap on papers sent to Claude |
| `LOOKBACK_DAYS` | 8 | Number of days to look back |
