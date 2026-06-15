# Research Digest — 2026-W24

## Highlights

- **[The Clustering Strikes Back: Building Cost-Effective and High-Performance ANNS at Scale with Helmsman](http://arxiv.org/abs/2606.13145v1)** — A battle-tested production ANNS system from Xiaohongshu detailing how to replace in-memory HNSW with clustering-based indexes to drastically cut memory cost while maintaining SLA—directly applicable to anyone running vector search at scale.
- **[ScoreGate: Adaptive Chunk Selection for Retrieval-Augmented Generation via Dual-Score Statistical Fusion](http://arxiv.org/abs/2606.14269v1)** — Proposes a zero-extra-cost method to dynamically decide how many retrieved chunks to feed the LLM by fusing bi-encoder and cross-encoder scores, solving the pervasive fixed-top-K problem in RAG pipelines.

## RAG Pipeline Optimization: Adaptive Retrieval, Stopping, and Chunk Selection

### [ScoreGate: Adaptive Chunk Selection for Retrieval-Augmented Generation via Dual-Score Statistical Fusion](http://arxiv.org/abs/2606.14269v1)
_Karamvir Singh, Arvind Jain | 2026-06-12 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces ScoreGate, a lightweight inference-time mechanism that uses bi-encoder similarity and cross-encoder reranker scores to dynamically select retrieval cardinality per query. No additional model calls are needed, directly addressing the over/under-retrieval problem of fixed top-K in RAG.

### [TASR: Training-Free Adaptive Stopping for Iterative Retrieval](http://arxiv.org/abs/2606.13814v1)
_Adrian Kieback, Uyiosa Philip Amadasun, Aman Chadha et al. | 2026-06-11 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a simple, training-free stopping rule for iterative RAG agents that halts retrieval when the model repeats its previous answer, eliminating wasteful retrieval calls without requiring labeled stopping trajectories.

### [Tail-Aware Adaptive-k: Query-Adaptive Context Selection for Retrieval-Augmented Generation](http://arxiv.org/abs/2606.11907v1)
_Ziyu Song, Jiaming Fang, Kuangyu Li et al. | 2026-06-10 | arXiv (cs.IR) | ⭐⭐⭐_

Applies Extreme Value Theory locally on the tail of ranked lists to perform training-free adaptive truncation, offering a principled alternative to fixed top-K that handles heavy-tailed similarity distributions common in real queries.

### [CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency](http://arxiv.org/abs/2606.13438v1)
_Yanjia Sun, Sifan Liu, Jie Shao | 2026-06-11 | arXiv (cs.IR) | ⭐⭐⭐_

Addresses RAG brittleness to query reformulation by enforcing cross-query consistency: semantically equivalent queries with different syntax should yield consistent answers, reducing hallucination from misleading retrieved documents.

### [How Fine-Grained Should a RAG Benchmark Be? A Hierarchical Framework for Synthetic Question Generation](http://arxiv.org/abs/2606.12789v1)
_Chase M. Fensore, Kaustubh Dhole, Jason Fan et al. | 2026-06-11 | arXiv (cs.IR) | ⭐⭐_

Presents HieraRAG, a hierarchical framework for constructing RAG benchmarks that identifies the optimal granularity of question variation to maximize discriminative power across RAG configurations. Useful for practitioners building evaluation suites.

### [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](http://arxiv.org/abs/2606.14047v1)
_Ghadir Alselwi, Basem Suleiman, Hao Xue et al. | 2026-06-12 | arXiv (cs.IR) | ⭐⭐_

Augments retrieval with dynamically constructed knowledge graphs during inference, combining semantic similarity with explicit entity relationships for long-context understanding—relevant to RAG systems handling complex, multi-entity documents.

---

## Dense Retrieval, Reranking, and Query Expansion

### [ADORE: Iterative Query Expansion with Retrieval-Grounded Relevance Feedback](http://arxiv.org/abs/2606.13905v1)
_Amin Bigdeli, Negar Arabzadeh, Radin Hamidi Rad et al. | 2026-06-11 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes retrieval-grounded iterative query expansion that checks corpus feedback at each step rather than relying on single-pass LLM generation, reducing retrieval drift and improving expansion quality.

### [CoDeR: Local Constraint-Compatible Retrieval Beyond Semantic Similarity](http://arxiv.org/abs/2606.13204v1)
_Xingkun Yin, Xuebin Tang, Hongyang Du | 2026-06-11 | arXiv (cs.IR) | ⭐⭐⭐_

Identifies how pure semantic similarity fails for constraint-sensitive queries (e.g., negation, exclusion) and proposes a dense retrieval method that disentangles constraint direction from topic similarity—directly useful for improving retrieval precision.

### [CompRank: Efficient LLM Reranking via Token-Level Compression and Decoding-Free Scoring](http://arxiv.org/abs/2606.11700v1)
_Xuan Lu, Haohang Huang, Yingqi Fan et al. | 2026-06-10 | arXiv (cs.IR) | ⭐⭐⭐_

Reduces the cost of LLM-based reranking by compressing document tokens and eliminating autoregressive decoding, making reranking viable for longer candidate lists in production retrieval and RAG pipelines.

### [uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking](http://arxiv.org/abs/2606.11945v1)
_Simon Lupart, Kidist Amde Mekonnen, Zahra Abbasiantaeb et al. | 2026-06-10 | arXiv (cs.IR) | ⭐⭐_

Describes a multi-turn RAG pipeline combining learned sparse retrieval with LLM-based listwise reranking for conversational QA across four domains, providing a practical reference architecture for conversational search.

### [What Limits Does Quantization Place on Dense Top-k Retrieval? A Theoretical Study](http://arxiv.org/abs/2606.11780v1)
_Koki Okajima, Tsukasa Yoshida | 2026-06-10 | arXiv (cs.IR) | ⭐⭐⭐_

Proves that with B-bit quantized embeddings, perfect top-k retrieval requires Bd = Ω(k ln N), meaning finite precision imposes fundamental limits on retrieval correctness—a crucial theoretical result for practitioners using scalar or product quantization.

---

## Vector Search Infrastructure and Indexing at Scale

### [The Clustering Strikes Back: Building Cost-Effective and High-Performance ANNS at Scale with Helmsman](http://arxiv.org/abs/2606.13145v1)
_Yuchen Huang, Baiteng Ma, Yiping Sun et al. | 2026-06-11 | arXiv (cs.IR) | ⭐⭐⭐_

Xiaohongshu's production system replaces expensive in-memory HNSW with an optimized clustering-based ANNS index (Helmsman), dramatically reducing memory and cost while meeting strict SLA requirements for search, recommendation, and ads at scale.

### [MLT-Dedup: Efficient Large-Scale Online Video Deduplication via Multi-Level Representations and Spatial-Temporal Matching](http://arxiv.org/abs/2606.12215v1)
_David Yuchen Wang, Haoying Li, Hailun Xu et al. | 2026-06-10 | arXiv (cs.IR) | ⭐⭐_

Tackles near-duplicate video retrieval at platform scale using multi-level representations and spatial-temporal matching, addressing the index budget vs. recall trade-off relevant to large-scale similarity search infrastructure.

### [FAST-MEL: A Fast, Accurate, and Storage Efficient Solution for Multimodal Entity Linking](http://arxiv.org/abs/2606.11749v1)
_Derrien Thomas, Laurent Amsaleg, Pascale Sévillot | 2026-06-10 | arXiv (cs.IR) | ⭐⭐_

Proposes a multimodal entity linking system optimized for accuracy, speed, and compact KB indexing—relevant to practitioners building multi-modal retrieval systems with storage constraints.

---

## Generative Retrieval and E-Commerce Search

### [OneRetrieval: Unifying Multi-Branch E-commerce Retrieval with an Editable Generative Model](http://arxiv.org/abs/2606.13533v1)
_Xuxin Zhang, Ben Chen, Yue Lv et al. | 2026-06-11 | arXiv (cs.IR) | ⭐⭐_

Proposes collapsing multi-branch e-commerce retrieval (term-match, embedding, etc.) into a single editable generative retrieval model that supports real-time catalog updates—an interesting production-oriented alternative to traditional hybrid retrieval.

### [CORE-Bench: A Comprehensive Benchmark for Code Retrieval in the Era of Agentic Coding](http://arxiv.org/abs/2606.11864v1)
_Fuwei Zhang, Yanzhao Zhang, Mingxin Li et al. | 2026-06-10 | arXiv (cs.IR) | ⭐⭐_

Introduces a repository-level code retrieval benchmark that goes beyond snippet matching to evaluate navigating real codebases—relevant for teams building code search or retrieval-augmented coding agents.

### [Hybrid Neural Retrieval with Generative Query Refinement for Quranic Passage Retrieval](http://arxiv.org/abs/2606.13837v1)
_Mohamed G. Salman, Mohammad E. Moftah, Ali Hamdi | 2026-06-11 | arXiv (cs.IR) | ⭐_

A four-phase neural retrieval architecture using generative query refinement to bridge the semantic gap between modern and classical Arabic, demonstrating hybrid retrieval techniques in a domain-specific setting.

---

## Evaluation, Simulation, and Benchmarking for IR/Rec Systems

### [Verifiable User Simulation for Search and Recommendation Systems](http://arxiv.org/abs/2606.14474v1)
_Chenglong Ma, Xinye Wanyan, Danula Hettiachchi et al. | 2026-06-12 | arXiv (cs.IR) | ⭐⭐_

Addresses the opacity of LLM-based user simulators for evaluating search and RAG pipelines, proposing verifiable simulation that checks consistency with intended user profiles—useful for teams doing offline evaluation of retrieval systems.

### [Charge as a Construct-Validity Factor in Chinese Legal Case Retrieval: A Cross-Benchmark Audit](http://arxiv.org/abs/2606.12993v1)
_Yao Liu, Tien-Ping Tan, Zhilan Liu | 2026-06-11 | arXiv (cs.IR) | ⭐_

Audits Chinese legal retrieval benchmarks and finds that a simple charge-matching heuristic closes 99.2% of the gap to trained models, exposing benchmark design flaws—a cautionary tale for IR benchmark construction.

### [Findings of the MAGMaR 2026 Shared Task](http://arxiv.org/abs/2606.12295v1)
_Alexander Martin, Dengjia Zhang, Joel Brogan et al. | 2026-06-10 | arXiv (cs.IR) | ⭐_

Reports results from a shared task on multimodal retrieval and grounded generation from videos, providing baselines and system comparisons for video retrieval practitioners.

---
