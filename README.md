# RAG-Based Hotel Q&A System

A Retrieval-Augmented Generation (RAG) system that answers natural language queries about hotels using a curated dataset of 39 documents. Combines semantic search over a FAISS vector store with Groq (Llama 3.3 70B) to produce context-grounded responses.

---

## Architecture

```
Raw Documents (data/raw/)
        |
        v
  Preprocessing          -- HTML stripping, mojibake fixes, boilerplate removal
        |
        v
   Chunking              -- RecursiveCharacterTextSplitter (512 chars, 64 overlap)
        |
        v
   Embeddings            -- all-MiniLM-L6-v2 (384-dim dense vectors)
        |
        v
  FAISS Index            -- Flat L2 index, top-5 retrieval
        |
        v
  LLM Generation         -- Groq / Llama-3.3-70B, temperature=0, context-only prompt
        |
        v
     Answer
```

**Chunking rationale:** `RecursiveCharacterTextSplitter` splits on paragraph and sentence boundaries before falling back to character cuts, preserving semantic units in hotel descriptions and policies. Chunk size 512 keeps individual amenity/policy facts self-contained; 64-char overlap prevents context loss at boundaries.

**Embedding model:** `all-MiniLM-L6-v2` is a lightweight sentence-transformer (22M params) that produces 384-dim vectors suitable for semantic similarity. Chosen for zero-cost local inference and strong performance on short factual passages.

**Top-k = 5:** Balances recall (enough context for multi-hotel queries) against context window efficiency and retrieval noise.

---

## Dataset

39 synthetic documents across 5 categories covering 8 hotel properties:

| Category          | Count |
|-------------------|-------|
| Hotel Descriptions | 8    |
| Amenities          | 7    |
| Guest Reviews      | 10   |
| Policies           | 7    |
| Location Details   | 7    |

Hotels: Burj Al Arab, The Ritz London, Marina Bay Sands, Waldorf Astoria New York, The Peninsula Hong Kong, Hotel del Coronado, Atlantis Paradise Island, One&Only Royal Mirage.

Dataset is synthetic and generated for assessment purposes.

---

## Tools & Libraries

| Library | Purpose |
|---|---|
| `langchain-groq` | Groq LLM integration (Llama 3.3 70B) |
| `langchain-huggingface` | HuggingFace embeddings wrapper |
| `langchain-community` | FAISS vector store wrapper |
| `langchain-core` | LCEL chain primitives |
| `langchain-text-splitters` | Document chunking |
| `faiss-cpu` | Vector similarity search |
| `sentence-transformers` | `all-MiniLM-L6-v2` embeddings |
| `python-dotenv` | API key loading from `.env` |

---

## Setup

**1. Clone and install dependencies**

```bash
git clone <repo-url>
cd staychatrag
pip install -r requirements.txt
```

**2. Set your Groq API key**

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

A free API key can be obtained from [console.groq.com](https://console.groq.com).

**3. Run the notebook**

Open `rag.ipynb` in Jupyter and run cells sequentially. The notebook is self-contained — it preprocesses documents, builds the FAISS index, and runs all evaluation queries in order.

Pre-run cell outputs are included; do not clear before reviewing.

---

## Known Limitations

- **Lexical mismatch:** The embedding model handles synonym matching at retrieval, but the LLM can fail when query terms differ from document vocabulary (e.g., "free WiFi" vs "complimentary WiFi"). Mitigated by using a context-grounded rather than strictly context-only prompt.
- **Generation faithfulness:** The LLM occasionally ignores top-ranked retrieved chunks in favour of lower-ranked ones — a known "lost in the middle" behaviour with long contexts at temperature=0. Partially addressed by adding an explicit "mention ALL matching hotels" instruction.
- **Single-hotel policy queries:** The dataset has one policy document per hotel. Queries naming a hotel not in the dataset (e.g., "Hotel X") return no answer since no relevant chunks are retrieved.
- **Dataset coverage:** 39 documents covering 8 properties. Queries requiring cross-property comparison or fine-grained detail (room rates, exact dimensions, staff names) are outside the dataset scope.
- **No persistent index:** The FAISS index is rebuilt on each notebook run. For production use, `vectorstore.save_local()` / `FAISS.load_local()` should be used.
