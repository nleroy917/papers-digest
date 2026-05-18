# Research Digest — 2026-W20

## Highlights

- **[Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization](http://arxiv.org/abs/2605.16007v1)** — Directly tackles billion-scale vector search performance with 1-bit quantization on new hardware (NPU), highly relevant for anyone building or optimizing vector search infrastructure.
- **[Granite Embedding Multilingual R2 Models](http://arxiv.org/abs/2605.13521v2)** — A new family of multilingual embedding models with 32K context and state-of-the-art retrieval across 200+ languages—critical for anyone deploying dense retrieval or RAG at enterprise scale.

## Vector Search & Embedding Infrastructure

### [Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization](http://arxiv.org/abs/2605.16007v1)
_Fujun He, Chuyue Ye, Huaxiang Cai et al. | 2026-05-15 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a heterogeneous NPU-CPU system for billion-scale vector similarity search using 1-bit RaBitQ quantization. Addresses hardware mismatches when porting CPU/GPU-optimized quantization to NPU architectures, offering significant throughput and efficiency gains.

### [Granite Embedding Multilingual R2 Models](http://arxiv.org/abs/2605.13521v2)
_Parul Awasthy, Aashka Trivedi, Yushu Yang et al. | 2026-05-13 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces encoder-based multilingual embedding models supporting 200+ languages with 32K context windows. Achieves state-of-the-art on multilingual text search, code retrieval, and long-document search benchmarks, directly applicable to vector database deployments.

### [A Picture is Worth a Thousand Words? An Empirical Study of Aggregation Strategies for Visual Financial Document Retrieval](http://arxiv.org/abs/2605.14581v1)
_Ho Hung Lim, Yi Yang | 2026-05-14 | arXiv (cs.IR) | ⭐⭐⭐_

Studies how to aggregate hundreds of vision patch tokens into single vectors for storage in vector databases. Develops a diagnostic benchmark for financial documents to evaluate information loss from single-vector aggregation—directly relevant to visual RAG pipelines.

### [VectorSmuggle: Steganographic Exfiltration in Embedding Stores and a Cryptographic Provenance Defense](http://arxiv.org/abs/2605.13764v1)
_Jascha Wanger | 2026-05-13 | arXiv (cs.IR) | ⭐⭐⭐_

Reveals a novel steganographic attack class on vector databases where adversaries embed hidden data in embeddings. Proposes cryptographic provenance attestation as a defense—important security reading for anyone operating vector stores in production.

### [Think When Needed: Adaptive Reasoning-Driven Multimodal Embeddings with a Dual-LoRA Architecture](http://arxiv.org/abs/2605.14448v1)
_Longxiang Zhang, Weilong Dai, Guanghao Zhang et al. | 2026-05-14 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a Dual-LoRA architecture that adaptively applies chain-of-thought reasoning only for complex inputs when generating multimodal embeddings, reducing inference cost while maintaining retrieval quality for hard queries.

---

## RAG Retrieval Quality & Fairness

### [Fairness-Aware Retrieval Optimization for Retrieval-Augmented Generation](http://arxiv.org/abs/2605.15790v1)
_Yingqi Zhao, Vasilis Efthymiou, Jyrki Nummenmaa et al. | 2026-05-15 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a fairness-aware retrieval framework for RAG that models and controls bias propagation in top-k document retrieval. Combines reranking with position-aware bias modeling—important for practitioners concerned about RAG output fairness.

### [Utility-Oriented Visual Evidence Selection for Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2605.13277v1)
_Weiqing Luo, Zongye Hu, Xiao Wang et al. | 2026-05-13 | arXiv (cs.IR) | ⭐⭐⭐_

Reformulates multimodal evidence selection from an information-theoretic perspective, defining utility as information gain on model output rather than surface similarity. Directly improves evidence selection quality in multimodal RAG systems.

### [Thinking Ahead: Prospection-Guided Retrieval of Memory with Language Models](http://arxiv.org/abs/2605.14177v1)
_Harshita Chopra, Krishna Kant Chintalapudi, Suman Nath et al. | 2026-05-13 | arXiv (cs.IR) | ⭐⭐⭐_

Addresses the limitation that many relevant facts have low semantic similarity to queries in dense retrieval. Proposes prospection-guided retrieval that anticipates future user needs rather than relying solely on embedding similarity—relevant for personalized RAG.

### [RAG-Enhanced Large Language Models for Dynamic Content Expiration Prediction in Web Search](http://arxiv.org/abs/2605.13052v1)
_Tingyu Chen, Wenkai Zhang, Li Gao et al. | 2026-05-13 | arXiv (cs.IR) | ⭐⭐_

Deployed at Baidu, this framework uses RAG-enhanced LLMs to predict content expiration dynamically per query, replacing static time-window filtering. Relevant to practitioners dealing with freshness in retrieval systems.

---

## Reranking & Retrieval Efficiency

### [Stop Overthinking: Unlocking Efficient Listwise Reranking with Minimal Reasoning](http://arxiv.org/abs/2605.14450v1)
_Danyang Liu, Kan Li | 2026-05-14 | arXiv (cs.IR) | ⭐⭐⭐_

Investigates the cost-performance tradeoff of chain-of-thought reasoning in LLM-based listwise reranking. Shows that minimal reasoning can achieve near-SOTA retrieval effectiveness at drastically reduced computational cost—practical for production reranking.

### [Efficient Generative Retrieval for E-commerce Search with Semantic Cluster IDs and Expert-Guided RL](http://arxiv.org/abs/2605.14434v1)
_Jianbo Zhu, Xing Fang, Jing Wang et al. | 2026-05-14 | arXiv (cs.IR) | ⭐⭐_

Proposes a generative retrieval framework for industrial e-commerce using semantic cluster IDs and reinforcement learning. Addresses massive dynamic catalogs and latency requirements, positioning generative retrieval as a recall-stage alternative.

### [Fortress: A Case Study in Stabilizing Search Recommendations via Temporal Data Augmentation and Feature Pruning](http://arxiv.org/abs/2605.15299v1)
_Milind Pandurang Jagre, Jia Huang, Dayvid V. R. Oliveira et al. | 2026-05-14 | arXiv (cs.IR) | ⭐⭐_

Introduces a framework for stabilizing search/recommendation model predictions by pruning temporally volatile features. Relevant to production search systems where prediction consistency across time is critical.

---

## Agentic & Graph-Based RAG Systems

### [Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG](http://arxiv.org/abs/2605.15109v1)
_Riccardo Terrenzi, Maximilian von Zastrow, Serkan Ayvaz | 2026-05-14 | arXiv (cs.IR) | ⭐⭐⭐_

Frames citation faithfulness in GraphRAG as a trajectory-level problem, arguing that citations must account for graph traversal paths and visited-but-uncited entities. Provides a new lens on provenance for knowledge-graph-grounded RAG.

### [Argus: Evidence Assembly for Scalable Deep Research Agents](http://arxiv.org/abs/2605.16217v1)
_Zhen Zhang, Liangcai Su, Zhuo Chen et al. | 2026-05-15 | arXiv (cs.IR) | ⭐⭐_

Addresses evidence duplication in parallel deep research agents by proposing an evidence assembly approach. Relevant to architects of agentic RAG systems that scale inference via parallel search and aggregation.

### [X-SYNTH: Beyond Retrieval -- Enterprise Context Synthesis from Observed Human Attention](http://arxiv.org/abs/2605.15505v1)
_Guruprasad Raghavan, George Nychis, Rohan Narayana Murthy | 2026-05-15 | arXiv (cs.IR) | ⭐⭐_

Proposes moving beyond content-matching retrieval for enterprise AI by synthesizing context from observed human attention patterns across systems. Relevant to enterprise RAG architects facing context scattered across many sources.

### [Falkor-IRAC: Graph-Constrained Generation for Verified Legal Reasoning in Indian Judicial AI](http://arxiv.org/abs/2605.14665v2)
_Joy Bose | 2026-05-14 | arXiv (cs.IR) | ⭐⭐_

Argues that legal reasoning requires graph-constrained generation rather than vector-based RAG, addressing hallucinated precedents and unsupported reasoning chains. Instructive case study on RAG limitations in structured reasoning domains.

### [Towards Self-Evolving Agentic Literature Retrieval](http://arxiv.org/abs/2605.14306v1)
_Yuwen Du, Tian Jin, Jing Kang et al. | 2026-05-14 | arXiv (cs.IR) | ⭐⭐_

Introduces PaSaMaster, a self-evolving agentic system for academic literature retrieval that balances complex intent understanding with source authenticity. Relevant to scientific RAG applications.

---

## Multimodal & Domain-Specific Retrieval

### [MERVIN: A Unified Framework for Multimodal Event Retrieval in Vietnamese News Videos](http://arxiv.org/abs/2605.16120v1)
_Anh-Tai Pham-Nguyen, Tung-Duong Le-Duc, Anh-Duy Le et al. | 2026-05-15 | arXiv (cs.IR) | ⭐⭐_

Presents a multimodal retrieval framework integrating keyframes, transcripts, and summaries for Vietnamese news video search. Uses vision encoders and language embeddings indexed independently—relevant to multimodal vector search practitioners.

### [ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence](http://arxiv.org/abs/2605.13034v1)
_Zhuofan Shi, Peilun Jia, Baoqin Sun et al. | 2026-05-13 | arXiv (cs.IR) | ⭐⭐_

Proposes treating source figures as retrievable evidence in deep research report generation, addressing the underuse of visual content in text-centric RAG systems. Relevant for multimodal RAG pipeline design.

### [LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving](http://arxiv.org/abs/2605.13137v2)
_Guoxiong Gao, Zeming Sun, Jiedong Jiang et al. | 2026-05-13 | arXiv (cs.IR) | ⭐_

A two-mode retrieval system for finding library lemmas needed for Lean 4 theorem proofs. While niche, it demonstrates interesting retrieval challenges around finding complementary rather than individually similar items.

---
