# Research Digest — 2026-W36

## Highlights

- **[Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval](http://arxiv.org/abs/2609.05110v1)** — Directly addresses a critical pain point for vector search practitioners — how to incorporate user feedback and evolving intent into static embedding indexes without full re-indexing.
- **[CAGE: Coherence-Aware Graph Encoding for Retrieval-Augmented Generation](http://arxiv.org/abs/2609.04647v1)** — Tackles the underexplored problem of inter-passage coherence in RAG context assembly, proposing a principled reranking framework that goes beyond per-passage relevance scoring.

## RAG Architecture & Retrieval Strategies

### [CAGE: Coherence-Aware Graph Encoding for Retrieval-Augmented Generation](http://arxiv.org/abs/2609.04647v1)
_Tong Qi, Jingyu Wu, Youbing Yin et al. | 2026-09-04 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces a reranking framework that models between-chunk coherence across four dimensions (relevance, noise resistance, bonding, factual consistency) using directed heterogeneous entity graphs. Addresses a key RAG weakness: individually relevant but collectively incoherent context sets.

### [A Tree-based RAG Framework for Evidence-Intensive QA via Adaptive Planning and Topology-Aware Evidence Gathering](http://arxiv.org/abs/2609.04981v1)
_Songeun Lee, Kyungjin Min, Injae Na et al. | 2026-09-04 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a tree-based reasoning structure for RAG that handles evidence-intensive multi-hop QA by enabling adaptive reasoning expansion and topology-aware evidence integration across hundreds of documents.

### [When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA](http://arxiv.org/abs/2609.03454v1)
_Hyunseo Oh, Chong-Kwon Kim, Yoonhyuk Choi | 2026-09-03 | arXiv (cs.IR) | ⭐⭐_

Studies when RAG helps vs. hurts for mental-health QA and introduces a lightweight selective retrieval policy. Relevant for practitioners designing adaptive retrieval triggers in sensitive domains.

### [Beyond Maintenance Manual Multimodal RAG: Suggesting What Tool](http://arxiv.org/abs/2609.05116v1)
_Seongjun Ha, Md Rashedul Islam | 2026-09-04 | arXiv (cs.IR) | ⭐⭐_

Extends multimodal RAG for aircraft maintenance by augmenting retrieved procedures with tool recommendations, demonstrating a practical vertical RAG application combining text and figure retrieval.

### [Enhancing Financial Question Answering: A Novel Benchmark Dataset of Banks' financial statements](http://arxiv.org/abs/2609.03654v1)
_Arianna Miola, Bruno Spaccavento, Lorenzo Silotto et al. | 2026-09-03 | arXiv (cs.IR) | ⭐⭐_

Introduces FinRAG-QA, a benchmark of 999 questions over 209 bank financial reports, useful for evaluating RAG systems on complex, mixed text-numeric financial documents.

---

## Dense Retrieval, Embeddings & Reranking

### [Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval](http://arxiv.org/abs/2609.05110v1)
_Maddalena Amendola, Antonio Mallia, Raffaele Perego | 2026-09-04 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces a lightweight method for modifying stored document embeddings in-place to adapt dense retrieval to user feedback or evolving search intent, avoiding costly full re-indexing of vector stores.

### [DoPR: Reusable Compressed Document Prefixes for Efficient LLM Reranking](http://arxiv.org/abs/2609.03311v1)
_Beiya Dai, Yifan Wei, Guang Yang et al. | 2026-09-03 | arXiv (cs.IR) | ⭐⭐⭐_

Decouples offline document processing from online LLM reranking by precomputing compressed document prefix states, eliminating redundant computation when the same document appears across queries.

### [CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation](http://arxiv.org/abs/2609.04083v1)
_Tingyu Song, Mingxin Li, Yanzhao Zhang et al. | 2026-09-03 | arXiv (cs.IR) | ⭐⭐⭐_

Distills compositional reasoning from a cross-attentive reranker into a multimodal embedding model using a Rank-KL objective, improving attribute-object binding in compositional retrieval tasks.

### [From Topical Relevance to Answerability: Entailment Distillation for Conversational Retrieval](http://arxiv.org/abs/2609.03482v1)
_Shuai Qin, Guojia An, Weikang Guo et al. | 2026-09-03 | arXiv (cs.IR) | ⭐⭐⭐_

Identifies and addresses the answerability gap in conversational retrieval by distilling answer-passage entailment signals into retrievers, shifting from topical relevance to actual answer support.

### [Comparing Retrieval Methods for Academic Advisor Discovery: A Six-Method Study](http://arxiv.org/abs/2609.03901v1)
_Biraj Subedi | 2026-09-03 | arXiv (cs.IR) | ⭐⭐_

Benchmarks six retrieval methods (Jaccard, TF-IDF, BM25, dense embeddings, hybrid fusion, learning-to-rank) on 768 faculty profiles, providing a practical comparison across sparse and dense approaches.

### [Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings](http://arxiv.org/abs/2609.03376v1)
_Peichun Hua, Yunming Xiao | 2026-09-03 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a cryptographic framework for privacy-preserving dense retrieval on untrusted clouds at million-document scale, directly relevant to organizations outsourcing vector search infrastructure.

### [SAM-D2Q: Aligning Multimodal Doc2Query with Search Demand and Conversion for E-commerce](http://arxiv.org/abs/2609.04961v1)
_Hui Zhou, Jian Hui Ji, Lei Ma et al. | 2026-09-04 | arXiv (cs.IR) | ⭐⭐_

Extends Doc2Query to multimodal e-commerce settings, generating pseudo-queries aligned with search demand and conversion objectives to reduce vocabulary mismatch between user queries and product titles.

---

## Agent Memory & Long-Term Retrieval

### [Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](http://arxiv.org/abs/2609.05339v1)
_Ankit Goyal, Jaideep Ray | 2026-09-04 | arXiv (cs.IR) | ⭐⭐⭐_

Systematically studies how model upgrades affect agent memory stores including RAG chunks and embeddings, revealing that mixed embedding versions break retrieval — a critical concern for production vector search systems.

### [RuleMem: Active Rule Memory for Long-Term Conversational Agents](http://arxiv.org/abs/2609.03915v1)
_Xingyuan Zeng, Zuohan Wu, Quanming Yao et al. | 2026-09-03 | arXiv (cs.IR) | ⭐⭐_

Proposes inducing reusable logical rules from dialogue history to actively guide evidence retrieval and reasoning, moving beyond passive fact storage for long-term conversational agents.

### [AtomRec: Evolving Atomic Memory for Agentic Recommendation](http://arxiv.org/abs/2609.04882v1)
_Peiyu Hu, Weihai Lu, Siying Gu et al. | 2026-09-04 | arXiv (cs.IR) | ⭐⭐_

Introduces fine-grained atomic collaborative memory for agentic recommenders that preserves preference evolution stages and supports interpretable evidence retrieval as user interests change.

### [SciLENS: RL-Driven Autonomous Agents for Scientific Localized Evidence Navigation and Synthesis](http://arxiv.org/abs/2609.03338v1)
_Leqi Zheng, Jinbo Su, Yuying Li et al. | 2026-09-03 | arXiv (cs.IR) | ⭐⭐_

Builds a fully local scientific literature agent indexing ~12M records with dual-tier infrastructure, relevant to practitioners building offline retrieval-driven research synthesis systems.

---

## E-commerce Search & Recommendation

### [Beyond Co-purchase Relation: Evolution of Complementary Recommendations at Allegro](http://arxiv.org/abs/2609.05063v1)
_Aleksandra Osowska-Kurczab, Klaudia Nazarko, Eliška Kosturová et al. | 2026-09-04 | arXiv (cs.IR) | ⭐⭐_

Describes AlleCompanion, a production-scale retrieval framework at Allegro.com that transforms noisy behavioral signals into true complementary product recommendations, with practical lessons for large-scale retrieval systems.

### [Inventory-Grounded Policy-Level Optimization for Training-Free AI Search](http://arxiv.org/abs/2609.04813v1)
_Wei Zhou, Tiandeng Wu, Jiandong Ding et al. | 2026-09-04 | arXiv (cs.IR) | ⭐⭐_

Presents IGPO, a training-free optimization approach for AI search over frequently updated product catalogs, addressing the challenge of dynamic inventory where fixed embeddings and prompts quickly become stale.

### [HypRQ-VAE: Hyperbolic Item Indexing for Long-Tail-Aware Generative Recommender Systems](http://arxiv.org/abs/2609.03369v1)
_Longfeng Wu, Tong Zeng, Giovanni Seni et al. | 2026-09-03 | arXiv (cs.IR) | ⭐⭐_

Uses hyperbolic geometry to create discrete item indices that better capture hierarchical item relationships and reduce hallucinations in generative recommendation, relevant to embedding space design.

---

## Benchmarks, Entity Resolution & Evaluation

### [Corporate-Family Resolution Is Not a String-Matching Problem: A Public Benchmark Stratified by Name Visibility](http://arxiv.org/abs/2609.04269v1)
_Harshit Gupta | 2026-09-02 | arXiv (cs.IR) | ⭐⭐_

Introduces CorpFam, a 54K-pair benchmark for corporate family resolution that goes beyond string matching, relevant to entity linking and deduplication workflows in vector search pipelines.

### [Leveraging Low-Level Symbolic Competences for Unsupervised Grounding in Hallucination Detection](http://arxiv.org/abs/2609.05025v1)
_Renato Vukovic, Hsien-chin Lin, Carel van Niekerk et al. | 2026-09-04 | arXiv (cs.IR) | ⭐_

Investigates using SQL as a symbolic competence for unsupervised hallucination detection in LLMs, tangentially relevant to grounding and factual verification in RAG systems.

### [SHELF: A Synthetic Harness for Multi-Task Bibliographic Benchmarking](http://arxiv.org/abs/2609.03047v1)
_Michael J. Bommarito | 2026-09-02 | arXiv (cs.IR) | ⭐_

Provides a synthetic benchmark generation system for bibliographic tasks, useful for evaluating retrieval and classification methods on library/archive workloads.

---
