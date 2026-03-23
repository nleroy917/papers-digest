# Research Digest — 2026-W12

## Highlights

- **[A Super Fast K-means for Indexing Vector Embeddings](http://arxiv.org/abs/2603.20009v1)** — Directly addresses a core bottleneck in vector search indexing—presents SuperKMeans achieving up to 7x speedup over FAISS k-means on CPUs and 4x over cuVS on GPUs while maintaining centroid quality, immediately applicable to IVF-style index building.
- **[CRE-T1 Preview Technical Report: Beyond Contrastive Learning for Reasoning-Intensive Retrieval](http://arxiv.org/abs/2603.17387v1)** — Challenges the dominant contrastive-learning paradigm for embedding models by showing its limitations on reasoning-intensive queries, proposing dynamic relevance judgments—critical reading for anyone building RAG pipelines over complex knowledge.

## Vector Index & Embedding Efficiency

### [A Super Fast K-means for Indexing Vector Embeddings](http://arxiv.org/abs/2603.20009v1)
_Leonardo Kuffo, Sven Hepkema, Peter Boncz | 2026-03-20 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces SuperKMeans, a k-means variant that prunes unneeded dimensions to dramatically accelerate clustering of high-dimensional embeddings. Achieves up to 7x speedup over FAISS/Scikit-Learn on CPUs and 4x over cuVS on GPUs without sacrificing centroid quality for vector search.

### [Spectral Tempering for Embedding Compression in Dense Passage Retrieval](http://arxiv.org/abs/2603.19339v1)
_Yongkang Li, Panagiotis Eustratiadis, Evangelos Kanoulas | 2026-03-19 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a spectral tempering method that navigates the PCA-whitening tradeoff for post-hoc dimensionality reduction of dense retrieval embeddings. Offers a principled way to compress embeddings while preserving retrieval effectiveness, directly useful for reducing memory/storage in vector databases.

---

## Dense Retrieval & RAG Quality

### [CRE-T1 Preview Technical Report: Beyond Contrastive Learning for Reasoning-Intensive Retrieval](http://arxiv.org/abs/2603.17387v1)
_Guangzhi Wang, Yinghao Jiao, Zhi Liu | 2026-03-18 | arXiv (cs.IR) | ⭐⭐⭐_

Argues that contrastive learning produces static representations inadequate for reasoning-intensive retrieval where implicit query-document relationships matter. Proposes methods to move beyond fixed geometric embeddings, highly relevant for RAG over complex documents.

### [Negation is Not Semantic: Diagnosing Dense Retrieval Failure Modes for Trade-offs in Contradiction-Aware Biomedical QA](http://arxiv.org/abs/2603.17580v1)
_Soumya Ranjan Sahoo, Gagan N., Sanand Sasidharan et al. | 2026-03-18 | arXiv (cs.IR) | ⭐⭐⭐_

Diagnoses how dense retrieval models fail on negation and contradiction in biomedical QA, a critical issue for RAG pipelines in high-stakes domains. Provides proxy-based evaluation strategies for contradiction-aware retrieval.

### [CoverageBench: Evaluating Information Coverage across Tasks and Domains](http://arxiv.org/abs/2603.20034v1)
_Saron Samuel, Andrew Yates, Dawn Lawrie et al. | 2026-03-20 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces a benchmark measuring information coverage in retrieval results—how much of the range of relevant information is surfaced. Directly relevant to RAG systems where diversity of retrieved evidence matters beyond simple precision/recall.

### [OPERA: Online Data Pruning for Efficient Retrieval Model Adaptation](http://arxiv.org/abs/2603.17205v1)
_Haoyang Fang, Shuai Zhang, Yifei Ma et al. | 2026-03-17 | arXiv (cs.IR) | ⭐⭐⭐_

Presents a data pruning framework for domain-specific fine-tuning of dense retrievers, revealing a quality-coverage tradeoff where static pruning improves NDCG but can hurt recall. Introduces online pruning to balance both, directly useful for teams fine-tuning retrieval models.

### [PJB: A Reasoning-Aware Benchmark for Person-Job Retrieval](http://arxiv.org/abs/2603.17386v1)
_Guangzhi Wang, Xiaohui Yang, Kai Li et al. | 2026-03-18 | arXiv (cs.IR) | ⭐⭐_

Introduces a diagnostic benchmark for person-job matching that requires skill-transfer inference and competency reasoning, going beyond lexical overlap. Useful for understanding where embedding-based retrieval models fail on complex domain tasks.

---

## Generative Retrieval & Semantic IDs

### [Deploying Semantic ID-based Generative Retrieval for Large-Scale Podcast Discovery at Spotify](http://arxiv.org/abs/2603.17540v1)
_Edoardo D'Amico, Marco De Nadai, Praveen Chandar et al. | 2026-03-18 | arXiv (cs.IR) | ⭐⭐⭐_

Describes Spotify's production deployment of generative retrieval using semantic IDs for podcast recommendation, demonstrating how generative models can replace or augment traditional ANN search for intent-aware discovery at scale.

### [A Unified Language Model for Large Scale Search, Recommendation, and Reasoning](http://arxiv.org/abs/2603.17533v1)
_Marco De Nadai, Edoardo D'Amico, Max Lefarov et al. | 2026-03-18 | arXiv (cs.IR) | ⭐⭐_

Proposes a single LLM that jointly handles search, recommendation, and reasoning over large heterogeneous catalogs using semantic IDs. Demonstrates an alternative to traditional retrieval pipelines combining embedding search with LLM reasoning.

### [RouterKGQA: Specialized--General Model Routing for Constraint-Aware Knowledge Graph Question Answering](http://arxiv.org/abs/2603.20017v1)
_Bo Yuan, Hexuan Deng, Xuebo Liu et al. | 2026-03-20 | arXiv (cs.IR) | ⭐⭐_

Proposes routing between lightweight retrieval-based KGQA and expensive agent-based models for knowledge graph QA. Relevant to practitioners building RAG over structured knowledge where cost-quality tradeoffs matter.

---

## E-Commerce Search & Recommendation

### [GenFacet: End-to-End Generative Faceted Search via Multi-Task Preference Alignment in E-Commerce](http://arxiv.org/abs/2603.19665v1)
_Zhouwei Zhai, Min Yang, Jin Li | 2026-03-20 | arXiv (cs.IR) | ⭐⭐_

Reframes faceted search as a generative task using LLMs deployed at JD.com, coupling facet generation with retrieval. Demonstrates how generative approaches can replace static rule-based faceting in production search systems.

### [AIGQ: An End-to-End Hybrid Generative Architecture for E-commerce Query Recommendation](http://arxiv.org/abs/2603.19710v1)
_Jingcao Xu, Jianyun Zou, Renkai Yang et al. | 2026-03-20 | arXiv (cs.IR) | ⭐⭐_

Proposes a generative framework for pre-search query recommendation on Taobao, replacing ID-based matching with semantic generation. Addresses cold-start and serendipity challenges in large-scale e-commerce search.

### [VLM2Rec: Resolving Modality Collapse in Vision-Language Model Embedders for Multimodal Sequential Recommendation](http://arxiv.org/abs/2603.17450v1)
_Junyoung Kim, Woojoo Kim, Jaehyung Lim et al. | 2026-03-18 | arXiv (cs.IR) | ⭐⭐_

Investigates using VLMs as high-capacity multimodal embedders for sequential recommendation, identifying and solving modality collapse during contrastive fine-tuning. Relevant to multimodal embedding and retrieval practitioners.

---

## Knowledge & Semantic Integration for IR

### [LLM-Enhanced Semantic Data Integration of Electronic Component Qualifications in the Aerospace Domain](http://arxiv.org/abs/2603.20094v1)
_Antonio De Santis, Marco Balduini, Matteo Belcao et al. | 2026-03-20 | arXiv (cs.IR) | ⭐⭐_

Uses LLMs for semantic data integration across siloed databases in aerospace, enabling cross-database retrieval of component qualification data. A practical case study of LLM-augmented information retrieval over heterogeneous enterprise data.

### [From Topic to Transition Structure: Unsupervised Concept Discovery at Corpus Scale via Predictive Associative Memory](http://arxiv.org/abs/2603.18420v1)
_Jason Dury | 2026-03-19 | arXiv (cs.IR) | ⭐⭐_

Discovers a novel 'transition-structure' embedding space via temporal co-occurrence that captures what text does rather than what it's about, complementing standard semantic embeddings. Could inform hybrid retrieval approaches that go beyond topical similarity.

### [Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures](http://arxiv.org/abs/2603.17244v1)
_Young Bin Park | 2026-03-18 | arXiv (cs.IR) | ⭐_

Presents Kumiho, a graph-native memory architecture for AI agents with formal belief revision semantics and versioned knowledge management. Tangentially relevant to knowledge-grounded retrieval and agent memory in RAG systems.

---
