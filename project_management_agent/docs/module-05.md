# Module 05 – Task Management with SQLite

## Overview

In Module 5, the AI Project Management Agent was extended to support **Task Management**. Users can now create, list, update, and delete tasks associated with projects. All task data is persisted in SQLite and linked to projects using foreign keys.

This module follows a layered architecture where:
- **Tools** expose functionality to the LLM.
- **TaskStore** contains business logic and validation.
- **DatabaseManager** handles SQLite operations.
- **SQLite** provides persistent storage.

---

# Features Implemented

## Project Management

- ✅ Create Project
- ✅ List Projects
- ✅ Delete Project

## Task Management

- ✅ Create Task
- ✅ List All Tasks
- ✅ List Tasks for a Project
- ✅ Update Task Status
- ✅ Update Task Priority
- ✅ Delete Task

---

# Architecture

```text
User
   │
   ▼
Project Manager Agent
   │
   ▼
Tool
   │
   ▼
TaskStore
   │
   ▼
DatabaseManager
   │
   ▼
SQLite Database
```

---

# Database Schema

## Projects Table

| Column | Type | Description |
|---------|------|-------------|
| id | TEXT | Primary Key |
| name | TEXT | Unique project name |
| description | TEXT | Project description |
| created_at | TEXT | Creation timestamp |

---

## Tasks Table

| Column | Type | Description |
|---------|------|-------------|
| id | TEXT | Primary Key |
| project_id | TEXT | Foreign Key |
| title | TEXT | Task title |
| description | TEXT | Task description |
| status | TEXT | Task status |
| priority | TEXT | Task priority |
| created_at | TEXT | Creation timestamp |

### Foreign Key

```sql
FOREIGN KEY(project_id)
REFERENCES projects(id)
ON DELETE CASCADE
```

Deleting a project automatically removes all tasks belonging to that project.

---

# Folder Structure

```text
project_management_agent/

├── agents/
│   └── project_manager.py
│
├── database/
│   ├── database.py
│   └── projects.db
│
├── models/
│   ├── project.py
│   └── task.py
│
├── services/
│   ├── project_store.py
│   └── task_store.py
│
├── tools/
│   ├── create_project.py
│   ├── delete_project.py
│   ├── list_projects.py
│   ├── create_task.py
│   ├── list_tasks.py
│   ├── update_task_status.py
│   ├── update_task_priority.py
│   └── delete_task.py
│
└── prompts/
    └── project_manager_prompt.py
```

---

# Task Validation

Business validation is performed inside **TaskStore**.

## Valid Statuses

```text
Pending
In Progress
Completed
```

## Valid Priorities

```text
Low
Medium
High
```

Invalid values are rejected before reaching the database.

---

# Available Tools

## Project Tools

- create_project
- list_projects
- delete_project

## Task Tools

- create_task
- list_tasks
- update_task_status
- update_task_priority
- delete_task

The Project Manager Agent automatically chooses the appropriate tool based on the user's request.

---

# Example Prompts

## Project Management

```text
Create a project called AI Project Management
```

```text
List all projects
```

```text
Delete project AI Project Management
```

---

## Task Management

```text
Create a task called Design Database for AI Project Management
```

```text
Create a task called Build Login API for AI Project Management
```

```text
List all tasks
```

```text
List tasks for AI Project Management
```

```text
Mark Design Database as Completed
```

```text
Change Design Database priority to High
```

```text
Delete task Design Database
```

---

# Testing Checklist

## Project Operations

- [x] Create Project
- [x] Handle Duplicate Project
- [x] List Projects
- [x] Delete Project

## Task Operations

- [x] Create Task
- [x] List Tasks
- [x] List Tasks by Project
- [x] Update Task Status
- [x] Update Task Priority
- [x] Delete Task

## Database

- [x] SQLite Persistence
- [x] Foreign Key Constraint
- [x] Cascade Delete

## Agent

- [x] Tool Registration
- [x] Prompt Updated
- [x] ADK Integration

---

# Concepts Learned

- SQLite Integration
- CRUD Operations
- Foreign Keys
- Cascade Delete
- Repository Pattern
- Service Layer Pattern
- Helper Methods
- Business Validation
- Pydantic Models
- Google ADK Tools
- Agent Tool Delegation
- Separation of Concerns
- Layered Architecture

---

# Outcome

At the end of Module 5, the AI Project Management Agent can:

- Manage projects using SQLite.
- Create and manage tasks linked to projects.
- Retrieve all tasks or tasks for a specific project.
- Update task status and priority.
- Delete individual tasks.
- Automatically delete project tasks when a project is removed.
- Execute all project and task operations through natural language using Google ADK.

---

# Next Module

## Module 6 – Project Dashboard & Analytics

In the next module, the agent will move beyond CRUD operations and provide project insights, including:

- Project summaries
- Task statistics
- Pending vs Completed tasks
- Project progress
- High-priority task reporting
- Analytics dashboard
- Intelligent project overview

This will transform the agent from a CRUD assistant into an AI-powered Project Management Copilot.