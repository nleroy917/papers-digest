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

CLAUDE_MODEL = "claude-opus-4-6"
CLAUDE_MAX_TOKENS = 8192

DIGEST_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "week": {"type": "string", "description": "ISO week label, e.g. 2026-W10"},
        "highlights": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "reason": {"type": "string", "description": "one sentence on why this is a must-read"},
                },
                "required": ["title", "url", "reason"],
                "additionalProperties": False,
            },
        },
        "clusters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "theme": {"type": "string", "description": "short theme name"},
                    "papers": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "url": {"type": "string"},
                                "authors": {"type": "array", "items": {"type": "string"}},
                                "published": {"type": "string", "description": "YYYY-MM-DD"},
                                "source": {"type": "string"},
                                "relevance": {"type": "integer", "enum": [1, 2, 3]},
                                "summary": {"type": "string", "description": "2-3 sentence summary"},
                            },
                            "required": ["title", "url", "authors", "published", "source", "relevance", "summary"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["theme", "papers"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["week", "highlights", "clusters"],
    "additionalProperties": False,
}
