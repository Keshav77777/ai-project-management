# Module 8 – Model Context Protocol (MCP)

## Overview

In this module, we transformed our Project Management Agent into an **MCP-powered AI system** by exposing all project management capabilities through a **Model Context Protocol (MCP) Server**.

Instead of directly registering Python functions with the ADK agent, the agent now discovers and invokes tools dynamically through an MCP client.

This architecture closely resembles how production AI systems integrate with external services.

---

## Objectives

- Understand the Model Context Protocol (MCP)
- Build a custom MCP Server
- Expose project management tools through MCP
- Register Project, Task, and Knowledge tools
- Connect Google ADK as an MCP Client
- Enable dynamic tool discovery
- Validate communication using MCP Inspector

---

# What is MCP?

The **Model Context Protocol (MCP)** is an open standard that enables AI agents to communicate with external tools and services using a standardized interface.

Instead of embedding business logic directly into an agent, MCP separates:

- AI reasoning
- Tool execution
- External systems

This makes tools reusable across multiple AI applications.

---

# Architecture

```
                 User
                   │
                   ▼
          Project Manager Agent
             (Google ADK)
                   │
                   ▼
             MCP Toolset Client
                   │
          STDIO Transport Layer
                   │
                   ▼
         Project Management MCP Server
                   │
      ┌────────────┼─────────────┐
      ▼            ▼             ▼
 Project Tools  Task Tools  Knowledge Tools
      │            │             │
      └────────────┼─────────────┘
                   ▼
       SQLite • Memory • RAG
```

---

# Folder Structure

```
project_management_agent/
│
├── mcp/
│   ├── __init__.py
│   ├── server.py
│   ├── client.py
│   │
│   └── tools/
│       ├── project_tools.py
│       ├── task_tools.py
│       └── knowledge_tools.py
```

---

# MCP Server

Created a dedicated MCP server using FastMCP.

```python
mcp = FastMCP("Project Management MCP")
```

The server is responsible for:

- Registering tools
- Handling MCP requests
- Returning tool metadata
- Executing tool calls

---

# Project Tools

The following Project tools were exposed through MCP.

- Create Project
- Delete Project
- List Projects

Example registration:

```python
mcp.tool()(create_project)
```

---

# Task Tools

Task management capabilities were also exposed.

Available tools:

- Create Task
- List Tasks
- Update Task Status
- Update Task Priority
- Delete Task

---

# Knowledge Tools

Knowledge management tools were added to the MCP server.

Current implementation:

- Upload Document

This allows future integration with our RAG pipeline.

---

# MCP Client

Instead of directly importing Python functions into the ADK agent, we created an MCP client.

The client launches the MCP server and dynamically discovers available tools.

```python
project_management_mcp = McpToolset(...)
```

The agent now communicates only with the MCP server.

---

# Tool Discovery

One of the biggest advantages of MCP is automatic tool discovery.

Instead of manually maintaining a list of available functions, the agent requests tool metadata from the MCP server.

This enables:

- Dynamic tool registration
- Loose coupling
- Easier extensibility

---

# MCP Inspector

We used the **MCP Inspector** to validate our implementation.

Verified:

- Server startup
- MCP initialization
- Tool discovery
- Tool invocation
- Request/Response flow

Inspector successfully displayed all registered tools.

---

# Agent Changes

## Before MCP

```
Project Manager Agent

↓

create_project()

↓

create_task()

↓

delete_project()
```

The agent directly invoked Python functions.

---

## After MCP

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

The agent is now completely decoupled from the business logic.

---

# Benefits of MCP

Our project now supports:

- Standardized tool interface
- Dynamic tool discovery
- Reusable tool servers
- Better separation of concerns
- Easier maintenance
- Production-style architecture

---

# Challenges Faced

During implementation we encountered several issues.

### Module Import Errors

Resolved package import issues when running the MCP server.

---

### Python Package Structure

Updated project structure to support module execution.

---

### MCP Inspector Setup

Installed Node.js and configured the MCP Inspector for testing.

---

### Tool Registration

Verified every tool was properly exposed through the MCP server.

---

### ADK Integration

Configured Google ADK to connect to the MCP server using an MCP Toolset.

---

### End-to-End Testing

Successfully verified:

- Tool discovery
- Tool execution
- Agent-to-MCP communication

---

# Current MCP Capabilities

Project Management

- Create Project
- Delete Project
- List Projects

Task Management

- Create Task
- List Tasks
- Update Task Status
- Update Task Priority
- Delete Task

Knowledge

- Upload Document

---

# Why MCP Matters

Without MCP:

```
Agent
 │
 ├── create_project()
 ├── create_task()
 ├── delete_project()
```

The agent is tightly coupled to the implementation.

---

With MCP:

```
Agent

↓

MCP Client

↓

MCP Server

↓

Any Tool
```

The agent only understands capabilities—not implementations.

This makes it possible to replace or extend backend services without modifying the agent itself.

---

# Key Learning Outcomes

By completing this module, we learned:

- Fundamentals of the Model Context Protocol
- MCP architecture
- FastMCP server development
- Tool registration
- MCP client configuration
- Tool discovery
- MCP Inspector debugging
- ADK and MCP integration
- Production-style agent architecture

---

# Module Summary

✅ Built a custom MCP Server

✅ Exposed Project tools

✅ Exposed Task tools

✅ Exposed Knowledge tools

✅ Created an MCP Client

✅ Connected Google ADK with MCP

✅ Validated tools using MCP Inspector

✅ Enabled dynamic tool discovery

✅ Decoupled business logic from the AI agent

---
