# Research Digest — 2026-W16

## Highlights

- **[vstash: Local-First Hybrid Retrieval with Adaptive Fusion for LLM Agents](http://arxiv.org/abs/2604.15484v1)** — Directly demonstrates a practical hybrid vector + keyword retrieval system in SQLite with RRF fusion, self-supervised embedding refinement, and BEIR benchmarks — immediately actionable for anyone building local RAG pipelines.
- **[Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](http://arxiv.org/abs/2604.14572v1)** — Proposes a compelling alternative to standard retrieve-then-read RAG by compiling a corpus into a hierarchical skill directory that an LLM agent navigates, addressing key limitations like scattered evidence and backtracking.

## Hybrid & Dense Retrieval Systems

### [vstash: Local-First Hybrid Retrieval with Adaptive Fusion for LLM Agents](http://arxiv.org/abs/2604.15484v1)
_Jayson Steffens | 2026-04-16 | arXiv (cs.IR) | ⭐⭐⭐_

Presents a local-first document memory combining sqlite-vec ANN search with FTS5 keyword matching via RRF and adaptive IDF weighting. Introduces self-supervised embedding refinement through hybrid retrieval disagreement. Evaluated on BEIR datasets (SciFact, NFCorpus, FiQA).

### [Hybrid Retrieval for COVID-19 Literature: Comparing Rank Fusion and Projection Fusion with Diversity Reranking](http://arxiv.org/abs/2604.13728v1)
_Harishkumar Kishorkumar Prajapati | 2026-04-15 | arXiv (cs.IR) | ⭐⭐⭐_

Benchmarks six retrieval configurations (SPLADE, BGE, RRF, projection-based vector fusion) on TREC-COVID with 171K papers. RRF fusion achieves nDCG@10=0.828, outperforming single-signal baselines substantially. Provides practical guidance on when rank fusion vs. projection fusion is preferable.

### [FRAGATA: Semantic Retrieval of HPC Support Tickets via Hybrid RAG over 20 Years of Request Tracker History](http://arxiv.org/abs/2604.13721v1)
_Santiago Paramés-Estévez, Nicolás Filloy-Montesino, Jorge Fernández-Fabeiro et al. | 2026-04-15 | arXiv (cs.IR) | ⭐⭐⭐_

Real-world deployment of hybrid semantic search over 20 years of HPC support tickets, combining modern embedding-based retrieval with RAG. A practical case study demonstrating vector search value in enterprise knowledge reuse scenarios.

### [BioHiCL: Hierarchical Multi-Label Contrastive Learning for Biomedical Retrieval with MeSH Labels](http://arxiv.org/abs/2604.15591v1)
_Mengfei Lan, Lecheng Zheng, Halil Kilicoglu | 2026-04-17 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces hierarchical multi-label contrastive learning using MeSH annotations for biomedical retrieval, going beyond binary relevance. Demonstrates that structured label hierarchies can improve embedding quality for domain-specific retrieval tasks.

---

## RAG Architectures & Adaptive Retrieval

### [Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](http://arxiv.org/abs/2604.14572v1)
_Yiqun Sun, Pengfei Wei, Lawrence B. Hsieh | 2026-04-16 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes Corpus2Skill, which compiles document corpora into hierarchical skill directories offline and lets an LLM agent navigate them at inference time. Addresses RAG limitations around scattered evidence and backtracking with a structured navigation paradigm.

### [Rethinking the Necessity of Adaptive Retrieval-Augmented Generation through the Lens of Adaptive Listwise Ranking](http://arxiv.org/abs/2604.15621v1)
_Jun Feng, Jiahui Tang, Zhicheng He et al. | 2026-04-17 | arXiv (cs.IR) | ⭐⭐⭐_

Re-evaluates whether adaptive retrieval is still needed as LLMs become more noise-robust, proposing AdaRankLLM which shifts the adaptive decision to listwise reranking. Highly relevant to RAG pipeline design choices around when and whether to retrieve.

### [A Unified Model and Document Representation for On-Device Retrieval-Augmented Generation](http://arxiv.org/abs/2604.14403v1)
_Julian Killingback, Ofer Meshi, Henry Li et al. | 2026-04-15 | arXiv (cs.IR) | ⭐⭐⭐_

Addresses on-device RAG by unifying retrieval and generation into a single model with shared document representations, reducing latency, storage, and privacy concerns. Directly relevant for edge-deployed vector search and RAG systems.

### [APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI](http://arxiv.org/abs/2604.14362v1)
_Pratyay Banerjee, Masud Moshtaghi, Shivashankar Subramanian et al. | 2026-04-15 | arXiv (cs.IR) | ⭐⭐_

Proposes a property-graph-based conversational memory system with temporal grounding and append-only storage, offering an alternative to naive vector retrieval for long-term memory. Relevant to practitioners building memory layers for conversational agents.

### [IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning](http://arxiv.org/abs/2604.15148v1)
_Zihan Liang, Yufei Ma, Ben Chen et al. | 2026-04-16 | arXiv (cs.IR) | ⭐⭐_

Introduces step-level information gain rewards for RL-trained search-augmented reasoning, helping LLMs issue more precise queries. Relevant to agentic RAG systems where query quality directly impacts retrieval effectiveness.

---

## Embedding Benchmarks & Retrieval Evaluation

### [JFinTEB: Japanese Financial Text Embedding Benchmark](http://arxiv.org/abs/2604.15882v1)
_Masahiro Suzuki, Hiroki Sakaji | 2026-04-17 | arXiv (cs.IR) | ⭐⭐⭐_

First comprehensive benchmark for Japanese financial text embeddings, covering retrieval and classification tasks. Valuable for practitioners building domain-specific embedding models for non-English financial corpora.

### [UsefulBench: Towards Decision-Useful Information as a Target for Information Retrieval](http://arxiv.org/abs/2604.15827v1)
_Tobias Schimanski, Stefanie Lewandowski, Christian Woerle et al. | 2026-04-17 | arXiv (cs.IR) | ⭐⭐_

Distinguishes between relevance (semantic similarity) and usefulness (decision utility) in IR, proposing a benchmark that targets truly useful retrieval. Challenges the implicit similarity-equals-relevance assumption in vector search systems.

### [Controlling Authority Retrieval: A Missing Retrieval Objective for Authority-Governed Knowledge](http://arxiv.org/abs/2604.14488v1)
_Andre Bacellar | 2026-04-15 | arXiv (cs.IR) | ⭐⭐_

Formalizes retrieval in authority-governed domains (law, regulation) where later documents can void earlier ones despite semantic distance. Highlights a fundamental limitation of similarity-based retrieval for compliance and legal use cases.

---

## Learning to Rank & Reranking

### [Metric-agnostic Learning-to-Rank via Boosting and Rank Approximation](http://arxiv.org/abs/2604.15101v1)
_Camilo Gomez, Pengyang Wang, Yanjie Fu | 2026-04-16 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a metric-agnostic LTR framework that avoids commitment to a single ranking metric (NDCG, MAP) during optimization. Addresses a practical pain point for search engineers who need to optimize across multiple metrics simultaneously.

---

## Cross-Modal Retrieval & Embeddings

### [SIMMER: Cross-Modal Food Image--Recipe Retrieval via MLLM-Based Embedding](http://arxiv.org/abs/2604.15628v1)
_Keisuke Gomi, Keiji Yanai | 2026-04-17 | arXiv (cs.IR) | ⭐⭐_

Uses a single multimodal LLM to generate embeddings for both food images and recipe texts, replacing complex dual-encoder alignment strategies. Demonstrates that unified MLLM embeddings can simplify cross-modal retrieval architectures.

### [DUET: Joint Exploration of User Item Profiles in Recommendation System](http://arxiv.org/abs/2604.13801v1)
_Yue Chen, Yifei Sun, Lu Wang et al. | 2026-04-15 | arXiv (cs.IR) | ⭐_

Studies how to construct effective textual profiles for users and items and align them for LLM-based recommendation. Explores the intersection of natural language representations and embedding alignment for relevance estimation.

---
