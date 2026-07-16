# Module 04 – SQLite Persistence Layer

## Objective

In this module, the project transitions from an in-memory project store to a persistent SQLite database. This ensures that project data is retained even after the application is restarted.

---

## Features Implemented

- SQLite database integration
- Automatic database initialization
- Projects table creation
- Persistent project storage
- CRUD operations using SQL
- Refactored `ProjectStore` to use `DatabaseManager`
- Removed dependency on in-memory dictionary storage

---

## Architecture

```
                User
                  │
                  ▼
          Project Manager Agent
                  │
                  ▼
              ADK Tool
                  │
                  ▼
            ProjectStore
                  │
                  ▼
          DatabaseManager
                  │
                  ▼
             SQLite Database
```

---

## Database Schema

### Projects Table

| Column | Type | Description |
|---------|------|-------------|
| id | TEXT | Primary Key |
| name | TEXT | Unique project name |
| description | TEXT | Project description |
| created_at | TEXT | Project creation timestamp |

---

## Folder Structure

```
project_management_agent/
│
├── database/
│   ├── database.py
│   └── projects.db
│
├── models/
│   └── project.py
│
├── services/
│   └── project_store.py
│
├── tools/
│   ├── create_project.py
│   ├── delete_project.py
│   └── list_projects.py
```

---

## DatabaseManager Responsibilities

The `DatabaseManager` is responsible for:

- Initializing the SQLite database
- Creating database tables
- Creating projects
- Listing projects
- Deleting projects

It acts as the application's persistence layer.

---

## ProjectStore Responsibilities

`ProjectStore` is now a service layer.

Responsibilities:

- Create `Project` objects
- Delegate database operations to `DatabaseManager`

It no longer stores project data in memory.

---

## CRUD Operations

### Create Project

```python
database_manager.create_project(project)
```

Stores a project in SQLite.

---

### List Projects

```python
database_manager.list_projects()
```

Returns a list of `Project` objects.

---

### Delete Project

```python
database_manager.delete_project(name)
```

Deletes a project by name.

---

## SQLite Features Used

- CREATE TABLE IF NOT EXISTS
- INSERT INTO
- SELECT
- DELETE
- PRIMARY KEY
- UNIQUE constraint
- Parameterized SQL queries (`?`)
- Transactions using `commit()`

---

## Testing

### Create Project

```
Create a project called AI Project Management with description Learning Google ADK
```

Expected:

```
Project created successfully.
```

---

### List Projects

```
List all projects
```

Expected:

```
Project Name
Description
Created At
```

---

### Delete Project

```
Delete project AI Project Management
```

Expected:

```
Project deleted successfully.
```

---

### Persistence Test

1. Create a project.
2. Stop the ADK server.
3. Restart the ADK server.
4. List projects.

The project should still exist, demonstrating persistent storage.

---

## Design Improvements

### Before Module 4

```
Agent
   │
Tool
   │
ProjectStore
   │
Dictionary
```

Project data was lost whenever the application stopped.

---

### After Module 4

```
Agent
   │
Tool
   │
ProjectStore
   │
DatabaseManager
   │
SQLite
```

Project data is now permanently stored.

---

## Key Learning Outcomes

- SQLite fundamentals
- Database initialization
- CRUD operations
- Parameterized SQL queries
- Layered architecture
- Service layer pattern
- Persistence layer design
- Separation of concerns
- Pydantic model mapping
- Using SQLite with Python

---

## Next Module

Module 05 will introduce **Task Management**, where each project can contain multiple tasks. This module will expand the database schema and implement relationships between projects and tasks.