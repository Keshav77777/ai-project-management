# Module 06 – Retrieval-Augmented Generation (RAG)

## Overview

In this module, the AI Project Management application was enhanced with **Retrieval-Augmented Generation (RAG)** capabilities. Instead of relying solely on the Large Language Model's general knowledge, the application can now answer questions using uploaded project documents.

A dedicated **Knowledge Agent** was introduced to manage document indexing and document question answering. Uploaded PDF documents are processed, converted into vector embeddings, stored in **ChromaDB**, and later retrieved using semantic similarity search. The retrieved context is injected into Gemini to generate grounded and context-aware responses.

This module transforms the application from a standard AI assistant into an intelligent project knowledge base capable of understanding project documentation.

---

# Module Objectives

By the end of this module, the application can:

- Upload PDF documents
- Split documents into semantic chunks
- Generate embeddings using Gemini
- Store embeddings in ChromaDB
- Retrieve relevant document chunks
- Answer questions using Retrieval-Augmented Generation (RAG)
- Delegate document-related tasks to a dedicated Knowledge Agent

---

# Learning Objectives

During this module, the following concepts were explored:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Document Loading
- Text Chunking
- Embeddings
- Google Gemini Embedding API
- Vector Databases
- ChromaDB
- Similarity Search
- Context Injection
- Prompt Engineering
- Google ADK Multi-Agent Architecture
- Tool Calling

---

# High-Level Architecture

```text
                    User
                      │
                      ▼
            Project Manager Agent
                      │
                      ▼
             Knowledge Agent
        ┌─────────────┴─────────────┐
        ▼                           ▼
 upload_document              ask_document
        │                           │
        └─────────────┬─────────────┘
                      ▼
                 RagService
        ┌─────────────┼──────────────┐
        ▼             ▼              ▼
Document Loader  Text Splitter  Retriever
        │             │              │
        ▼             ▼              ▼
    Documents       Chunks      Query Embedding
                      │              │
                      ▼              ▼
              Embedding Service
                      │
                      ▼
                 Vector Store
                      │
                      ▼
                  ChromaDB
                      │
                      ▼
               Retrieved Context
                      │
                      ▼
                 LLM Service
                      │
                      ▼
               Gemini 2.5 Flash
                      │
                      ▼
                 Final Response
```

---

# Project Structure

```text
project_management_agent/

agents/
│
├── knowledge_agent.py
├── planning_agent.py
├── project_manager.py
└── risk_agent.py

knowledge/
│
├── uploads/
└── chroma_db/

rag/
│
├── document_loader.py
├── text_splitter.py
├── embedding_service.py
├── vector_store.py
├── retriever.py
└── llm_service.py

services/
└── rag_service.py

tools/
├── upload_document.py
└── ask_document.py

prompts/
└── knowledge_prompt.py
```

---

# Dependencies

Install the required packages:

```bash
pip install chromadb
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install google-genai
pip install pypdf
```

requirements.txt

```text
chromadb
langchain
langchain-community
langchain-text-splitters
google-genai
pypdf
```

---

# End-to-End RAG Workflow

## Document Indexing Pipeline

```text
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
```

---

## Question Answering Pipeline

```text
User Question
 │
 ▼
Retriever
 │
 ▼
Generate Query Embedding
 │
 ▼
Similarity Search
 │
 ▼
Top-K Chunks
 │
 ▼
LLM Service
 │
 ▼
Gemini
 │
 ▼
Final Answer
```

---

# Part 1 – Document Loader ✅

## Purpose

The Document Loader is responsible for reading PDF documents from disk and converting them into LangChain `Document` objects.

Pipeline

```text
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

Example:

```python
{
    "page": 0,
    "source": "sample.pdf"
}
```

### Why LangChain Documents?

Instead of returning plain text, LangChain preserves metadata such as page number and source, making chunking and retrieval significantly easier.

---

# Part 2 – Text Splitter ✅

## Purpose

Large documents are split into overlapping chunks before generating embeddings.

Implementation

```python
RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
```

Pipeline

```text
Large Document
        │
        ▼
Chunk 1

Chunk 2

Chunk 3
```

### Why Chunk Documents?

Embedding an entire document produces poor retrieval quality.

Smaller chunks improve:

- Semantic search
- Retrieval accuracy
- Context quality

### Why Overlap?

Without overlap:

```text
Authentication uses OAuth

----------------------

2.0 with JWT
```

Context is broken.

With overlap:

```text
Chunk 1

Authentication uses OAuth...

Chunk 2

...uses OAuth 2.0...
```

Important context is preserved.

---

# Part 3 – Embedding Service ✅

Model Used

```
gemini-embedding-001
```

Purpose

Convert text into numerical vectors.

Pipeline

```text
Text
 │
 ▼
Embedding API
 │
 ▼
3072-dimensional Vector
```

Responsibilities

- Create Gemini client
- Generate embeddings
- Return vector representation

Why not use `@staticmethod`?

The service maintains:

- Gemini Client
- Model Name

Creating the client once improves efficiency.

---

# Part 4 – Vector Store ✅

Purpose

Persist embeddings inside ChromaDB.

Pipeline

```text
Chunk
 │
 ▼
Embedding
 │
 ▼
ChromaDB
```

Responsibilities

- Create collection
- Store embeddings
- Store metadata
- Similarity search

Methods

- add_documents()
- search()

---

# Understanding Top-K Retrieval

Suppose ChromaDB contains:

```text
Authentication
JWT
Database
Docker
AWS
```

Question:

```
How do users authenticate?
```

Similarity ranking:

```text
Authentication
JWT
Database
Docker
AWS
```

If

```python
top_k = 3
```

Retriever returns

```text
Authentication
JWT
Database
```

Only the most relevant chunks are sent to Gemini.

---

# Part 5 – Retriever ✅

Purpose

Retrieve the most relevant document chunks for a user question.

Pipeline

```text
Question
 │
 ▼
Embedding Service
 │
 ▼
Query Embedding
 │
 ▼
Vector Store
 │
 ▼
Top-K Chunks
```

Responsibilities

- Generate question embedding
- Perform similarity search
- Return relevant document chunks

---

# Part 6 – LLM Service ✅

Purpose

Generate grounded responses using retrieved context.

Pipeline

```text
Question
 │
 ▼
Retrieved Context
 │
 ▼
Prompt
 │
 ▼
Gemini 2.5 Flash
 │
 ▼
Answer
```

Responsibilities

- Combine retrieved context
- Build prompt
- Call Gemini
- Return answer

---

# Part 7 – RagService ✅

The RagService orchestrates the complete RAG pipeline.

## Document Indexing

- Load PDF
- Split document
- Generate embeddings
- Store embeddings in ChromaDB

## Question Answering

- Retrieve relevant chunks
- Generate context
- Produce grounded answer using Gemini

---

# Part 8 – Knowledge Agent ✅

A dedicated specialist agent responsible for document understanding.

Responsibilities

- Upload documents
- Index documents
- Search documents
- Answer document questions

Available Tools

- upload_document
- ask_document

---

# Part 9 – ADK Tool Integration ✅

## upload_document

Indexes uploaded PDFs.

Pipeline

```text
PDF
 │
 ▼
Document Loader
 │
 ▼
Chunking
 │
 ▼
Embeddings
 │
 ▼
ChromaDB
```

---

## ask_document

Answers questions using RAG.

Pipeline

```text
Question
 │
 ▼
Retriever
 │
 ▼
Context
 │
 ▼
Gemini
 │
 ▼
Answer
```

---

# Agent Delegation

| Request | Handler |
|----------|---------|
| CRUD Operations | Project Manager Tools |
| Planning | Planning Agent |
| Risk Analysis | Risk Agent |
| Upload Document | Knowledge Agent |
| Ask Document Questions | Knowledge Agent |

---

# Testing

## Document Loader

- [x] Load PDF
- [x] Verify metadata

## Text Splitter

- [x] Generate chunks
- [x] Verify overlap

## Embedding Service

- [x] Generate embeddings
- [x] Verify vector dimensions

## Vector Store

- [x] Store embeddings
- [x] Retrieve embeddings

## Retriever

- [x] Retrieve Top-K chunks

## RagService

- [x] Index documents
- [x] Answer questions

## Knowledge Agent

- [x] Upload documents
- [x] Ask document questions

## ADK Integration

- [x] upload_document
- [x] ask_document

---

# Challenges Faced

## 1. Python Import Errors

Error:

```text
ModuleNotFoundError:
No module named 'project_management_agent'
```

### Cause

Running files directly instead of as Python modules.

### Solution

Run tests using:

```bash
python -m project_management_agent.rag.test.test_rag_service
```

or configure VS Code launch configurations.

---

## 2. MODEL_RETURNED_NO_CONTENT

Error

```text
MODEL_RETURNED_NO_CONTENT
```

### Cause

The upload tool returned only a minimal status message, leaving Gemini with no conversational response to produce.

### Solution

Return a user-friendly confirmation message after indexing and improve the Knowledge Agent prompt.

---

## 3. Prompt Engineering

Initially, the Knowledge Agent summarized uploaded documents immediately after indexing.

### Solution

The prompt was updated so uploads perform only indexing. Analysis occurs only when the user explicitly requests it.

---

## 4. ChromaDB Persistence

Initially embeddings were stored only in memory.

### Solution

Switched to ChromaDB's `PersistentClient` to preserve embeddings across application restarts.

---

## 5. Separation of Concerns

Instead of placing all logic in one class, responsibilities were separated into:

- Document Loader
- Text Splitter
- Embedding Service
- Vector Store
- Retriever
- LLM Service
- RagService

This improved readability, testing, and maintainability.

---

# Concepts Learned

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- ChromaDB
- Google Gemini Embeddings
- Similarity Search
- Prompt Engineering
- Context Injection
- Google ADK
- Multi-Agent Systems
- Tool Calling
- Layered Architecture
- Service Layer Pattern
- Separation of Concerns

---

# Module Outcome

At the end of Module 06, the AI Project Management application can:

- Upload PDF documents.
- Process and chunk documents.
- Generate embeddings using Gemini.
- Store vectors in ChromaDB.
- Retrieve relevant chunks using semantic search.
- Generate grounded answers using retrieved context.
- Delegate document-related requests to the Knowledge Agent.
- Answer questions from uploaded project documentation using a complete Retrieval-Augmented Generation pipeline.

---

# Future Improvements

Potential enhancements include:

- Support DOCX, TXT and Markdown documents
- Hybrid Search (Keyword + Vector Search)
- Metadata Filtering
- Document Versioning
- Duplicate Document Detection
- Delete Indexed Documents
- Re-index Updated Documents
- Streaming Responses
- RAG Evaluation Metrics
- Support Multiple Vector Databases (FAISS, Pinecone, Weaviate)

---

# Next Module

## Module 07 – Memory & Context Management

Upcoming topics:

- Session Memory
- Conversation History
- Long-Term Memory
- Context Retrieval
- Context Compression
- Memory Evaluation
- Persistent User Context

By the end of Module 07, the AI Project Management application will support multi-turn, context-aware conversations, making it behave more like an intelligent AI Project Management Copilot.