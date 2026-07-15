from google.adk.agents import LlmAgent

from project_management_agent.config import MODEL_NAME
from project_management_agent.prompts.risk_prompt import (
    RISK_PROMPT
)

risk_agent = LlmAgent(
    name="risk_agent",
    model=MODEL_NAME,
    instruction=RISK_PROMPT,
)