# Research Digest — 2026-W25

## Highlights

- **[Query-aware Routing for Filtered Approximate Nearest Neighbors Search](http://arxiv.org/abs/2606.19898v1)** — Directly addresses a core vector database primitive (filtered ANN), benchmarks all major methods, and proposes a practical lightweight routing framework that adapts strategy per-query — immediately actionable for Qdrant/Pinecone/Weaviate practitioners.
- **[MonaVec: A Training-Free Embedded Vector Search Kernel for Edge and Offline AI Systems](http://arxiv.org/abs/2606.19458v1)** — Presents a SQLite-like embedded vector search engine with training-free quantization, targeting edge/offline deployments — a novel and practical design point that fills a real gap in the vector search ecosystem.

## Vector Search & ANN Index Innovations

### [Query-aware Routing for Filtered Approximate Nearest Neighbors Search](http://arxiv.org/abs/2606.19898v1)
_Qianqian Xiong, Mengxuan Zhang | 2026-06-18 | arXiv (cs.IR) | ⭐⭐⭐_

Benchmarks all major categorical filtered ANN methods and shows no single method dominates even within a dataset. Proposes a lightweight ML-based routing framework that predicts the best filtered ANN strategy per query, improving recall and latency trade-offs.

### [When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems](http://arxiv.org/abs/2606.19692v1)
_Prashant Kumar Pathak, Tarun Kumar Sharma | 2026-06-18 | arXiv (cs.IR) | ⭐⭐⭐_

Addresses the vector hubness problem where a few points dominate nearest-neighbor lists, creating a poisoning risk in RAG. Proposes an admission-time gating mechanism using sentinel queries to quarantine hub-like documents before index insertion, avoiding costly periodic rescans.

### [MonaVec: A Training-Free Embedded Vector Search Kernel for Edge and Offline AI Systems](http://arxiv.org/abs/2606.19458v1)
_Oğuzhan Yenen | 2026-06-17 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces an embedded, single-file vector search kernel inspired by SQLite's deployment model. Uses a training-free Randomized Hadamard Transform quantization scheme that is data-oblivious, targeting resource-constrained edge and offline environments.

### [Compact Geometric Representations of Hierarchies](http://arxiv.org/abs/2606.18520v1)
_Prashant Gokhale, Piotr Indyk, Yuhao Liu et al. | 2026-06-16 | arXiv (cs.IR) | ⭐⭐_

Studies how to compute compact geometric embeddings for hierarchical (DAG-based) retrieval. Extends dual-encoder embedding approaches to ancestor-descendant relationships, relevant for structured/taxonomic search scenarios.

### [Non-negative Elastic Net Decoding for Information Retrieval](http://arxiv.org/abs/2606.17910v1)
_Koki Okajima, Yasutoshi Ida, Tsukasa Yoshida et al. | 2026-06-16 | arXiv (cs.IR) | ⭐⭐_

Proposes a corpus-aware decoding approach for dense retrieval that reduces redundancy in top-k results by using non-negative elastic net optimization over document embeddings, addressing a fundamental limitation of independent scoring in dense retrieval.

---

## RAG Architecture & Chunking Strategies

### [MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval](http://arxiv.org/abs/2606.18508v1)
_Amirhossein Abaskohi, Raymond Li, Gaetano Cimino et al. | 2026-06-16 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces topic metadata augmentation for paragraph-level chunks in RAG, balancing retrieval precision with semantic coherence. Addresses the fundamental chunking granularity trade-off that plagues production RAG systems.

### [SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG](http://arxiv.org/abs/2606.18381v1)
_Amirhossein Abaskohi, Issam H. Laradji, Peter West et al. | 2026-06-16 | arXiv (cs.IR) | ⭐⭐⭐_

Presents a hierarchical RAG framework using attention-guided tree search with progressive embeddings. Avoids costly LLM calls during indexing while enabling multi-granularity context aggregation for long documents.

### [PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents](http://arxiv.org/abs/2606.20047v1)
_Manu Ghulyani, Arunabh Singh, Karan Bharadwaj et al. | 2026-06-18 | arXiv (cs.IR) | ⭐⭐_

Proposes submodular optimization for context window management in LLM agents, replacing naive recency truncation. Relevant to RAG systems that must select which retrieved passages to include when context budgets are limited.

### [When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation](http://arxiv.org/abs/2606.20113v1)
_Elroy Galbraith | 2026-06-18 | arXiv (cs.IR) | ⭐⭐_

Analyzes streaming RAG where tool queries are issued before user input is complete. Introduces the concept of tool-intent stabilization — the point at which speculative retrieval becomes reliable — providing practical guidance for latency optimization.

### [Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries](http://arxiv.org/abs/2606.19960v1)
_Yuxiang Guo, Zhonghao Hu, Yuren Mao et al. | 2026-06-18 | arXiv (cs.IR) | ⭐⭐_

Addresses the memory overhead of multi-vector representations in multimodal document retrieval for RAG. Proposes a scalable approach to reduce the cost of late-interaction retrieval while maintaining effectiveness.

---

## Reranking, Sparse Retrieval & Retrieval Model Training

### [Rescaling MLM-Head for Neural Sparse Retrieval](http://arxiv.org/abs/2606.18811v1)
_Youngjoon Jang, Seongtae Hong, Jonah Turner et al. | 2026-06-17 | arXiv (cs.IR) | ⭐⭐⭐_

Identifies a critical scale mismatch bug when using stronger pretrained encoders as SPLADE backbones: large MLM-head L2 norms cause training collapse. Proposes a simple rescaling fix that unlocks improved sparse retrieval with modern backbones.

### [Querit-Reranker: Training Compact Multilingual Rerankers via Efficient Label-Free Distribution Adaptation](http://arxiv.org/abs/2606.19037v1)
_Yunfei Zhong, Jun Yang, Wei Huang et al. | 2026-06-17 | arXiv (cs.IR) | ⭐⭐⭐_

Presents a data-centric pipeline for training compact multilingual cross-encoder rerankers without requiring task-specific relevance labels. The 0.4B parameter model achieves strong cross-lingual generalization, making it practical for production reranking.

### [RSRank: Learning Relevance from Representational Shifts](http://arxiv.org/abs/2606.17468v1)
_Archit Gupta, Sai Sundaresan, Debabrata Mahapatra | 2026-06-16 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a reranking method that uses representational shifts rather than raw logits for relevance scoring, addressing the mismatch between next-token prediction training and relevance assessment in RAG filtering pipelines.

### [Temporal Preference Optimization for Unsupervised Retrieval](http://arxiv.org/abs/2606.17664v1)
_HyunJin Kim, Jaejun Shim, Young Jin Kim et al. | 2026-06-16 | arXiv (cs.IR) | ⭐⭐_

Addresses temporal misalignment in unsupervised dense retrieval where semantically similar but temporally wrong documents are retrieved. Introduces temporal preference optimization without requiring explicit temporal supervision.

### [Understanding and Debugging Failures in N-Gram-Based Generative Retrieval](http://arxiv.org/abs/2606.17721v1)
_Richard Takacs, Adrian Bracher, Svitlana Vakulenko | 2026-06-16 | arXiv (cs.IR) | ⭐⭐_

Provides a taxonomy of failure modes in generative retrieval systems where models directly generate document identifiers. Empirically investigates n-gram-based methods, offering debugging insights for this emerging IR paradigm.

---

## Multimodal & Cross-Lingual Retrieval

### [ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval](http://arxiv.org/abs/2606.20280v1)
_Yuhan Liu, Pei Fu, Hang Li et al. | 2026-06-18 | arXiv (cs.IR) | ⭐⭐_

Identifies 'grain blindness' in contrastive-learning-based multimodal retrieval where models overlook query granularity. Proposes a ranking-driven approach for universal multimodal retrieval that better handles complex multi-grain queries.

### [SHIFT: Semantic Harmonization via Index-side Feature Transformation for Multilingual Information Retrieval](http://arxiv.org/abs/2606.18801v1)
_Youngjoon Jang, Seongtae Hong, Hyeonseok Moon et al. | 2026-06-17 | arXiv (cs.IR) | ⭐⭐_

Addresses language bias in multilingual dense retrieval where models prefer same-language documents. Proposes index-side feature transformations to harmonize cross-lingual embeddings, directly relevant to multilingual vector search deployments.

### [LARE: Low-Attention Region Encoding for Text-Image Retrieval](http://arxiv.org/abs/2606.18885v1)
_Abdulmalik Alquwayfili, Faisal Almeshal, Jumanah Almajnouni et al. | 2026-06-17 | arXiv (cs.IR) | ⭐⭐_

Proposes dual-encoding of low-attention and full image regions for text-image retrieval in crowded scenes. Addresses salience bias in visual encoders to improve fine-grained cross-modal retrieval.

### [VCG: A Multimodal Retrieval Framework for E-Commerce Video Feeds under Extreme Cold-Start Conditions](http://arxiv.org/abs/2606.19627v1)
_Katya Mirylenka, Egor Malykh, Mahdyar Ravanbakhsh et al. | 2026-06-17 | arXiv (cs.IR) | ⭐⭐_

Presents a scalable multimodal video candidate generation system for e-commerce that handles extreme cold-start by leveraging content features instead of interaction history. Addresses position and duration biases in video feed retrieval.

---

## Agentic Search & Knowledge Retrieval

### [Beyond Parallel Sampling: Diverse Query Initialization for Agentic Search](http://arxiv.org/abs/2606.17209v1)
_Sidhaarth Murali, João Coelho, Jingjie Ning et al. | 2026-06-15 | arXiv (cs.IR) | ⭐⭐_

Shows that parallel rollouts in agentic search suffer from query redundancy at the first turn, leading to overlapping evidence retrieval. Proposes diverse query initialization to improve breadth scaling for multi-step retrieval agents.

### [Multi-Agent Transactive Memory](http://arxiv.org/abs/2606.19911v1)
_To Eun Kim, Xuhong He, Dishank Jain et al. | 2026-06-18 | arXiv (cs.IR) | ⭐⭐_

Extends RAG to multi-agent settings where retrieval systems organize and index agent-generated artifacts for reuse across heterogeneous agent populations. Draws parallels between search engine indexing and agent knowledge sharing.

### [RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning in Recommendation](http://arxiv.org/abs/2606.18379v1)
_Renzhi Wu, Zikun Cui, Junjie Yang et al. | 2026-06-16 | arXiv (cs.IR) | ⭐⭐_

Describes Meta's production system for billion-node graph-based retrieval, co-designing graph construction, representation learning, and real-time serving with co-learned cluster indices. Offers insights relevant to large-scale similarity search infrastructure.

---
