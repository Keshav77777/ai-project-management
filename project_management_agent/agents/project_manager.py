from google.adk.agents import LlmAgent

from project_management_agent.prompts.project_manager_prompt import (
    PROJECT_MANAGER_PROMPT,
)
from project_management_agent.config import MODEL_NAME

project_manager = LlmAgent(
    name="project_manager",
    model=MODEL_NAME,
    instruction=PROJECT_MANAGER_PROMPT,
)