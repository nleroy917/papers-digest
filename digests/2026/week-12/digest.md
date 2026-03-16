# Research Digest — 2026-W11

## Highlights

- **[A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](http://arxiv.org/abs/2603.09933v2)** — Provides a mathematically grounded framework for reducing ColBERT index size via token pruning—directly actionable for anyone operating large-scale late-interaction vector indexes.
- **[Test-Time Strategies for More Efficient and Accurate Agentic RAG](http://arxiv.org/abs/2603.12396v1)** — Tackles the core practical pain points of agentic RAG (redundant retrieval, context bloat) with concrete test-time strategies that can be applied to existing pipelines immediately.

## RAG Systems & Retrieval-Augmented Pipelines

### [Test-Time Strategies for More Efficient and Accurate Agentic RAG](http://arxiv.org/abs/2603.12396v1)
_Brian Zhang, Deepti Guntur, Zhiyang Zuo et al. | 2026-03-12 | arXiv (cs.IR) | ⭐⭐⭐_

Identifies inefficiencies in iterative agentic RAG such as redundant retrieval and poor context management. Proposes test-time strategies to reduce unnecessary retrieval steps while improving answer accuracy on multi-hop questions.

### [Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track](http://arxiv.org/abs/2603.09891v1)
_Shivani Upadhyay, Nandan Thakur, Ronak Pradeep et al. | 2026-03-10 | arXiv (cs.IR) | ⭐⭐⭐_

Summarizes the second TREC RAG Track, introducing long narrative queries to stress-test retrieval+generation pipelines. Provides benchmark insights and design patterns directly relevant to production RAG system builders.

### [RAGPerf: An End-to-End Benchmarking Framework for Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2603.10765v1)
_Shaobo Li, Yirui Zhou, Yuan Xu et al. | 2026-03-11 | arXiv (cs.IR) | ⭐⭐⭐_

Decouples the RAG pipeline into embedding, indexing, retrieval, reranking, and generation stages for fine-grained profiling. Enables practitioners to identify bottlenecks and tune each component independently.

### [Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval](http://arxiv.org/abs/2603.10700v1)
_Andrea Volpini, Elie Raad, Beatrice Gamba et al. | 2026-03-11 | arXiv (cs.IR) | ⭐⭐⭐_

Tests whether Schema.org markup and knowledge-graph structure improve retrieval accuracy over flat-text RAG across four domains. Demonstrates that structured metadata layers boost both retrieval precision and answer quality in agentic settings.

### [MDER-DR: Multi-Hop Question Answering with Entity-Centric Summaries](http://arxiv.org/abs/2603.11223v1)
_Riccardo Campi, Nicolò Oreste Pinciroli Vago, Mathyas Giudici et al. | 2026-03-11 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a KG-based indexing approach that converts triples into entity-centric summaries to preserve contextual nuance. Targets the core multi-hop retrieval problem where standard chunking loses relational information.

### [MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](http://arxiv.org/abs/2603.09800v1)
_Abhishikth Mallampalli, Sridhara Dasu | 2026-03-10 | arXiv (cs.IR) | ⭐⭐_

Describes a domain-specific RAG system for navigating CMS/CERN internal documentation. Provides a practical case study of deploying RAG over large specialized corpora.

### [A Hybrid Knowledge-Grounded Framework for Safety and Traceability in Prescription Verification](http://arxiv.org/abs/2603.10891v1)
_Yichi Zhu, Kan Ling, Xu Liu et al. | 2026-03-11 | arXiv (cs.IR) | ⭐⭐_

Presents PharmGraph-Auditor, a graph-grounded RAG system for prescription auditing that emphasizes traceability and factual grounding. Illustrates how structured retrieval can address LLM hallucination in safety-critical domains.

---

## Vector Index Efficiency & Document Retrieval

### [A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](http://arxiv.org/abs/2603.09933v2)
_Yash Kankanampati, Yuxuan Zong, Nadi Tomeh et al. | 2026-03-10 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces a geometrically grounded Voronoi-cell framework to identify and prune low-importance token embeddings in ColBERT-style indexes. Directly reduces storage overhead while maintaining retrieval quality—critical for large-scale vector search deployments.

### [NanoVDR: Distilling a 2B Vision-Language Retriever into a 70M Text-Only Encoder for Visual Document Retrieval](http://arxiv.org/abs/2603.12824v1)
_Zhuchenyang Liu, Yao Zhang, Yu Xiao | 2026-03-13 | arXiv (cs.IR) | ⭐⭐⭐_

Exploits query-document asymmetry to distill a 2B VLM retriever into a 70M text-only query encoder, slashing latency and GPU requirements. Highly relevant for teams building visual document search with vector databases.

### [Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation](http://arxiv.org/abs/2603.13017v1)
_Sydney Lewis | 2026-03-13 | arXiv (cs.IR) | ⭐⭐⭐_

Compresses conversational history into structured compound objects achieving 11x token reduction while preserving retrieval quality. Directly applicable to memory layers in vector-search-backed agent systems.

---

## LLM Knowledge, Reranking & Fairness in IR

### [Does Reasoning Make Search More Fair? Comparing Fairness in Reasoning and Non-Reasoning Rerankers](http://arxiv.org/abs/2603.10332v1)
_Saron Samuel, Benjamin Van Durme, Eugene Yang | 2026-03-11 | arXiv (cs.IR) | ⭐⭐⭐_

First systematic fairness comparison of reasoning rerankers (e.g., Rank1) vs. traditional rerankers using TREC Fair Ranking data. Finds reasoning neither helps nor hurts fairness—important for practitioners evaluating reranking pipelines.

### [Understanding the Interplay between LLMs' Utilisation of Parametric and Contextual Knowledge](http://arxiv.org/abs/2603.09654v1)
_Isabelle Augenstein | 2026-03-10 | arXiv (cs.IR) | ⭐⭐_

ECIR 2025 keynote examining how LLMs balance parametric vs. retrieved contextual knowledge. Provides theoretical grounding for understanding when RAG retrieval actually influences LLM outputs.

### [PRECEPT: Planning Resilience via Experience, Context Engineering & Probing Trajectories](http://arxiv.org/abs/2603.09641v1)
_Arash Shahmansoori | 2026-03-10 | arXiv (cs.IR) | ⭐⭐_

Introduces a structured rule retrieval system with exact-match keys and conflict-aware memory for LLM agents. Relevant to practitioners designing hybrid retrieval strategies that combine structured and vector-based lookup.

---

## Memory & Retrieval for Conversational Agents

### [TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA](http://arxiv.org/abs/2603.09297v1)
_Mengwei Yuan, Jianan Liu, Jing Yang et al. | 2026-03-10 | arXiv (cs.IR) | ⭐⭐⭐_

Moves beyond static top-k embedding retrieval for long-term memory by introducing tool-augmented autonomous retrieval. Directly addresses limitations of naive vector similarity search in conversational agent memory.

### [Fine-grained Motion Retrieval via Joint-Angle Motion Images and Token-Patch Late Interaction](http://arxiv.org/abs/2603.09930v1)
_Yao Zhang, Zhuchenyang Liu, Yanlan He et al. | 2026-03-10 | arXiv (cs.IR) | ⭐⭐_

Applies late-interaction retrieval (ColBERT-style) to text-motion cross-modal search, converting 3D skeleton sequences to images for token-patch matching. Demonstrates late-interaction's versatility beyond text retrieval.

---

## Multimodal & LLM-Based Recommendation Systems

### [Anchored Alignment: Preventing Positional Collapse in Multimodal Recommender Systems](http://arxiv.org/abs/2603.12726v1)
_Yonghun Jeong, David Yoon Suk Kang, Yeon-Chang Lee | 2026-03-13 | arXiv (cs.IR) | ⭐⭐_

Proposes anchor-based alignment in a projection domain to prevent modality collapse in multimodal embedding spaces. Relevant to practitioners fusing image/text embeddings in vector databases for recommendations.

### [VLM4Rec: Multimodal Semantic Representation for Recommendation with Large Vision-Language Models](http://arxiv.org/abs/2603.12625v1)
_Ty Valencia, Burak Barlas, Varun Singhal et al. | 2026-03-13 | arXiv (cs.IR) | ⭐⭐_

Studies whether aligning visual features to a preference-aware semantic space improves multimodal recommendations over naive feature fusion. Relevant to embedding space design for recommendation-oriented vector stores.

### [RecThinker: An Agentic Framework for Tool-Augmented Reasoning in Recommendation](http://arxiv.org/abs/2603.09843v1)
_Haobo Zhang, Yutao Zhu, Kelong Mao et al. | 2026-03-10 | arXiv (cs.IR) | ⭐_

Introduces an agentic recommendation framework where LLMs actively acquire information via tools rather than relying on static profiles. More recommendation-focused than retrieval-focused.

---
