from google.adk.agents import LlmAgent

from project_management_agent.prompts.project_manager_prompt import (
    PROJECT_MANAGER_PROMPT,
)
from project_management_agent.mcp.client import project_management_mcp
from project_management_agent.tools.create_project import create_project
from project_management_agent.tools.delete_project import delete_project
from project_management_agent.tools.list_projects import list_projects
from project_management_agent.tools.create_task import create_task
from project_management_agent.tools.list_tasks import list_tasks
from project_management_agent.tools.update_task_status import update_task_status
from project_management_agent.tools.delete_task import delete_task
from project_management_agent.tools.update_task_priority import update_task_priority



from project_management_agent.agents.planning_agent import planning_agent
from project_management_agent.agents.risk_agent import risk_agent
from project_management_agent.config import MODEL_NAME
from project_management_agent.agents.knowledge_agent import knowledge_agent



project_manager = LlmAgent(
    name="project_manager",
    model=MODEL_NAME,
    description=(
        "Coordinates project management activities and delegates "
        "planning, risk analysis, and document-based queries "
        "to specialized agents."
    ),
    instruction=PROJECT_MANAGER_PROMPT,
    tools=[
        # create_project,
        # delete_project,
        # list_projects,
        # create_task,
        # list_tasks,
        # update_task_status,
        # update_task_priority,
        # delete_task,
        project_management_mcp,
    ],
    sub_agents=[
        planning_agent,
        risk_agent,
        knowledge_agent,
    ],
)