from google.adk.agents import LlmAgent

from project_management_agent.prompts.project_manager_prompt import (
    PROJECT_MANAGER_PROMPT,
)
from project_management_agent.tools.create_project import create_project
from project_management_agent.tools.delete_project import delete_project
from project_management_agent.tools.list_projects import list_projects
from project_management_agent.agents.planning_agent import planning_agent
from project_management_agent.agents.risk_agent import risk_agent
from project_management_agent.config import MODEL_NAME

project_manager = LlmAgent(
    name="project_manager",
    model=MODEL_NAME,
    instruction=PROJECT_MANAGER_PROMPT,
    tools=[
        create_project,
        delete_project,
        list_projects,
        ],
    sub_agents=[
        planning_agent,
        risk_agent,
    ]
)