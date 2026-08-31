# Research Digest — 2026-W35

## Highlights

- **[A Versioned Unified Graph Index for Dynamic Timestamp-Aware Nearest Neighbor Search](http://arxiv.org/abs/2608.27663v1)** — TiGER directly addresses a critical production need — time-filtered ANN search on continuously updated vector datasets — with a novel unified graph structure that avoids traversing invalid vectors, making it essential reading for anyone building temporal vector indices.
- **[PUMA: Post-Hoc Sparsification of Universal Multimodal Embeddings for Efficient Retrieval](http://arxiv.org/abs/2608.25780v1)** — PUMA offers a practical, backbone-agnostic sparse autoencoder recipe that dramatically reduces memory and inference costs for multimodal dense retrieval without retraining, directly relevant to anyone operating large-scale vector search systems.

## Vector Index Structures & Efficient ANN Search

### [A Versioned Unified Graph Index for Dynamic Timestamp-Aware Nearest Neighbor Search](http://arxiv.org/abs/2608.27663v1)
_Jun Woo Chung, Weijie Zhao | 2026-08-27 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces TiGER, a unified graph index with integrated versioned connectivity for time-aware ANN search on dynamic datasets. Supports arbitrary time-range queries without traversing invalid vectors, addressing a key gap in production vector databases.

### [misi: a Metric Inverted Sample Index](http://arxiv.org/abs/2608.27422v1)
_Edgar Chavez | 2026-08-27 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes an inverted index for approximate nearest-neighbor search over general metric spaces using a random database sample as vocabulary with IDF-weighted voting. Generalizes NAPP to linear-size vocabularies, offering a lightweight alternative ANN approach.

### [PUMA: Post-Hoc Sparsification of Universal Multimodal Embeddings for Efficient Retrieval](http://arxiv.org/abs/2608.25780v1)
_Matteo Attimonelli, Alessandro De Bellis, Franco Maria Nardini et al. | 2026-08-26 | arXiv (cs.IR) | ⭐⭐⭐_

Introduces a sparse autoencoder that converts dense multimodal embeddings into compact sparse codes post-hoc without backbone retraining. Reduces memory and compute costs while preserving retrieval quality, directly applicable to production vector search.

### [Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval at Scale](http://arxiv.org/abs/2608.25735v1)
_Peichun Hua, Danyang Chen, Junan Zhang et al. | 2026-08-26 | arXiv (cs.IR) | ⭐⭐⭐_

Repurposes learned deep hashing as a private filter for hosted dense retrieval, balancing query privacy with efficiency. Addresses a real production concern for hosted RAG and semantic search services operating over sensitive corpora.

---

## RAG Systems & Retrieval-Augmented Generation

### [PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise Visual Document RAG](http://arxiv.org/abs/2608.28572v1)
_Benjamin Constable, Anup Roy, Vishal Sharma et al. | 2026-08-28 | arXiv (cs.IR) | ⭐⭐⭐_

Describes a production vision-first RAG system using a ColPali-style backbone with pooled two-stage late interaction for enterprise document retrieval. Demonstrates how to index visually dense documents at scale without costly OCR pipelines.

### [LINE Conversation History Retrieval for Personal Memory RAG](http://arxiv.org/abs/2608.27809v1)
_Akito Hattori | 2026-08-28 | arXiv (cs.IR) | ⭐⭐_

Evaluates BM25, dense vector, and hybrid retrieval approaches on personal chat history for RAG, comparing raw text, summaries, and composite embedding representations. Provides practical insights on chunking strategies and hybrid search for conversational data.

### [Assessing the Downstream Utility of Evidence-Aware Retrieval in RAG](http://arxiv.org/abs/2608.26379v1)
_Utshab Kumar Ghosh, Debayan Mukhopadhyay, Shubham Chatterjee | 2026-08-26 | arXiv (cs.IR) | ⭐⭐⭐_

Studies whether evidence-aware retrieval metrics (beyond topical relevance) better predict downstream RAG generation quality across five benchmarks. Provides actionable guidance on retrieval evaluation strategies for RAG pipeline builders.

### [PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans](http://arxiv.org/abs/2608.26091v1)
_Nabaraj Subedi, Shuvo Dip Datta, Ahmed Abdelaty et al. | 2026-08-26 | arXiv (cs.IR) | ⭐⭐_

Presents a visual-first multimodal RAG framework for civil engineering plans using ColNomic-3B multi-vector retrieval and MaxSim heatmaps. Shows how late-interaction retrieval can be applied to domain-specific visual document understanding.

### [hoBIT: A Profile-Aware Retrieval-Augmented Chatbot for University Academic Advising](http://arxiv.org/abs/2608.26604v1)
_Yoonseo Kim, Seongmin Lee, Joongheon Kim et al. | 2026-08-27 | arXiv (cs.IR) | ⭐⭐_

Demonstrates a profile-aware RAG system that progressively acquires user context to filter and retrieve the most applicable documents. Highlights practical challenges in personalized retrieval where the same query needs different evidence depending on user attributes.

---

## Hybrid & Agentic Retrieval Methods

### [ProRetrieval: Learning to Orchestrate Hybrid Search via Executable Program Synthesis](http://arxiv.org/abs/2608.27017v2)
_Chengsong You, Zhen Sun, Yunhai Hu et al. | 2026-08-27 | arXiv (cs.IR) | ⭐⭐⭐_

Recasts hybrid retrieval orchestration as executable program synthesis, allowing an LLM to compose structured constraints with semantic search via arbitrary Boolean logic. Goes beyond fixed fusion strategies like RRF to dynamically plan retrieval paths.

### [ITER: Interaction-Aware Retrieval for Agentic Search](http://arxiv.org/abs/2608.27912v1)
_Haodong Chen, Shuai Wang, Yu Yin et al. | 2026-08-28 | arXiv (cs.IR) | ⭐⭐⭐_

Proposes a dense retriever that incorporates accumulated context from prior agent search interactions to improve multi-step retrieval. Directly addresses the growing need for retrieval models that work within agentic, iterative search workflows.

### [Conversational Recommendation over Live E-Commerce Catalogues with Self-Refreshing Retrieval](http://arxiv.org/abs/2608.27006v1)
_Ante Kapetanovic, Tomislav Duricic, Dionizije Fa et al. | 2026-08-27 | arXiv (cs.IR) | ⭐⭐_

Presents a self-refreshing retriever that continuously syncs with live product feeds for conversational recommendation. Demonstrates practical vector index maintenance patterns for rapidly changing catalogs.

---

## Retrieval Evaluation & Ranking

### [Equal Ranking Quality, Different Decisions: Training Order-Consistent LLM Scorers](http://arxiv.org/abs/2608.26762v1)
_Markus Frohmann, Mahdiyar Alavi, Elizabeth Lingg et al. | 2026-08-27 | arXiv (cs.IR) | ⭐⭐⭐_

Reveals that LLM-based rerankers with similar nDCG scores can make very different threshold and selection decisions due to input order sensitivity. Proposes training strategies for order consistency, important for anyone using LLM rerankers in production.

### [NormasTCU --- A Brazilian Portuguese IR Dataset and an Evaluation of LLM-as-a-Judge for Relevance Assessment](http://arxiv.org/abs/2608.27746v1)
_Leandro Carísio Fernandes, Marcus Vinícius Borela de Castro, Leandro dos Santos Ribeiro et al. | 2026-08-27 | arXiv (cs.IR) | ⭐⭐_

Introduces a Portuguese legal IR benchmark and evaluates LLM-as-a-judge for relevance assessment in non-English specialized domains. Valuable for practitioners building IR evaluation pipelines for low-resource languages.

### [PailitaoGR: Latent Think-with-Images for Generative Image Retrieval](http://arxiv.org/abs/2608.26658v1)
_Xiaomeng Fan, Yueran Liu, Shengyu Zhou et al. | 2026-08-27 | arXiv (cs.IR) | ⭐⭐_

Extends generative retrieval to image search by having the model reason over visual content to generate product semantic identifiers. Represents an emerging alternative to embedding-based image retrieval for e-commerce.

---

## Multimodal & Content-Based Retrieval

### [Every Article Deserves a Video: Contextual Video Matching for Digital Publishers](http://arxiv.org/abs/2608.28359v1)
_Arnaud Corone, Brice Pierre de la Briere, Gladys Roch et al. | 2026-08-28 | arXiv (cs.IR) | ⭐⭐_

Presents a production system for automatically matching videos to text articles using semantic matching across large catalogs. Demonstrates practical cross-modal retrieval at publisher scale.

### [Information-Guided Selective Modality-Interest Alignment for Multimodal Recommendation](http://arxiv.org/abs/2608.27950v1)
_Wenze Ma, Chenyu Sun, Yanmin Zhu et al. | 2026-08-28 | arXiv (cs.IR) | ⭐⭐_

Proposes selective alignment of modality signals with user interests rather than naively fusing all modalities. Relevant to practitioners building multimodal embedding pipelines where not all signals contribute equally to retrieval quality.

### [QUEST: A Query and Extraction System for Topics in Asylum Law Application Decisions](http://arxiv.org/abs/2608.28555v1)
_Maria Vlachou, Anna Murphy Høgenhaug, Mohammad N. S. Jahromi et al. | 2026-08-28 | arXiv (cs.IR) | ⭐_

Builds a topic extraction and retrieval system for complex legal asylum documents. While domain-specific, demonstrates retrieval over heterogeneous long-document collections.

---
