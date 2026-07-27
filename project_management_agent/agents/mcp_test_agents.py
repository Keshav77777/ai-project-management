from google.adk.agents import LlmAgent

from project_management_agent.mcp.client import project_management_mcp

mcp_test_agent = LlmAgent(
    name="mcp_test_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a Project Management Assistant.

    Always use the available tools whenever possible.
    """,
    tools=[
        project_management_mcp,
    ],
)