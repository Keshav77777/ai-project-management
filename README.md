# AI Project Management Agent

A production-oriented **Multi-Agent Project Management Assistant** built using **Google Agent Development Kit (ADK)**.

The project demonstrates how to build an enterprise-style AI system using multiple specialized agents, persistent storage, Retrieval-Augmented Generation (RAG), conversational memory, and the **Model Context Protocol (MCP)**.

---

# Features

- Multi-Agent Architecture
- Project Management
- Task Management
- Risk Analysis
- Project Planning
- Knowledge Management
- Retrieval-Augmented Generation (RAG)
- Conversational Memory
- SQLite Persistence
- MCP Server
- MCP Client Integration
- Dynamic Tool Discovery

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Framework | Google ADK 2.4.0 |
| Language | Python 3.13 |
| Database | SQLite |
| Vector Search | ChromaDB |
| LLM | Gemini |
| Embeddings | Gemini Embeddings |
| Protocol | MCP (Model Context Protocol) |
| API | FastAPI |
| Package Manager | pip |
| Environment | python-dotenv |

---

# Project Architecture

```
                               User
                                 │
                                 ▼
                     Project Manager Agent
                           (Root Agent)
                                 │
          ┌──────────────────────┼──────────────────────┐
          ▼                      ▼                      ▼
    Planning Agent         Risk Agent         Knowledge Agent
                                 │
                                 ▼
                        Memory Manager
                                 │
                                 ▼
                           MCP Tool Client
                                 │
                                 ▼
                 Project Management MCP Server
                                 │
      ┌──────────────┬──────────────┬──────────────┐
      ▼              ▼              ▼
 Project Tools   Task Tools   Knowledge Tools
      │              │              │
      └──────────────┼──────────────┘
                     ▼
        SQLite • Memory • RAG Pipeline
```

---

# Folder Structure

```
project_management_agent/

├── agents/
│   ├── project_manager.py
│   ├── planning_agent.py
│   ├── risk_agent.py
│   └── knowledge_agent.py
│
├── database/
│
├── knowledge/
│
├── mcp/
│   ├── client.py
│   ├── server.py
│   └── tools/
│
├── memory/
│
├── models/
│
├── prompts/
│
├── rag/
│
├── services/
│
├── tools/
│
├── config.py
└── agent.py
```

---

# Implemented Modules

---

## Module 1 — Project Setup

### Implemented

- Google ADK setup
- Project structure
- Environment configuration
- Root agent
- Prompt separation
- Configuration management

---

## Module 2 — Project Management

Implemented project CRUD operations.

### Features

- Create Project
- Delete Project
- List Projects

---

## Module 3 — Planning Agent

Created a specialized planning agent responsible for generating project plans.

Responsibilities include:

- Project planning
- Task breakdown
- Timeline generation
- Milestone suggestions

---

## Module 4 — SQLite Persistence

Replaced in-memory storage with SQLite.

Implemented

- Database Manager
- SQLite schema
- Persistent project storage
- Repository layer

---

## Module 5 — Task Management

Added complete task lifecycle management.

### Features

- Create Task
- List Tasks
- Update Status
- Update Priority
- Delete Task

---

## Module 6 — Knowledge Agent (RAG)

Implemented Retrieval-Augmented Generation.

### Features

- Document Upload
- Chunking
- Embedding Generation
- Vector Storage
- Semantic Search
- Question Answering

---

## Module 7 — Context Memory

Implemented conversational memory.

The agent remembers:

- Current Project
- Current Task

Example

Instead of

```
Create task Design API for AI Project
```

User can simply say

```
Create task Design API
```

The project is inferred from memory.

---

## Module 8 — Model Context Protocol (MCP)

One of the major milestones of this project.

Implemented:

### MCP Server

Exposes all business capabilities as MCP tools.

### MCP Client

Integrated Google ADK with MCP Toolset.

### Tool Discovery

Agent dynamically discovers available tools.

### Registered Tools

Project

- Create Project
- Delete Project
- List Projects

Task

- Create Task
- List Tasks
- Update Task Status
- Update Task Priority
- Delete Task

Knowledge

- Upload Document

---

# Agents

## Project Manager

Root orchestration agent.

Responsible for:

- User interaction
- Tool selection
- Agent delegation

---

## Planning Agent

Responsible for

- Planning
- Milestones
- Timeline generation

---

## Risk Agent

Responsible for

- Risk identification
- Risk mitigation
- Dependency analysis

---

## Knowledge Agent

Responsible for

- Document understanding
- Semantic search
- RAG

---

# Memory

Current implementation stores

- Current Project
- Current Task

Future improvements

- Session memory
- Redis
- Long-term memory
- User preferences

---

# Database

SQLite stores

Projects

- id
- name
- description
- created_at

Tasks

- id
- project_id
- title
- description
- priority
- status
- created_at

---

# MCP Architecture

```
Project Manager Agent

↓

MCP Client

↓

Project Management MCP Server

↓

Project Tools

↓

Database
```

Benefits

- Loose coupling
- Dynamic tool discovery
- Reusable tools
- Production-ready architecture

---

# Current Capabilities

## Project Management

- Create Project
- Delete Project
- List Projects

---

## Task Management

- Create Task
- List Tasks
- Update Task Status
- Update Task Priority
- Delete Task

---

## Planning

- Generate Project Plans
- Task Breakdown
- Milestone Suggestions

---

## Risk Analysis

- Risk Identification
- Risk Mitigation
- Dependency Analysis

---

## Knowledge

- Upload Documents
- Semantic Retrieval
- Question Answering

---

## Memory

- Context-aware conversations

---

## MCP

- Dynamic tool execution
- Tool discovery
- Standardized protocol

---

# Setup

## Clone Repository

```bash
git clone <repository-url>
cd ai-project-management
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env`

```
GOOGLE_API_KEY=YOUR_KEY
MODEL_NAME=gemini-2.5-flash
```

---

## Run ADK

```bash
adk web
```

---

## Run MCP Server

```bash
python -m project_management_agent.mcp.server
```

---

# Example Commands

```
Create project AI PM
```

```
List projects
```

```
Create task Design Database
```

```
Update task status to DONE
```

```
Set priority HIGH
```

```
Upload requirements document
```

```
Generate project plan
```

```
Identify project risks
```

---

# Roadmap

## Completed

- ✅ Google ADK
- ✅ Multi-Agent System
- ✅ SQLite
- ✅ Task Management
- ✅ RAG
- ✅ Memory
- ✅ MCP Integration


# Learning Outcomes

This project demonstrates practical implementation of:

- Google ADK
- Agent Orchestration
- Multi-Agent Systems
- MCP
- SQLite Integration
- RAG Pipelines
- Conversational Memory
- Tool Calling
- Prompt Engineering
- Modular AI Architecture

---


# Acknowledgements

- Google Agent Development Kit (ADK)
- Model Context Protocol (MCP)
- SQLite
- ChromaDB
- Gemini Models
