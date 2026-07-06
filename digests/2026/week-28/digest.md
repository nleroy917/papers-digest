# Research Digest — 2026-W27

## Highlights

- **[HNSW with Accuracy Guarantees Using Graph Spanners -- A Technical Report](http://arxiv.org/abs/2607.02338v1)** — Directly addresses the core limitation of HNSW (no correctness guarantees) with a practical "Certify-then-Rectify" framework that bridges heuristic speed and exact retrieval rigor — essential reading for anyone operating vector indexes in production.
- **[RACORN-1: Adaptive Recall-Preserving Speedup for Low-Selectivity Filtered Vector Search](http://arxiv.org/abs/2607.00768v1)** — Filtered vector search at low selectivity is a major pain point in production RAG systems; this paper fixes ACORN-1's recall collapse below 5% selectivity with practical in-place extensions directly applicable to existing HNSW deployments.

## Graph ANN Index Improvements & Maintenance

### [HNSW with Accuracy Guarantees Using Graph Spanners -- A Technical Report](http://arxiv.org/abs/2607.02338v1)
_Minghao Li, Raghav Mittal, Sanjivni Rana et al. | 2026-07-02 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a "Certify-then-Rectify" framework for HNSW that uses graph spanners to provide distribution-free accuracy guarantees on top of greedy search. Bridges the gap between fast heuristic ANN search and provably correct retrieval.

### [RACORN-1: Adaptive Recall-Preserving Speedup for Low-Selectivity Filtered Vector Search](http://arxiv.org/abs/2607.00768v1)
_Yoonseok Kim, Gyusik Choe | 2026-07-01 | arXiv (cs.IR) | ⭐⭐⭐_

Extends ACORN-1's in-filtering approach for HNSW-based filtered vector search, fixing connectivity instability and recall collapse at very low selectivity (<5%). Directly relevant to production RAG systems using metadata filters over vector indexes.

### [When to Repair a Graph ANN Index: Navigability-Signal-Triggered Local Repair Protects Tail Recall Under Bursty Churn](http://arxiv.org/abs/2607.00728v1)
_Madhulatha Mandarapu, Sandeep Kunkunuru | 2026-07-01 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes triggering HNSW/DiskANN graph repairs based on measured navigability degradation signals rather than fixed schedules. Shows this approach maintains tail recall under bursty insert/delete churn while spending repair budgets more efficiently.

---

## RAG Architecture, Chunking & Context Packing

### [Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic Texts](http://arxiv.org/abs/2607.01852v1)
_Valentin J. J. Kreileder, Johannes Reisinger, Andreas Fischer | 2026-07-02 | arXiv (cs.IR) | ⭐⭐⭐_

Compares cluster-based semantic chunking vs. fixed-size and recursive chunking for RAG on long academic documents. Finds that RAGAs faithfulness metric is unreliable in this setting and provides empirical guidance on chunking strategy selection.

### [What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop RAG and When Submodular Evidence Packing Improves It](http://arxiv.org/abs/2607.00725v1)
_Ananto Nayan Bala | 2026-07-01 | arXiv (cs.IR) | ⭐⭐⭐_

Argues that document recall is the wrong metric for budget-constrained RAG and introduces "answer-in-context" as a diagnostic. Proposes submodular evidence packing to maximize the chance that gold answers survive into the reader's context window.

### [When RAG Meets Query Planning: Logical Query Trees for Resolving Exploratory Reasoning Problems](http://arxiv.org/abs/2607.00508v2)
_Ganlin Xu, Linghao Zhang, Zhitao Yin et al. | 2026-07-01 | arXiv (cs.IR) | ⭐⭐_

Addresses RAG's struggles with ambiguous, multi-step exploratory queries by decomposing them into logical query trees with an end-to-end planning mechanism. Reduces retrieval noise and error accumulation for complex reasoning chains.

### [One Retrieval to Cover Them All: Co-occurrence-Aware Knowledge Base Reorganization for Session-Level RAG](http://arxiv.org/abs/2606.31156v1)
_Shivam Ratnakar, Yixuan Zhu, Cecilia Cheng et al. | 2026-06-30 | arXiv (cs.IR) | ⭐⭐⭐_

Shows that standard RAG retrieval covers only 41% of session-level information needs and proposes co-occurrence-aware KB clustering with cluster neighborhood expansion. Directly practical for enterprise RAG systems serving multi-query sessions.

### [AGE: Adaptive-masking for Graph Embedding in Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2607.00052v1)
_Bao Long Nguyen Huu, Atsushi Hashimoto | 2026-06-30 | arXiv (cs.IR) | ⭐⭐_

Introduces adaptive masking for graph embeddings in GraphRAG to better align graph-based and text-based features for frozen LLMs. Addresses the representation mismatch problem when using structured graph knowledge with language models.

---

## Embedding Models, Retrieval Training & Security

### [Field Order Should Not Matter: Permutation-Invariant Embedding Model Fine-Tuning for Structured Metadata Retrieval](http://arxiv.org/abs/2606.30473v1)
_Aivin V. Solatorio, Olivier Dupriez, Rafael Macalaba | 2026-06-29 | arXiv (cs.IR) | ⭐⭐⭐_

Reveals that field serialization order silently degrades retrieval quality by 7.4 nDCG@10 points after fine-tuning text encoders on structured metadata. Proposes permutation-invariant training to make embeddings robust to field ordering — highly relevant for catalog and metadata search.

### [Real-Time Hard Negative Sampling via LLM-based Clustering for Large-Scale Two-Tower Retrieval](http://arxiv.org/abs/2607.00448v1)
_Ivan Ji, Liuyi Hu, Harrison et al. | 2026-07-01 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes using LLM-based clustering for self-supervised hard negative sampling in two-tower retrieval models. Addresses the easy-negative problem in standard in-batch/out-of-batch sampling for large-scale recommendation retrieval.

### [Embedding Inference Attack](http://arxiv.org/abs/2607.01276v1)
_Cedric Fitiavana Raelijohn, Sébastien Gambs, Jean-Francois Rajotte | 2026-07-01 | arXiv (cs.IR) | ⭐⭐_

Studies black-box attacks on IR systems where adversaries infer embedding model properties from only unordered retrieved document sets. Highlights security vulnerabilities relevant to anyone exposing embedding-based retrieval through APIs.

### [Attribute-Prompted Kernel Hashing for Unsupervised Data-Efficient Cross-Modal Retrieval](http://arxiv.org/abs/2607.00379v1)
_Runhao Li, Xiaoxu Ma, Zhenyu Weng et al. | 2026-07-01 | arXiv (cs.IR) | ⭐⭐_

Presents an attribute-prompted kernel hashing approach for cross-modal retrieval that works with scarce image-text pairs. Relevant for efficient cross-modal similarity search in data-constrained scenarios.

---

## Search Systems, Query Understanding & Evaluation

### [IntentTune: Using user demand and personalization to resolve "unknown" query intents for e-commerce search](http://arxiv.org/abs/2607.01530v1)
_Rachith Aiyappa, Ishita Khan, Chester Palen-Michel et al. | 2026-07-01 | arXiv (cs.IR) | ⭐⭐_

Addresses under-specified e-commerce queries by inferring latent user intent (age, gender, etc.) through a personalization-aware framework. Practical for improving retrieval relevance in product search systems.

### [As It Was: Aligning LLM Search Evaluation with Historical User Preferences](http://arxiv.org/abs/2607.01040v1)
_Ali Vardasbi, Gustavo Penha, Enrico Palumbo et al. | 2026-07-01 | arXiv (cs.IR) | ⭐⭐_

Proposes a behavior-grounded LLM judge that augments SERP evaluation with historical user preference signals, preventing LLM judgment drift from actual user behavior. Useful for teams using LLM-as-judge for search quality assessment.

### [Trie-based Experiment Plans for Efficient IR Pipeline Experiments](http://arxiv.org/abs/2607.01162v1)
_Irene Anu, Craig Macdonald | 2026-07-01 | arXiv (cs.IR) | ⭐⭐_

Introduces trie-based experiment plans for efficiently evaluating cascading IR pipelines (retriever combinations, re-rankers). Practical for teams running ablations over multi-stage retrieval systems.

### [Bringing Agentic Search to Earth Observation Data Discovery](http://arxiv.org/abs/2607.02387v1)
_Minghan Yu, Youran Sun, Chugang Yi et al. | 2026-07-02 | arXiv (cs.IR) | ⭐_

Deploys an agentic search system combining LLMs with knowledge graphs for NASA geoscience dataset discovery. Demonstrates a domain-specific application pattern for KG-augmented natural language search.

### [Multi-Turn Agentic Scientific Literature Search via Workflow Induction](http://arxiv.org/abs/2607.00597v1)
_Jisen Li, Bingxuan Li, Nanyi Jiang et al. | 2026-07-01 | arXiv (cs.IR) | ⭐_

Introduces PaperPilot, a multi-turn literature search agent that frames scientific search as workflow induction from anchor papers and user queries. Relevant for understanding agentic search patterns over document corpora.

---

## Recommendation & Re-ranking

### [Diffusion-GR2: Diffusion Generative Reasoning Re-ranker](http://arxiv.org/abs/2607.01170v1)
_Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen et al. | 2026-07-01 | arXiv (cs.IR) | ⭐⭐_

Applies block-diffusion language models to parallelize chain-of-thought reasoning in re-ranking, dramatically reducing inference latency versus autoregressive approaches. Relevant for teams exploring LLM-based re-rankers at scale.

### [ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping](http://arxiv.org/abs/2606.31693v1)
_Jiacheng Chen, Tao Zhang, Manxi Lin et al. | 2026-06-30 | arXiv (cs.IR) | ⭐⭐_

Proposes giving LLM agents a direct item-space interface via semantic IDs for shopping, bridging the gap between language understanding and item retrieval. Relevant to generative retrieval and semantic ID approaches for product search.

### [GR2 Technical Report](http://arxiv.org/abs/2606.31984v2)
_Yufei Li, Zaiwei Zhang, Mingfu Liang et al. | 2026-06-30 | arXiv (cs.IR) | ⭐_

Details an industrial LLM-based re-ranking system for recommendation, addressing gaps in applying LLMs to the final re-ranking stage. Provides practical lessons from production deployment at scale.

---
