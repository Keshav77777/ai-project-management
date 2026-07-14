# Module 02 - Building Tools with Google ADK

## Objective

The objective of this module is to transform the Project Manager Agent from a conversational AI into an agent capable of performing real actions using Google ADK Tools.

By the end of this module, the agent can:

- Create a project
- List all existing projects
- Delete a project

The project data is stored temporarily using an in-memory service.

---

# Problem Statement

In Module 01, the Project Manager Agent could only respond with text based on user prompts.

Although it could suggest project ideas, it had no capability to execute actions or maintain project data.

This module solves that problem by introducing:

- Google ADK Tools
- A Service Layer
- Pydantic Models
- Temporary Project Storage

---

# Concepts Learned

- Google ADK Tool Calling
- Pydantic Models
- Service Layer
- Dictionary Data Structure
- Separation of Concerns
- Business Logic vs Agent Logic

---

# Folder Structure

```text
project_management_agent/
│
├── models/
│   ├── __init__.py
│   └── project.py
│
├── services/
│   ├── __init__.py
│   └── project_store.py
│
├── tools/
│   ├── __init__.py
│   ├── create_project.py
│   ├── delete_project.py
│   └── list_projects.py
│
├── prompts/
│
├── agent.py
└── config.py
```

---

# Architecture

```text
                    User
                      │
                      ▼
            ProjectManagerAgent
                      │
          LLM selects appropriate tool
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Create Tool     List Tool     Delete Tool
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                ProjectStore
                      │
                      ▼
             Project (Pydantic Model)
```

---

# Components

## 1. Project Model

The `Project` model represents a project entity.

Implemented using **Pydantic**.

### Fields

- id
- name
- description
- status
- created_at

### Why Pydantic?

- Data validation
- Type safety
- JSON serialization
- FastAPI compatibility
- Structured outputs for future modules

---

## 2. ProjectStore

The `ProjectStore` acts as an in-memory database.

Responsibilities:

- Create projects
- List projects
- Delete projects

Projects are stored in a dictionary.

```python
self.projects: dict[str, Project]
```

Each project is stored using its unique project ID as the key.

Example:

```text
{
    "1c45d...": Project(...),
    "7ab91...": Project(...)
}
```

---

## Why Dictionary Instead of List?

Instead of storing projects in a list:

```python
[
    Project(...),
    Project(...)
]
```

Projects are stored as:

```python
{
    "project_id": Project(...)
}
```

### Benefits

- Faster lookup
- Unique identifiers
- Easier updates
- Easier deletion
- Better scalability

---

# 3. Google ADK Tools

Three tools were implemented.

## create_project

Creates a new project.

Delegates business logic to `ProjectStore`.

---

## list_projects

Returns all existing projects.

---

## delete_project

Deletes a project using its name.

---

# Agent Configuration

The tools are registered with the Project Manager Agent.

```python
project_manager = LlmAgent(
    ...
    tools=[
        create_project,
        delete_project,
        list_projects,
    ]
)
```

The LLM automatically decides which tool to invoke based on the user's request.

---

# Data Flow

```text
User
   │
   ▼
ProjectManagerAgent
   │
   ▼
LLM decides which tool to execute
   │
   ▼
Python Tool
   │
   ▼
ProjectStore
   │
   ▼
Project Model
   │
   ▼
Result
   │
   ▼
LLM formats the final response
```

---

# Testing

The implementation was tested using **Google ADK Web**.

## Test Cases

### Create Project

Prompt

```
Create a project called AI Project Management Copilot.
```

Expected Result

```
Project created successfully.
```

---

### Create Duplicate Project

Prompt

```
Create a project called AI Project Management Copilot.
```

Expected Result

```
Project already exists.
```

---

### List Projects

Prompt

```
List all projects.
```

Expected Result

Displays all created projects.

---

### Delete Project

Prompt

```
Delete project AI Project Management Copilot.
```

Expected Result

```
Project deleted successfully.
```

---

### Delete Non-existing Project

Prompt

```
Delete project CRM System.
```

Expected Result

```
Project not found.
```

---

# Challenges Faced

## 1. Choosing Between List and Dictionary

Initially, projects were considered for storage in a list.

After discussing lookup efficiency and scalability, a dictionary was chosen.

Benefits:

- Faster lookup
- Easier deletion
- Unique keys

---

## 2. Dataclass vs Pydantic

The initial implementation considered Python dataclasses.

Pydantic was selected because future modules will require:

- FastAPI
- Structured Outputs
- JSON serialization
- Validation

---

## 3. Service Layer

Instead of placing business logic inside the tools, all project operations were moved into `ProjectStore`.

Benefits:

- Cleaner architecture
- Better maintainability
- Easier database migration

---

# Key Learnings

- How Google ADK invokes Python tools
- Difference between Agent, Tool and Service
- Using Pydantic models
- Using dictionaries for in-memory storage
- Singleton pattern
- Separation of concerns
- Layered architecture

---

# Interview Questions

## Why did you use Pydantic instead of a dataclass?

Pydantic provides built-in validation, serialization, FastAPI compatibility, and supports structured outputs, making it better suited for production AI applications.

---

## Why store projects in a dictionary?

A dictionary allows constant-time average lookups using project IDs and simplifies updates and deletions compared to iterating through a list.

---

## What is the responsibility of ProjectStore?

ProjectStore manages project data and contains the business logic for project operations. It acts as the application's data layer.

---

## What is the responsibility of Google ADK Tools?

Tools expose Python functions that the LLM can invoke. They bridge the gap between natural language requests and application logic.

---

## What is the responsibility of the Agent?

The agent understands the user's request, selects the appropriate tool, invokes it, and generates a natural language response based on the tool's output.

---

# Improvements

Future enhancements include:

- Persistent SQLite database
- Update project status
- Rename project
- Search projects
- Task management
- User management
- Analytics and reporting

---

# Module Status

✅ Completed

---

# Next Module

## Module 03 - Multi-Agent Architecture

Topics to be covered:

- Parent Agent
- Child Agents
- Agent Delegation
- Specialized AI Agents
- Multi-Agent Collaboration
- Agent Routing
- Shared Context