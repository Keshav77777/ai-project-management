# Module 06 – Retrieval-Augmented Generation (RAG)

## Objective

In this module, we begin transforming the AI Project Management application into an AI-powered knowledge assistant by integrating Retrieval-Augmented Generation (RAG).

The goal is to allow the Project Manager Agent to answer questions using uploaded project documents instead of relying solely on the LLM's general knowledge.

---

# Learning Objectives

By the end of this module you will understand:

- What RAG is
- Document loading
- Text chunking
- Embeddings
- Vector databases
- Similarity search
- Retrieval
- Context injection
- Google Gemini Embeddings
- ChromaDB

---

# Architecture

```
                User
                  │
                  ▼
        Project Manager Agent
                  │
                  ▼
          Knowledge Agent
                  │
                  ▼
            RAG Service
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
Document Loader Text Splitter Embedding Service
                  │
                  ▼
             Vector Store
                  │
                  ▼
              ChromaDB
                  │
                  ▼
              Retriever
                  │
                  ▼
                Gemini
                  │
                  ▼
               Final Answer
```

---

# Project Structure

```
project_management_agent/

agents/
    knowledge_agent.py

knowledge/
    uploads/
    chroma_db/

rag/
    __init__.py
    document_loader.py
    text_splitter.py
    embedding_service.py
    vector_store.py
    retriever.py

services/
    rag_service.py

tools/
    upload_document.py
    ask_document.py
```

---

# Dependencies

Install:

```bash
pip install chromadb
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install pypdf
pip install google-genai
```

Add to `requirements.txt`

```
chromadb
langchain
langchain-community
langchain-text-splitters
pypdf
google-genai
```

---

# Part 1 – Document Loader ✅

## Purpose

Read documents from disk and convert them into LangChain `Document` objects.

Current implementation:

```
PDF
    │
    ▼
PyPDFLoader
    │
    ▼
Document Objects
```

Each document contains:

- page_content
- metadata

Example metadata:

```
{
    "page": 0,
    "source": "sample.pdf"
}
```

### Why use LangChain?

Instead of returning a single string, it returns structured `Document` objects that preserve metadata such as page number and source, making downstream chunking and retrieval much easier.

---

# Part 2 – Text Splitter ✅

Purpose:

Split large documents into smaller chunks before generating embeddings.

Implementation:

```
RecursiveCharacterTextSplitter
```

Configuration:

```python
chunk_size = 500
chunk_overlap = 100
```

Why chunk?

Instead of embedding an entire PDF:

```
Entire PDF
      │
      ▼
Huge embedding ❌
```

We create:

```
Chunk 1
Chunk 2
Chunk 3
```

Each chunk receives its own embedding.

### Why overlap?

Without overlap:

```
Authentication uses OAuth

------------------------

2.0 with JWT...
```

The sentence is broken.

With overlap:

```
Chunk 1
Authentication uses OAuth...

Chunk 2
...uses OAuth 2.0...
```

The context is preserved.

---

# Part 3 – Embedding Service ✅

Model used:

```
gemini-embedding-001
```

Purpose:

Convert text into a numerical vector.

Pipeline:

```
Text
    │
    ▼
Embedding Service
    │
    ▼
3072-dimensional vector
```

Example output:

```
<class 'list'>

3072

[-0.02623944,
 -0.004676714,
 ...]
```

### Why not use @staticmethod?

The embedding service maintains state:

- Gemini Client
- Model Name

Creating the client once is more efficient than recreating it for every request.

---

# Part 4 – Vector Store (In Progress)

Purpose:

Store embeddings inside ChromaDB.

Pipeline:

```
Chunk
    │
    ▼
Embedding
    │
    ▼
ChromaDB
```

Responsibilities:

- Connect to ChromaDB
- Create collection
- Store embeddings
- Retrieve embeddings

Current methods:

- `__init__()`
- `add_documents()`
- `search()`

---

# Understanding top_k

Search works like this:

```
Question
    │
    ▼
Embedding
    │
    ▼
Similarity Search
    │
    ▼
Top K Results
```

Example:

Database contains

```
Authentication
JWT
Database
AWS
Docker
```

Question:

```
How do users authenticate?
```

Similarity ranking:

```
Authentication
JWT
Database
AWS
Docker
```

If

```python
top_k = 3
```

The retriever returns only the three most relevant chunks.

---

# Progress

Completed

- ✅ Project Structure
- ✅ Dependencies
- ✅ Document Loader
- ✅ Text Splitter
- ✅ Embedding Service

In Progress

- 🚧 Vector Store

Upcoming

- Retriever
- RagService
- Knowledge Agent
- upload_document Tool
- ask_document Tool
- ADK Integration

---

# Current RAG Pipeline

```
PDF
 │
 ▼
Document Loader
 │
 ▼
Document Objects
 │
 ▼
Text Splitter
 │
 ▼
Chunks
 │
 ▼
Embedding Service
 │
 ▼
Embeddings
 │
 ▼
Vector Store
 │
 ▼
ChromaDB
 │
 ▼
Retriever
 │
 ▼
Gemini
 │
 ▼
Answer
```

---

# Next Session Plan

We will complete:

1. Finish `VectorStore`
2. Store embeddings in ChromaDB
3. Query ChromaDB
4. Build `Retriever`
5. Build `RagService`
6. Integrate with `KnowledgeAgent`
7. Add ADK tools:
   - `upload_document`
   - `ask_document`

At the end of Module 06, the AI Project Manager will be able to answer questions directly from uploaded project documents using a complete Retrieval-Augmented Generation (RAG) pipeline.