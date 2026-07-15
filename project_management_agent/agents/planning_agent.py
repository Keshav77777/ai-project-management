from google.adk.agents import LlmAgent

from project_management_agent.config import MODEL_NAME
from project_management_agent.prompts.planning_prompt import (
    PLANNING_PROMPT,
)
from project_management_agent.models.planning import ProjectPlan

planning_agent = LlmAgent(
    name="planning_agent",
    model=MODEL_NAME,
    instruction=PLANNING_PROMPT,
)