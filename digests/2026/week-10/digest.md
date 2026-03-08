# Research Digest — 2026-W10

## Highlights

- **[Scaling Laws for Reranking in Information Retrieval](http://arxiv.org/abs/2603.04816v1)** — Establishes predictable scaling laws for reranking in multi-stage retrieval pipelines, giving practitioners principled guidance on model sizing and compute allocation for production search systems.
- **[Scaling Retrieval Augmented Generation with RAG Fusion: Lessons from an Industry Deployment](http://arxiv.org/abs/2603.02153v1)** — Provides rare production-level evidence on whether retrieval fusion (multi-query + RRF) actually improves RAG answer quality under real constraints, directly actionable for anyone running RAG in production.

## RAG Systems & GraphRAG

### [Core-based Hierarchies for Efficient GraphRAG](http://arxiv.org/abs/2603.05207v1)
_Jakir Hossain, Ahmet Erdem Sarıyüce | 2026-03-05 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes replacing Leiden clustering with core-based hierarchies for community detection in GraphRAG knowledge graphs. Demonstrates improved efficiency on sparse knowledge graphs typical of document collections, directly relevant to anyone building graph-augmented RAG pipelines.

### [Scaling Retrieval Augmented Generation with RAG Fusion: Lessons from an Industry Deployment](http://arxiv.org/abs/2603.02153v1)
_Luigi Medrano, Arush Verma, Mukul Chhabra | 2026-03-02 | arXiv (cs.IR) | ⭐⭐⭐_

Evaluates multi-query retrieval and reciprocal rank fusion in a production RAG pipeline, challenging the assumption that higher recall always yields better answers. Provides practical lessons on when fusion helps and when it hurts under latency and cost constraints.

### [Detecting RAG Advertisements Across Advertising Styles](http://arxiv.org/abs/2603.04925v1)
_Sebastian Heineking, Wilhelm Pertsch, Ines Zelch et al. | 2026-03-05 | arXiv (cs.IR) | ⭐⭐_

Develops a taxonomy of advertising styles that can be injected into RAG-generated responses and evaluates automatic detection methods. Relevant to RAG system integrity and trustworthiness concerns.

### [MemSifter: Offloading LLM Memory Retrieval via Outcome-Driven Proxy Reasoning](http://arxiv.org/abs/2603.03379v1)
_Jiejun Tan, Zhicheng Dou, Liancheng Zhang et al. | 2026-03-03 | arXiv (cs.IR) | ⭐⭐_

Proposes a proxy-based memory retrieval mechanism for LLMs that balances cost and accuracy for long-term memory lookup. Relevant to the memory management layer of conversational RAG systems.

### [DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval](http://arxiv.org/abs/2603.04743v1)
_Maojun Sun, Yue Wu, Yifei Xie et al. | 2026-03-05 | arXiv (cs.IR) | ⭐⭐_

Introduces distribution-aware retrieval embeddings for matching statistical tasks to R functions, going beyond function-level semantics. Demonstrates a novel retrieval approach that incorporates data characteristics into the embedding space.

---

## Retrieval, Reranking & IR Benchmarks

### [Scaling Laws for Reranking in Information Retrieval](http://arxiv.org/abs/2603.04816v1)
_Rahul Seetharaman, Aman Bansal, Hamed Zamani et al. | 2026-03-05 | arXiv (cs.IR) | ⭐⭐⭐_

Investigates scaling laws specific to the reranking stage of multi-stage retrieval, showing how model size and compute affect reranking effectiveness. Essential reading for engineering decisions around reranker model selection.

### [Reproducing and Comparing Distillation Techniques for Cross-Encoders](http://arxiv.org/abs/2603.03010v1)
_Victor Morand, Mathias Vast, Basile Van Cooten et al. | 2026-03-03 | arXiv (cs.IR) | ⭐⭐⭐_

Systematically reproduces and compares knowledge distillation strategies for cross-encoder rerankers across multiple backbone sizes. Clarifies which distillation approaches allow smaller cross-encoders to match LLM reranker quality.

### [Still Fresh? Evaluating Temporal Drift in Retrieval Benchmarks](http://arxiv.org/abs/2603.04532v1)
_Nathan Kuissi, Suraj Subrahmanyan, Nandan Thakur et al. | 2026-03-04 | arXiv (cs.IR) | ⭐⭐⭐_

Investigates how temporal corpus drift affects retrieval benchmark validity by comparing two FreshStack snapshots a year apart. Critical for practitioners who rely on static benchmarks to evaluate retrieval systems over time.

### [Model Editing for New Document Integration in Generative Information Retrieval](http://arxiv.org/abs/2603.02773v1)
_Zhen Zhang, Zihan Wang, Xinyu Ma et al. | 2026-03-03 | arXiv (cs.IR) | ⭐⭐_

Addresses the challenge of integrating new documents into generative retrieval models without full retraining, using model editing techniques. Tackles the catastrophic forgetting problem in generative IR.

### [Behind the Prompt: The Agent-User Problem in Information Retrieval](http://arxiv.org/abs/2603.03630v1)
_Saber Zerhoudi, Michael Granitzer, Dang Hai Dang et al. | 2026-03-04 | arXiv (cs.IR) | ⭐⭐_

Formalizes the structural challenge of AI agents as IR users whose hidden instructions make intent non-identifiable. Important conceptual work for anyone building search APIs consumed by AI agents.

### [τ-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge](http://arxiv.org/abs/2603.04370v1)
_Quan Shi, Alexandra Zytek, Pedram Razavi et al. | 2026-03-04 | arXiv (cs.IR) | ⭐⭐_

Introduces a benchmark for evaluating conversational agents that must retrieve and apply knowledge from unstructured corpora during live interactions. Fills a gap in end-to-end agentic RAG evaluation.

---

## Embeddings & Multimodal Retrieval

### [OmniRet: Efficient and High-Fidelity Omni Modality Retrieval](http://arxiv.org/abs/2603.02098v1)
_Chuong Huynh, Manh Luong, Abhinav Shrivastava | 2026-03-02 | arXiv (cs.IR) | ⭐⭐⭐_

Presents the first retrieval model handling queries across more than two modalities, advancing toward truly universal multimodal vector search. Directly relevant to practitioners building multimodal embedding pipelines.

### [CONE: Embeddings for Complex Numerical Data Preserving Unit and Variable Semantics](http://arxiv.org/abs/2603.04741v1)
_Gyanendra Shrestha, Anna Pyayt, Michael Gubanov | 2026-03-05 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a hybrid transformer encoder that properly encodes numerical data with unit and variable semantics into embeddings. Addresses a key weakness of standard text embeddings for structured/numerical data in vector search.

### [The Science Data Lake: A Unified Open Infrastructure Integrating 293 Million Papers](http://arxiv.org/abs/2603.03126v1)
_Jonas Wilinski | 2026-03-03 | arXiv (cs.IR) | ⭐⭐_

Unifies eight scholarly data sources with embedding-based ontology alignment across 293M papers. Demonstrates practical embedding-based entity alignment at scale, relevant to large-scale knowledge base construction.

---

## Ranking & Recommendation Systems

### [Constraint-Aware Generative Re-ranking for Multi-Objective Optimization in Advertising Feeds](http://arxiv.org/abs/2603.04227v1)
_Chenfei Li, Hantao Zhao, Weixi Yao et al. | 2026-03-04 | arXiv (cs.IR) | ⭐⭐_

Proposes a constraint-aware generative reranking framework for ad feeds that transforms constrained optimization into bounded neural decoding. Relevant to anyone building production ranking pipelines with business constraints.

### [OneRanker: Unified Generation and Ranking with One Model](http://arxiv.org/abs/2603.02999v2)
_Dekai Sun, Yiming Liu, Jiafan Zhou et al. | 2026-03-03 | arXiv (cs.IR) | ⭐⭐_

Unifies generative retrieval and ranking into a single model for advertising recommendation, addressing the disconnect between generation and ranking stages in cascaded systems.

### [Relevance Matters: Multi-Task and Multi-Stage LLM Approach for E-commerce Query Rewriting](http://arxiv.org/abs/2603.02555v1)
_Aijun Dai, Jixiang Zhang, Haiqing Hu et al. | 2026-03-03 | arXiv (cs.IR) | ⭐⭐_

Proposes an LLM-based multi-task framework for e-commerce query rewriting that jointly optimizes relevance and user conversion. Practical for search engineers working on query understanding pipelines.

### [Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking](http://arxiv.org/abs/2603.03770v1)
_Pengfei Tong, Siyuan Chen, Chenwei Zhang et al. | 2026-03-04 | arXiv (cs.IR) | ⭐_

Addresses gradient conflicts in pre-ranking caused by mixing heterogeneous training samples from different retrieval stages. Proposes heterogeneity-aware training for large-scale cascade recommendation systems.

### [SOLAR: SVD-Optimized Lifelong Attention for Recommendation](http://arxiv.org/abs/2603.02561v1)
_Chenghao Zhang, Chao Feng, Yuanhao Pu et al. | 2026-03-03 | arXiv (cs.IR) | ⭐_

Uses SVD-based linear attention to handle long user interaction sequences efficiently in recommendation. Relevant to efficient attention mechanisms applicable to long-context retrieval scenarios.

---
