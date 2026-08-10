# Research Digest — 2026-W32

## Highlights

- **[Filtered Vector Search in a Disaggregated Lakehouse: Composing Table-Format Pruning with Per-File ANN](http://arxiv.org/abs/2608.05441v1)** — Directly addresses the practical pain point of combining metadata filtering with ANN search inside open lakehouse formats (Iceberg/Parquet), offering a composable architecture that vector-DB practitioners can adopt or learn from.
- **[EXCISE: Query-Side Exclusion for Late-Interaction Retrieval](http://arxiv.org/abs/2608.05497v1)** — Identifies and fixes a fundamental failure mode ('exclusion inversion') in ColBERT-style late-interaction retrievers with a lightweight query-side module, directly useful for anyone running ColBERT-based vector search.

## RAG Architecture & Optimization

### [CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG](http://arxiv.org/abs/2608.07458v1)
_Gyuwan Kim, Cheoneum Park, Tao Yang | 2026-08-07 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes fine-grained information-nugget-level KV cache reuse for RAG, reducing redundancy beyond chunk-level caching. Optimizes the accuracy-latency Pareto frontier for long retrieved contexts, directly relevant to production RAG pipelines.

### [Exact Adaptive Hybrid Retrieval Without Fixed Top-L Cutoffs](http://arxiv.org/abs/2608.07152v1)
_Chunran Zhang | 2026-08-07 | arXiv (cs.IR) | ⭐⭐⭐_

Replaces fixed top-L truncation in hybrid dense+sparse fusion with an adaptive algorithm that dynamically determines how many candidates to read per channel. Addresses a core design decision in every hybrid retrieval system.

### [DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding](http://arxiv.org/abs/2608.07067v1)
_Hanshu Yao, Janfeng Zhong, Niu Lian et al. | 2026-08-07 | arXiv (cs.IR) | ⭐⭐_

Introduces multi-round probabilistic memory-guided retrieval for long documents, propagating state across rounds to recover from early retrieval errors. Applicable to complex document QA pipelines.

### [Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](http://arxiv.org/abs/2608.06305v2)
_Sagar Tamang, Ayush Vyas, Tabarakul Hazarika | 2026-08-06 | arXiv (cs.IR) | ⭐⭐⭐_

Argues that embedding-based top-k retrieval is structurally inadequate for table-heavy financial documents and proposes interpretable agentic operations as replacements. Highlights real failure modes of vector search on structured data.

### [Rhetorical-Role-Aware Retrieval-Augmented Generation for Legal Question Answering over Indian Supreme Court Judgments](http://arxiv.org/abs/2608.06828v1)
_Sayed Ayaan Ahmed Sha, Sangeetha Sivanesan, Anand Kumar Madasamy et al. | 2026-08-07 | arXiv (cs.IR) | ⭐⭐_

Applies rhetorical-role-based chunking, fusion retrieval, and cross-encoder reranking to legal RAG. Demonstrates domain-specific chunking strategies that improve relevance in specialized RAG applications.

### [Align-RAG: Alignment Is All You Need for TSFM In-Context Learning](http://arxiv.org/abs/2608.05571v1)
_Mohammad Asadi, Soheil Hor, Bardiya Akhbari et al. | 2026-08-06 | arXiv (cs.IR) | ⭐⭐_

Introduces a training-free RAG method for time-series foundation models using closed-form permutation alignment of retrieved examples. Shows RAG principles extending beyond text to time-series domains.

### [Cross-platform epistemic verification for improving factual reliability in AI-generated news summarization](http://arxiv.org/abs/2608.05302v1)
_Zhuo Xie, Haoze Ni | 2026-08-05 | arXiv (cs.IR) | ⭐⭐_

Proposes MECV, a multi-source evidence consensus framework that aggregates retrieval from documents, Wikipedia, and open web to correct hallucinations. Relevant to RAG reliability engineering.

---

## Vector Search & Retrieval Infrastructure

### [Filtered Vector Search in a Disaggregated Lakehouse: Composing Table-Format Pruning with Per-File ANN](http://arxiv.org/abs/2608.05441v1)
_Rakesh Jain, Thomas Griffin, Syed Zawad | 2026-08-05 | arXiv (cs.IR) | ⭐⭐⭐_

Integrates ANN search into Iceberg/Parquet lakehouse tables, composing partition pruning and zone-maps with per-file vector indexes. Directly relevant to engineers building filtered vector search at scale.

### [EXCISE: Query-Side Exclusion for Late-Interaction Retrieval](http://arxiv.org/abs/2608.05497v1)
_Mohammed Ali, Abdelrahman Abdallah, Adam Jatowt | 2026-08-06 | arXiv (cs.IR) | ⭐⭐⭐_

Fixes the 'exclusion inversion' problem in ColBERT-style retrievers where negated query terms boost rather than suppress documents. A 1.5M-parameter query-side module corrects scoring without modifying the index.

### [omni-macos: On-Device Omni-Modal Search on Apple Silicon](http://arxiv.org/abs/2608.05543v1)
_Han Xiao | 2026-08-06 | arXiv (cs.IR) | ⭐⭐⭐_

Ships a complete multi-modal embedding + vector index engine on-device for Mac, supporting text, code, images, audio, and video in one representation space. Demonstrates practical on-device vector search under tight memory budgets.

### [A Mechanistic Analysis of Gender Sensitivity in Dense Retrieval Models](http://arxiv.org/abs/2608.05467v1)
_Catherine Chen, Maarten de Rijke, Carsten Eickhoff | 2026-08-05 | arXiv (cs.IR) | ⭐⭐_

Mechanistically localizes gender bias in bi-encoder retrieval models to specific input embeddings and late-layer attention heads. Important for understanding and mitigating bias in dense retrieval systems.

---

## Recommendation Systems

### [Gryphon-v2: One Model in Place of a Cascade - Generate-and-Rank Recommender with Rollout Distillation](http://arxiv.org/abs/2608.06213v1)
_Anna Lipkina, Daria Tikhonovich, Viktor Yanush et al. | 2026-08-06 | arXiv (cs.IR) | ⭐⭐_

Replaces multi-stage retrieval-ranking cascades with a single generative retrieval model using semantic IDs and rollout distillation. Shows how generative retrieval can simplify industrial recommendation pipelines.

### [Hierarchical Quantization with Domain-Adaptive Sparse Routing for Generative Cross-Domain Recommendation](http://arxiv.org/abs/2608.06997v1)
_Haiying He, Xiaopeng Li, Yuchen Gu et al. | 2026-08-07 | arXiv (cs.IR) | ⭐⭐_

Extends generative recommendation with hierarchical semantic IDs and domain-adaptive sparse routing for cross-domain settings. Relevant to understanding semantic ID quantization for item retrieval.

### [DEGR: Dual Exploration-Driven Generative Re-Ranking for Adaptive Cross-Request Context Bridging](http://arxiv.org/abs/2608.04809v1)
_Binglei Zhao, Xuanhua Yang, Xiwei Zhao et al. | 2026-08-05 | arXiv (cs.IR) | ⭐_

Proposes a generative re-ranking method that balances immediate and exploratory value in industrial recommendation, improving sequence-level optimization under low-quality supply.

### [ATLAS: Learning to Recommend Across Unseen Domains](http://arxiv.org/abs/2608.03899v1)
_Pervez Shaik, Prosenjit Biswas, Abhinav Thorat et al. | 2026-08-04 | arXiv (cs.IR) | ⭐_

Proposes a zero-shot cross-domain recommendation model that generalizes to unseen item catalogues without retraining. Relevant to universal embedding approaches for recommendation.

### [Is Personalized Modality Weighting Actually Personalized? A Controlled Audit of Per-User Weighting Claims in Multimodal Recommenders](http://arxiv.org/abs/2608.05655v1)
_Jingyuan Zheng, Xin Zhang, Yang Gu et al. | 2026-08-06 | arXiv (cs.IR) | ⭐_

Audits whether per-user modality weighting in multimodal recommenders captures genuinely user-specific signals or just global modality preferences. Methodologically interesting for multimodal retrieval evaluation.

---

## Agent Memory & Skill Retrieval

### [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](http://arxiv.org/abs/2608.04746v1)
_Kartikey Singh Bhandari, Aarya Wadhwani, Dhruv Kumar et al. | 2026-08-05 | arXiv (cs.IR) | ⭐⭐_

Introduces type-conditioned temporal decay for LLM agent memory stores, preventing retrieval contamination from stale facts. Directly relevant to memory management in agentic RAG systems.

### [Skills Know Their Neighbors: Cluster-Contrastive Capability Pages for Skill Retrieval](http://arxiv.org/abs/2608.04482v1)
_Zifei Wang, Wei Wen, Qiang Ji et al. | 2026-08-05 | arXiv (cs.IR) | ⭐⭐_

Formalizes skill retrieval as an executable-region problem and proposes cluster-contrastive document augmentation so retrievers can distinguish similar but functionally different skills. Relevant to tool-use retrieval in agents.

### [Invisible to the Machine: Auditing AI Restaurant, Cafe, and Bar Recommendation Against a Complete Market Census](http://arxiv.org/abs/2608.07069v1)
_Vladimir Pitenin | 2026-08-07 | arXiv (cs.IR) | ⭐_

First census-denominated audit of AI venue recommendation, revealing which venues AI assistants surface vs. ignore. Interesting for understanding retrieval coverage and bias in production systems.

---

## Evaluation & Bias in IR

### [Cleo: A Transparent and Controllable Chatbot for Conversational Commerce](http://arxiv.org/abs/2608.06068v1)
_Kevin Schott, Jan Lattenkamp, Daniel Hienert et al. | 2026-08-06 | arXiv (cs.IR) | ⭐_

Demonstrates a conversational product advisor with explainable ranking and controllable LLM behavior. Relevant to practitioners building transparent retrieval-based chat systems.

### [Neighborhood-Aware Dual Biomedical Entity Linking](http://arxiv.org/abs/2608.04144v1)
_Yicheng Tao, Jie Liu | 2026-08-04 | arXiv (cs.IR) | ⭐⭐_

Proposes PILOT for biomedical entity linking, leveraging KB ontological structure and neighborhood awareness. Relevant to embedding-based entity retrieval in specialized knowledge bases.

### [From Classification to Recommendation: Empirical Analysis of Audio Embedding Models Application for Content-Based Music Recommendation](http://arxiv.org/abs/2608.06928v1)
_Qingrui Li, Haowei Lou, Chengkai Huang et al. | 2026-08-07 | arXiv (cs.IR) | ⭐⭐_

Evaluates how well pretrained audio embedding models transfer to content-based music recommendation via nearest-neighbor retrieval. Directly tests embedding quality for similarity search in the audio domain.

---
