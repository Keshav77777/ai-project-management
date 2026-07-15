# Module 03 - Multi-Agent Architecture

## Objective

In this module, the Project Management Agent was transformed from a single-agent application into a multi-agent system using Google ADK.

The ProjectManagerAgent now acts as an orchestrator, delegating specialized tasks to dedicated sub-agents while continuing to use tools for project management operations.

---

## What We Built

### 1. Planning Agent

Created a dedicated Planning Agent responsible for:

- Project planning
- Project phases
- Milestones
- Deliverables
- Timelines
- Work Breakdown Structure (WBS)
- Roadmaps

---

### 2. Risk Agent

Created a dedicated Risk Agent responsible for:

- Risk identification
- Risk assessment
- Risk mitigation
- Dependencies
- Assumptions
- Constraints
- Potential blockers

---

### 3. Project Manager as an Orchestrator

Updated the ProjectManagerAgent to:

- Delegate planning requests to the Planning Agent.
- Delegate risk-related requests to the Risk Agent.
- Execute project management tools.
- Respond directly when no specialist agent or tool is required.

---

### 4. Multi-Agent Delegation

Configured the ProjectManagerAgent with multiple sub-agents:

- Planning Agent
- Risk Agent

This allows the Project Manager to route user requests to the most appropriate specialist.

---

## Architecture

```
                        User
                          │
                          ▼
                 ProjectManagerAgent
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
   PlanningAgent                  RiskAgent
          │
          └───────────────┐
                          │
                          ▼
                    Project Tools
               • Create Project
               • Delete Project
               • List Projects
```

---

## Project Structure

```
project_management_agent/

├── agent.py
├── config.py
│
├── agents/
│   ├── project_manager.py
│   ├── planning_agent.py
│   └── risk_agent.py
│
├── prompts/
│   ├── project_manager_prompt.py
│   ├── planning_prompt.py
│   └── risk_prompt.py
│
├── tools/
│   ├── create_project.py
│   ├── delete_project.py
│   ├── list_projects.py
│   └── get_time.py
│
├── services/
│   └── project_store.py
│
└── models/
    └── project.py
```

---

## Key Learnings

- Understanding the Parent Agent pattern.
- Creating specialized sub-agents.
- Prompt engineering for agent routing.
- Agent delegation using `sub_agents`.
- Tool calling vs agent delegation.
- Reading ADK Trace View.
- Designing scalable multi-agent systems.

---

## Testing Performed

### Planning Agent

Prompt:

```
Create a project plan for an AI Resume Builder.
```

Expected Result:

```
ProjectManagerAgent
        ↓
PlanningAgent
```

---

### Risk Agent

Prompt:

```
Identify the top 5 risks in developing an AI Resume Builder.
```

Expected Result:

```
ProjectManagerAgent
        ↓
RiskAgent
```

---

### Project Tools

Prompt:

```
Create a project named AI Resume Builder.
```

Expected Result:

```
ProjectManagerAgent
        ↓
create_project()
```

---

## Challenges Faced

### Multiple Intent Request

Prompt:

```
Create a project plan and identify the top 5 risks.
```

Initially, the Project Manager delegated only to the Planning Agent because the request contained both planning and risk analysis.

This demonstrated how the parent agent chooses a primary specialist for a mixed-intent request. Future modules may introduce more advanced orchestration to combine responses from multiple specialist agents.

---

## Outcome

By the end of this module, the application evolved from a single-agent assistant into a multi-agent project management system capable of:

- Delegating planning tasks
- Delegating risk analysis
- Executing project management tools
- Routing user requests intelligently
- Visualizing agent transfers using ADK Trace View

This architecture provides a scalable foundation for adding more specialist agents in future modules.