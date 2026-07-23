# Module 07 – Conversational Memory

## Objective

In this module, we enhance the AI Project Management System by introducing conversational memory.

Until now, the agent treated every user request as an independent interaction. With conversational memory, the agent can now remember important information throughout a session, enabling more natural conversations without requiring the user to repeat context.

For example:

User:

> Create a project called AI Project Management.

Later:

> Create a task called Design Database.

The agent automatically understands that the task belongs to the current project without asking for the project name again.

---

# Learning Objectives

By the end of this module, you will understand:

- What conversational memory is
- Session-based memory
- Memory Manager pattern
- Context Manager pattern
- Managing conversation context
- Tracking active project
- Tracking active task
- Tracking uploaded documents
- Integrating memory into ADK tools
- Building context-aware AI agents

---

# Why Memory?

Without memory:

```
User:
Create project AI PM

Assistant:
Project created.

User:
Create task Login API

Assistant:
Which project?
```

With memory:

```
User:
Create project AI PM

Assistant:
Project created.

User:
Create task Login API

Assistant:
Task created successfully.
```

The assistant remembers the current project.

---

# Architecture

```
                User
                  │
                  ▼
        Project Manager Agent
                  │
                  ▼
              ADK Tools
                  │
                  ▼
          Memory Manager
                  │
                  ▼
          Session Memory
                  │
                  ▼
      Current Conversation Context
```

---

# Project Structure

```
project_management_agent/

memory/
│
├── session_memory.py
├── memory_manager.py
└── context_manager.py
```

---

# Session Memory

## Purpose

Stores important information for the current conversation.

Current implementation stores:

- Current Project
- Current Task
- Last Uploaded Document

Example:

```
Current Project:
AI Project Management

Current Task:
Design Database

Last Uploaded Document:
requirements.pdf
```

---

# Memory Manager

## Purpose

Acts as the interface between tools and Session Memory.

Instead of tools directly modifying memory, every tool communicates through the Memory Manager.

Responsibilities:

- Set current project
- Get current project
- Clear current project
- Set current task
- Get current task
- Clear current task
- Set last uploaded document
- Get last uploaded document
- Clear uploaded document

Benefits:

- Single responsibility
- Easier maintenance
- Centralized memory operations
- Better separation of concerns

---

# Context Manager

## Purpose

Builds conversation context from memory.

Example:

```
Current Project:
AI Project Management

Current Task:
Design Database

Uploaded Document:
requirements.pdf
```

The context can later be injected into prompts to make conversations more natural.

---

# Tool Integration

Memory was integrated into multiple tools.

## create_project

After successfully creating a project:

```
Create Project
      │
      ▼
Database
      │
      ▼
Memory Manager
      │
      ▼
Current Project Updated
```

---

## delete_project

When deleting a project:

```
Delete Project
      │
      ▼
Database
      │
      ▼
Clear Current Project
```

---

## create_task

If no project name is provided:

```
Create Task
      │
      ▼
Memory Manager
      │
      ▼
Current Project
      │
      ▼
TaskStore
```

If task creation succeeds:

```
Current Task Updated
```

---

## update_task_status

When task status changes:

```
Update Status
      │
      ▼
Database
      │
      ▼
Current Task Updated
```

---

## update_task_priority

When task priority changes:

```
Update Priority
      │
      ▼
Database
      │
      ▼
Current Task Updated
```

---

## delete_task

After deleting a task:

```
Delete Task
      │
      ▼
Database
      │
      ▼
Clear Current Task
```

---

## upload_document

After indexing a document:

```
Upload PDF
      │
      ▼
Knowledge Base
      │
      ▼
Memory Manager
      │
      ▼
Last Uploaded Document Updated
```

---

# Memory Flow

```
User
 │
 ▼
Create Project
 │
 ▼
ProjectStore
 │
 ▼
SQLite
 │
 ▼
Memory Manager
 │
 ▼
Session Memory
```

Later:

```
User
 │
 ▼
Create Task
 │
 ▼
Memory Manager
 │
 ▼
Current Project
 │
 ▼
TaskStore
```

---

# Separation of Responsibilities

## Tools

Responsible for:

- Reading memory
- Updating memory
- Calling service layer

---

## Services

Responsible for:

- Business logic
- Validation
- Calling DatabaseManager

Services do **not** interact with memory.

---

## Database

Responsible only for persistence.

No knowledge of:

- Current project
- Current task
- Session state

---

# Benefits of This Design

- Clean Architecture
- Separation of Concerns
- Easier Testing
- Reusable Services
- Context-Aware Conversations
- Easier Future Expansion

---

# Current Memory Fields

| Field | Purpose |
|--------|---------|
| Current Project | Tracks active project |
| Current Task | Tracks active task |
| Last Uploaded Document | Tracks active document |

---

# Example Conversation

```
User:
Create project AI Project Management

Assistant:
Project created successfully.
```

Memory:

```
Current Project:
AI Project Management
```

---

```
User:
Create task Design Database
```

The tool retrieves:

```
Current Project:
AI Project Management
```

Task is automatically created under the remembered project.

---

```
User:
Mark Design Database as Completed
```

Memory becomes:

```
Current Task:
Design Database
```

---

```
User:
Delete Design Database
```

Memory:

```
Current Task:
None
```

---

# Challenges Faced

## 1. Mixing Memory with Service Layer

Initially, memory logic was mistakenly added inside `TaskStore`.

Problem:

- Services became aware of conversation state.
- Violated separation of concerns.
- Introduced recursive calls.

Solution:

Move all memory operations to the tool layer.

---

## 2. Recursive Function Calls

An incorrect implementation caused `TaskStore.create_task()` to call itself, resulting in recursion and runtime errors.

Solution:

Restore `TaskStore` as a pure service that only interacts with the database.

---

## 3. Missing `self` in Service Methods

While refactoring, the `self` parameter was accidentally removed from service methods.

Result:

```
TypeError:
got multiple values for argument
```

Solution:

Restore proper instance method signatures.

---

## 4. Tool vs Service Responsibilities

Initially, tool logic and business logic became mixed.

Final architecture:

```
User
 │
 ▼
Tool
 │
 ▼
Service
 │
 ▼
Database
```

Each layer has a single responsibility.

---

## 5. API Rate Limits

While testing multiple agents and tools, the Gemini API returned:

```
429 RESOURCE_EXHAUSTED
```

Reason:

Exceeded the free-tier request quota during development and debugging.

Resolution:

- Wait for quota reset.
- Reduce unnecessary LLM calls.
- Test services independently where possible.
- Consider enabling billing or using a different model if higher limits are required.

---

# Key Takeaways

- Memory enables context-aware conversations.
- Only tools should read and update session memory.
- Services should remain independent of conversation state.
- Databases should only handle persistence.
- Separating memory from business logic results in cleaner, more maintainable code.

---

# Module Outcome

At the end of this module, the AI Project Management System can:

- Remember the current project.
- Remember the current task.
- Remember the last uploaded document.
- Automatically reuse conversation context.
- Reduce repetitive user input.
- Provide a more natural conversational experience.

---