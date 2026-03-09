# Research Digest — 2026-W10

## Highlights

- **[Efficient Vector Search in the Wild: One Model for Multi-K Queries](http://arxiv.org/abs/2603.06159v1)** — Directly addresses a core pain point for vector search practitioners: serving real-world workloads with varying top-K values from a single learned index, offering both accuracy and performance gains.
- **[Scaling Laws for Reranking in Information Retrieval](http://arxiv.org/abs/2603.04816v1)** — Establishes predictable scaling laws for the reranking stage of multi-stage retrieval pipelines, giving practitioners actionable guidance on how model size, data, and compute trade off in production systems.

## Vector Search & Retrieval Efficiency

### [Efficient Vector Search in the Wild: One Model for Multi-K Queries](http://arxiv.org/abs/2603.06159v1)
_Yifan Peng, Jiafei Fan, Xingda Wei et al. | 2026-03-06 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes OMEGA, a K-generalizable learned top-K search model that serves multi-K vector queries without retraining. It avoids accuracy degradation for large K and performance loss for small K, solving a key real-world deployment problem for vector search systems.

### [Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion](http://arxiv.org/abs/2603.06397v1)
_Pengcheng Jiang, Judith Yue Li, Moonkyung Ryu et al. | 2026-03-06 | arXiv (cs.IR) | ⭐⭐_

Addresses set-valued retrieval where the system must return collections optimizing higher-order properties like diversity and coverage. Uses RL-compiled diffusion to produce property-aligned result sets grounded in a fixed database, relevant for advanced retrieval scenarios.

### [CONE: Embeddings for Complex Numerical Data Preserving Unit and Variable Semantics](http://arxiv.org/abs/2603.04741v1)
_Gyanendra Shrestha, Anna Pyayt, Michael Gubanov | 2026-03-05 | arXiv (cs.IR) | ⭐⭐_

Proposes a hybrid transformer encoder that properly encodes numbers, ranges, and units into embeddings. Relevant for vector search practitioners dealing with numerical or structured data where standard text embeddings lose semantic precision.

---

## Reranking, Distillation & Multi-Stage Retrieval

### [Scaling Laws for Reranking in Information Retrieval](http://arxiv.org/abs/2603.04816v1)
_Rahul Seetharaman, Aman Bansal, Hamed Zamani et al. | 2026-03-05 | arXiv (cs.IR) | ⭐⭐⭐_

Derives scaling laws specifically for the reranking stage in multi-stage retrieval systems, showing how performance predictably improves with model size, data, and compute. Essential reading for anyone tuning production retrieval pipelines.

### [Reproducing and Comparing Distillation Techniques for Cross-Encoders](http://arxiv.org/abs/2603.03010v1)
_Victor Morand, Mathias Vast, Basile Van Cooten et al. | 2026-03-03 | arXiv (cs.IR) | ⭐⭐⭐_

Systematically reproduces and compares knowledge distillation strategies for cross-encoder rerankers across multiple backbone sizes. Clarifies which distillation approaches let traditional cross-encoders match LLM reranker effectiveness.

### [Constraint-Aware Generative Re-ranking for Multi-Objective Optimization in Advertising Feeds](http://arxiv.org/abs/2603.04227v1)
_Chenfei Li, Hantao Zhao, Weixi Yao et al. | 2026-03-04 | arXiv (cs.IR) | ⭐⭐_

Proposes a constraint-aware generative reranking framework that transforms constrained optimization into bounded neural decoding for advertising feeds. Addresses latency and constraint-handling issues in production reranking.

### [Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking in Recommender Systems](http://arxiv.org/abs/2603.03770v1)
_Pengfei Tong, Siyuan Chen, Chenwei Zhang et al. | 2026-03-04 | arXiv (cs.IR) | ⭐⭐_

Reveals gradient conflicts caused by mixing heterogeneous samples in multi-stage pre-ranking and proposes a heterogeneity-aware approach. Relevant for large-scale retrieval pipelines with distinct retrieval and ranking stages.

### [OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation](http://arxiv.org/abs/2603.02999v2)
_Dekai Sun, Yiming Liu, Jiafan Zhou et al. | 2026-03-03 | arXiv (cs.IR) | ⭐⭐_

Unifies generative retrieval and ranking into a single model for advertising recommendation, addressing misalignment between generation and ranking stages. Demonstrates a practical approach to collapsing multi-stage cascaded systems.

---

## RAG Systems & Knowledge-Augmented Retrieval

### [Core-based Hierarchies for Efficient GraphRAG](http://arxiv.org/abs/2603.05207v1)
_Jakir Hossain, Ahmet Erdem Sarıyüce | 2026-03-05 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes replacing Leiden clustering with core-based hierarchical decomposition in GraphRAG, proving advantages on sparse knowledge graphs. Directly improves the graph-based RAG pipeline used for global sensemaking across documents.

### [CBR-to-SQL: Rethinking Retrieval-based Text-to-SQL using Case-based Reasoning in the Healthcare Domain](http://arxiv.org/abs/2603.05569v1)
_Hung Nguyen, Hans Moen, Pekka Marttinen | 2026-03-05 | arXiv (cs.IR) | ⭐⭐_

Improves RAG-based text-to-SQL by replacing single-step retrieval with iterative case-based reasoning, handling the variability and noise typical in healthcare EHR databases. Demonstrates a practical pattern for domain-adapted retrieval.

### [AutothinkRAG: Complexity-Aware Control of Retrieval-Augmented Reasoning for Image-Text Interaction](http://arxiv.org/abs/2603.05551v1)
_Jiashu Yang, Chi Zhang, Abudukelimu Wuerkaixi et al. | 2026-03-05 | arXiv (cs.IR) | ⭐⭐_

Introduces complexity-aware routing for multimodal RAG, dynamically controlling retrieval depth based on query difficulty. Addresses efficiency and reasoning bottlenecks in document QA with mixed image-text content.

### [Detecting RAG Advertisements Across Advertising Styles](http://arxiv.org/abs/2603.04925v1)
_Sebastian Heineking, Wilhelm Pertsch, Ines Zelch et al. | 2026-03-05 | arXiv (cs.IR) | ⭐⭐_

Develops a taxonomy of advertising styles injected into RAG outputs and benchmarks detection methods. Important for RAG system builders concerned about content integrity and adversarial context injection.

### [DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval](http://arxiv.org/abs/2603.04743v1)
_Maojun Sun, Yue Wu, Yifei Xie et al. | 2026-03-05 | arXiv (cs.IR) | ⭐⭐_

Proposes distribution-aware retrieval embeddings that incorporate data characteristics alongside function semantics for tool retrieval. Demonstrates that enriching retrieval representations beyond text semantics improves match quality.

### [Model Editing for New Document Integration in Generative Information Retrieval](http://arxiv.org/abs/2603.02773v1)
_Zhen Zhang, Zihan Wang, Xinyu Ma et al. | 2026-03-03 | arXiv (cs.IR) | ⭐⭐_

Addresses the critical problem of adding new documents to generative retrieval models without full retraining. Uses model editing techniques to update docID generation, avoiding catastrophic forgetting and expensive incremental training.

---

## IR Benchmarks & Evaluation

### [Still Fresh? Evaluating Temporal Drift in Retrieval Benchmarks](http://arxiv.org/abs/2603.04532v1)
_Nathan Kuissi, Suraj Subrahmanyan, Nandan Thakur et al. | 2026-03-04 | arXiv (cs.IR) | ⭐⭐⭐_

Investigates how temporal corpus drift affects retrieval benchmarks by comparing two snapshots of FreshStack a year apart. Essential reading for anyone relying on static benchmarks to evaluate retrieval systems over evolving technical corpora.

### [τ-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge](http://arxiv.org/abs/2603.04370v1)
_Quan Shi, Alexandra Zytek, Pedram Razavi et al. | 2026-03-04 | arXiv (cs.IR) | ⭐⭐_

Introduces a benchmark for evaluating conversational agents that must retrieve and apply domain knowledge from unstructured corpora during live interactions. Fills a gap between isolated retrieval and tool-use evaluation.

### [The Science Data Lake: A Unified Open Infrastructure Integrating 293 Million Papers Across Eight Scholarly Sources with Embedding-Based Ontology Alignment](http://arxiv.org/abs/2603.03126v1)
_Jonas Wilinski | 2026-03-03 | arXiv (cs.IR) | ⭐⭐_

Presents a locally-deployable infrastructure unifying 293M papers from eight sources using DOI normalization and embedding-based ontology alignment. Useful as a large-scale corpus for retrieval research and embedding experiments.

### [Behind the Prompt: The Agent-User Problem in Information Retrieval](http://arxiv.org/abs/2603.03630v1)
_Saber Zerhoudi, Michael Granitzer, Dang Hai Dang et al. | 2026-03-04 | arXiv (cs.IR) | ⭐_

Examines a fundamental challenge for IR systems when the user is an AI agent with hidden instructions: observed behavior no longer reliably reveals intent. A thought-provoking conceptual piece on the future of IR evaluation and user modeling.

---

## Conversational Search & Intent Understanding

### [Sensitivity-Aware Retrieval-Augmented Intent Clarification](http://arxiv.org/abs/2603.06025v1)
_Maik Larooij | 2026-03-06 | arXiv (cs.IR) | ⭐⭐_

Augments intent clarification in conversational search with a retrieval step, framed within the exploratory search paradigm. Proposes sensitivity-aware approaches that balance clarification performance with user data concerns.

### [ChatShopBuddy: Towards Reliable Conversational Shopping Agents via Reinforcement Learning](http://arxiv.org/abs/2603.06065v1)
_Yiruo Cheng, Kelong Mao, Tianhao Li et al. | 2026-03-06 | arXiv (cs.IR) | ⭐_

Applies RL-based post-training to optimize conversational shopping agents that must balance product correctness, persuasiveness, and other objectives. Relevant as a case study of retrieval-powered conversational agents in e-commerce.

---
