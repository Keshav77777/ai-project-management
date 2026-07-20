from google.adk.agents import LlmAgent

from project_management_agent.config import MODEL_NAME
from project_management_agent.prompts.knowledge_prompt import KNOWLEDGE_PROMPT
from project_management_agent.tools.ask_document import ask_document
from project_management_agent.tools.upload_document import upload_document


knowledge_agent = LlmAgent(
    name="knowledge_agent",
    model=MODEL_NAME,
    description="Handles document indexing and document question answering using RAG.",
    instruction=KNOWLEDGE_PROMPT,
    tools=[
        upload_document,
        ask_document,
    ],
)