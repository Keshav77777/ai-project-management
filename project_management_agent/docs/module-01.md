# Module 01 - Google ADK Foundation

## Objective

The goal of Module 1 is to understand the fundamental building blocks of Google Agent Development Kit (ADK) and create the first working AI agent.

At the end of this module, the application should be able to accept a project idea and generate a structured software project overview.

---

# Learning Objectives

After completing this module I should understand:

- What Google ADK is
- What an LLM Agent is
- What a Root Agent is
- How prompts work
- Google ADK project structure
- Environment configuration
- Running applications using ADK Web

---

# Concepts Learned

## 1. Google ADK

Google Agent Development Kit (ADK) is a framework for building AI agents.

Instead of interacting directly with an LLM, ADK provides:

- Agent abstraction
- Session management
- Tool execution
- Memory
- Multi-agent orchestration
- Event streaming

Throughout this project, ADK will be used as the orchestration layer.

---

## 2. LLM Agent

An LLM Agent represents an AI assistant with a specific responsibility.

For Module 1, the agent is:

**Project Manager**

Responsibilities:

- Analyze project ideas
- Suggest features
- Recommend technology stack
- Identify risks
- Generate a high-level roadmap

Example:

User

```
Build an online grocery delivery application.
```

↓

Project Manager Agent

↓

```
Summary
Features
Tech Stack
Risks
Roadmap
```

---

## 3. Prompt Engineering

Instead of writing prompts directly inside the code, prompts are stored separately.

```
project_management_agent/
└── prompts/
    └── project_manager_prompt.py
```

Benefits:

- Easier maintenance
- Version control
- Reusable prompts
- Better separation of concerns

---

## 4. Root Agent

Google ADK requires one entry point called the **Root Agent**.

```
project_management_agent/
│
└── agent.py
```

Example:

```python
root_agent = project_manager
```

When ADK starts, it loads this agent first.

---

## 5. Project Structure

Current structure:

```
ai-project-management/
│
├── project_management_agent/
│   ├── agent.py
│   ├── agents/
│   ├── prompts/
│   ├── tools/
│   └── config.py
│
├── docs/
├── README.md
└── requirements.txt
```

The structure is intentionally modular to make future modules easier to implement.

---

# Why We Removed Runner

Initially, the project contained a `runner.py`.

Older Google ADK tutorials create a Runner manually.

Example:

```
Runner
    ↓
Agent
```

However, Google ADK 2.4.0 introduced a different execution model where the Runner depends on a SessionService and is typically managed by ADK itself during development.

Current execution flow:

```
User
    ↓
Session
    ↓
Runner
    ↓
Events
    ↓
Agent
```

Instead of manually creating a Runner, we use **ADK Web**.

Benefits:

- Session management
- Streaming
- Event inspection
- Debugging
- Future compatibility

A custom Runner will be implemented in a later module.

---

# Absolute Imports

During development, import errors occurred because Python could not locate local packages.

Incorrect:

```python
from agents.project_manager import project_manager
```

Correct:

```python
from project_management_agent.agents.project_manager import project_manager
```

Using absolute imports makes the project compatible with ADK, testing frameworks, and production deployments.

---

# Running the Project

From the project root:

```bash
adk web
```

Open:

```
http://127.0.0.1:8000
```

The Project Manager Agent should now be available through the ADK Web interface.

---

# Challenges Faced

## Runner Initialization

Problem:

```
Runner.__init__() missing required keyword argument:
session_service
```

Reason:

The project was using an older Runner implementation that is no longer compatible with Google ADK 2.4.0.

Solution:

Use ADK Web during development and postpone custom Runner implementation until the SessionService is introduced.

---

## Package Import Errors

Problem:

```
ModuleNotFoundError
```

Reason:

Python was using relative imports.

Solution:

Use absolute imports based on the project package.

---

# Git Commits

```
chore: initialize project structure

feat: create Project Manager agent

feat: add project manager prompt

docs: complete Module 1 documentation
```

---

# Module 1 Deliverables

- Repository initialized
- Virtual environment configured
- Google ADK installed
- Environment variables configured
- Project Manager Agent created
- Prompt separated from code
- Root Agent configured
- ADK Web running
- Project documentation completed

---

# What Comes Next

Module 2 focuses on Tool Calling.

New concepts:

- Tool registration
- Function calling
- SessionService
- Runner
- Custom CLI
- Project creation tools
- Task management tools