# Research Digest — 2026-W28

## Highlights

- **[Learn to Pool: Lightweight Fine-Tuning for Flexible Multi-Vector Compression](http://arxiv.org/abs/2607.06036v1)** — Directly addresses the key deployment bottleneck of late-interaction models (e.g., ColBERT) by learning to pool token vectors, reducing storage and memory costs with minimal accuracy loss — immediately actionable for vector search practitioners.
- **[Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](http://arxiv.org/abs/2607.05803v1)** — Provides the first theoretical analysis of MaxSim's representation power compared to single-vector and sparse models, offering foundational insights for anyone choosing between retrieval architectures.

## Late-Interaction & Multi-Vector Retrieval Efficiency

### [Learn to Pool: Lightweight Fine-Tuning for Flexible Multi-Vector Compression](http://arxiv.org/abs/2607.06036v1)
_Stefan Josef | 2026-07-07 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a lightweight fine-tuning approach to pool token-level vectors in late-interaction models like ColBERT, compressing storage footprint while preserving retrieval accuracy. Demonstrates pooling-aware training yields strong results even at high compression ratios, directly relevant to anyone deploying multi-vector indices.

### [Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](http://arxiv.org/abs/2607.05803v1)
_Julian Killingback, Varad Ingale, Hamed Zamani et al. | 2026-07-07 | arXiv (cs.IR) | ⭐⭐⭐_

Shows by construction that MaxSim can exactly replicate inner products between non-negative sparse vectors, establishing formal expressiveness results for late-interaction models. Provides theoretical grounding for when and why MaxSim outperforms single-vector approaches.

### [Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval](http://arxiv.org/abs/2607.04605v1)
_Suhyeong Park, Junha Jung, Jungwoo Park et al. | 2026-07-06 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes SaMer, an object-aware token merging framework that compresses image-side tokens in vision-language late-interaction retrieval while preserving object-level evidence. Reduces storage and scoring costs for multi-vector visual retrieval systems.

### [CMDR: Contextual Multimodal Document Retrieval](http://arxiv.org/abs/2607.05927v1)
_Ryota Tanaka, Taku Hasegawa, Kyosuke Nishida | 2026-07-07 | arXiv (cs.IR) | ⭐⭐_

Introduces a benchmark and method for multimodal document retrieval that encodes cross-page context rather than treating pages independently. Highlights limitations of current page-level indexing approaches for document-level queries.

---

## RAG Systems & Multi-Hop Retrieval

### [DynaKRAG: A Unified Framework for Learnable Evidence Control in Multi-Hop Retrieval-Augmented Generation](http://arxiv.org/abs/2607.06507v1)
_Yaqi Wu, Xiaolei Guo, Chenyu Zhou et al. | 2026-07-07 | arXiv (cs.IR) | ⭐⭐⭐_

Unifies iterative retrieval, query reformulation, evidence critique, and sufficiency judging into a learnable state-conditioned control policy for multi-hop RAG. Addresses a key pain point in production RAG pipelines where fixed control flow fails for complex queries.

### [Interpretable Uncertainty for Adaptive Retrieval and Reasoning in Question Answering](http://arxiv.org/abs/2607.07380v1)
_Ritajit Dey, Iadh Ounis, Graham McDonald | 2026-07-08 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes an uncertainty-aware framework that uses LLM internal signals to decide when and how to retrieve, making RAG more efficient and transparent. Directly applicable to building adaptive retrieval-augmented QA systems.

### [Retrieving a Set, Not Independent Passages: Set-Level Compatibility Learning for Efficient Set Exploration](http://arxiv.org/abs/2607.05712v1)
_Mooho Song, Jay-Yoon Lee | 2026-07-07 | arXiv (cs.IR) | ⭐⭐⭐_

Formulates multi-hop retrieval as set-level selection rather than independent passage scoring, learning passage compatibility for jointly useful evidence. Addresses a fundamental limitation of standard dense retrieval for complex reasoning tasks.

### [Inject or Navigate? Token-Efficient Retrieval for LLM Analysis of Transactional Legal Documents](http://arxiv.org/abs/2607.05764v1)
_Mahmoud Hany, Mourad ElSheraey, Mahmoud Said et al. | 2026-07-07 | arXiv (cs.IR) | ⭐⭐_

Compares full-corpus injection versus structured retrieval for legal document analysis with LLMs, quantifying the token-efficiency vs. recall trade-off. Practical lessons for RAG system designers on when context-stuffing fails.

### [Conversational Retrieval and On-the-Fly Knowledge Modeling of Historical Penitentiary Repression Records](http://arxiv.org/abs/2607.08459v1)
_Paula Font Solà, Adrià Molina Rodríguez, Josep Lladós | 2026-07-09 | arXiv (cs.IR) | ⭐⭐_

Presents a RAG-based conversational system for historical digital libraries that goes beyond extractive QA to holistic collection interpretation. Demonstrates RAG applied to structured archival data with dynamic expert knowledge integration.

### [Curated retrieval versus open web search in public AI information services: a coverage-trust trade-off](http://arxiv.org/abs/2607.05217v2)
_Hafsteinn Einarsson, Hafsteinn Birgir Einarsson, Jón Gunnar Ólafsson et al. | 2026-07-06 | arXiv (cs.IR) | ⭐⭐_

Empirically evaluates the trade-off between curated knowledge bases and live web search in a public RAG-powered information service. Provides evidence on source trustworthiness relevant to RAG pipeline design decisions.

---

## Hashing, Embeddings & Benchmarks

### [H3D: Benchmarking Unsupervised Text Hashing for Fine-Grained Document Deduplication](http://arxiv.org/abs/2607.08382v1)
_Qianren Mao, Jiaxun Lyu, Junnan Liu et al. | 2026-07-09 | arXiv (cs.IR) | ⭐⭐⭐_

Benchmarks MinHash, SimHash, Winnowing, FuzzyHash, FlyHash alongside semantic methods (BGE embeddings) under a unified protocol for document deduplication. Essential reading for anyone building deduplication into vector search pipelines.

### [MTEB-BR: A Text Embedding Benchmark for Brazilian Portuguese](http://arxiv.org/abs/2607.04581v2)
_Tardelli Ronan Coelho Stekel | 2026-07-06 | arXiv (cs.IR) | ⭐⭐_

Introduces 22 native Brazilian-Portuguese tasks across seven categories for evaluating text embeddings. Important for practitioners deploying multilingual embedding models and needing language-specific benchmarks beyond English.

### [Evaluation and Explainability of Unsupervised Scholarly Collaboration Recommendations](http://arxiv.org/abs/2607.04529v1)
_Md Asaduzzaman Noor, John W. Sheppard, Jason A. Clark | 2026-07-05 | arXiv (cs.IR) | ⭐⭐_

Compares TF-IDF, topic models, and SciBERT+Faiss embedding retrieval for scholarly collaboration recommendations. Provides practical insights on embedding-based retrieval versus traditional methods in a real-world use case.

### [Submitted and Diagnostic Analysis of Full-Text Temporal Retrieval for LongEval-Sci](http://arxiv.org/abs/2607.04088v1)
_Yingdong Yang, Haijian Wu | 2026-07-05 | arXiv (cs.IR) | ⭐⭐_

Reports experiments on scientific retrieval under temporal collection change, comparing BM25, dense baselines, query expansion, and cross-encoder reranking. Useful for understanding how retrieval systems degrade as document collections evolve.

---

## Retrieval Architecture & Search Paradigms

### [DaV-Gen: End-to-End Generative Retrieval via Draft-and-Verify](http://arxiv.org/abs/2607.08365v1)
_Meng Zhao, Chunmei Liu, Qinyong Wang | 2026-07-09 | arXiv (cs.IR) | ⭐⭐_

Proposes an end-to-end generative retrieval model using a draft-and-verify mechanism to bypass the inconsistency of multi-stage cascade retrieval-ranking pipelines. Relevant to those exploring alternatives to traditional vector retrieval architectures.

### [Improving Ad-hoc Search Effectiveness for Conversational Information Retrieval via Model Merging](http://arxiv.org/abs/2607.08540v1)
_Ahmed Rayane Kebir, Jose G. Moreno, Lynda Tamine | 2026-07-09 | arXiv (cs.IR) | ⭐⭐_

Uses model merging (rather than retraining) to adapt ad-hoc retrievers for conversational search, reducing cost while handling topic shifts and coreference. A practical approach for extending existing retrieval models to conversational settings.

### [BACH: A Bayesian Admixture of Contrastive Heads for Multi-Interest Two-Tower Retrieval](http://arxiv.org/abs/2607.08107v1)
_Quoc Phong Nguyen, Paul Albert, Long Vuong et al. | 2026-07-09 | arXiv (cs.IR) | ⭐⭐⭐_

Addresses routing collapse in multi-interest two-tower retrieval by casting it as a Bayesian mixture over contrastive heads. Directly relevant to practitioners building recommendation or personalized search systems using vector retrieval.

### [InfluMatch: Frontier-Quality KOL Search at 4B-Model Cost](http://arxiv.org/abs/2607.05968v1)
_Krittanon Kaewtawee, Petmongkon Pornpichitsuwan, Natchaya Temyingyong et al. | 2026-07-07 | arXiv (cs.IR) | ⭐⭐_

Builds a retrieve→rerank→reason cascade using small open-weight models for influencer matching, achieving frontier LLM quality at fraction of cost. Demonstrates practical retrieval cascade design with dense retrieval and lightweight reranking.

### [The New Shape of Search: How Conversational AI Recomposes Information Seeking](http://arxiv.org/abs/2607.04282v1)
_Michael Iannelli, Alan Ai | 2026-07-05 | arXiv (cs.IR) | ⭐_

Analyzes how conversational AI assistants change the structure of information-seeking episodes compared to traditional search. Provides high-level insights on the evolving search paradigm but less directly actionable for system builders.

---

## Recommendation Systems

### [From Raw IDs to Semantic Planning: How Recommender Systems Utilize Information at Scale](http://arxiv.org/abs/2607.09540v1)
_Changhong Jin, Shiqiu Yang, Roger Zhe Li et al. | 2026-07-10 | arXiv (cs.IR) | ⭐⭐_

Surveys the evolution of recommender systems from ID-based memorization to semantic representations. Useful background for understanding how embedding-based retrieval fits into modern recommendation architectures.

### [LBR: Towards Mitigating Length Bias in Large Language Models for Recommendation](http://arxiv.org/abs/2607.04270v1)
_Hongchen Li, Bohao Wang, Jingbang Chen et al. | 2026-07-05 | arXiv (cs.IR) | ⭐_

Identifies and addresses length bias in LLM-based recommender systems where longer item descriptions receive disproportionate attention. Relevant to practitioners using LLMs for item representation but less directly to vector search.

---
