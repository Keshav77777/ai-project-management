from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StdioConnectionParams,
)
from mcp import StdioServerParameters


project_management_mcp = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="python",
            args=[
                "-m",
                "project_management_agent.mcp.server",
            ],
        ),
        timeout=30,  # Explicit timeout in seconds
    ),
)