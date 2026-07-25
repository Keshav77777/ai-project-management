from mcp.server.fastmcp import FastMCP

from project_management_agent.mcp.tools.project_tools import (
    create_project,
    list_projects,
    delete_project,
)

from project_management_agent.mcp.tools.task_tools import (
    create_task,
    list_tasks,
    update_task_status,
    update_task_priority,
    delete_task,
)

from project_management_agent.mcp.tools.knowledge_tools import (
    upload_document,
)

mcp = FastMCP("Project Management MCP")

# Project tools
mcp.tool()(create_project)
mcp.tool()(list_projects)
mcp.tool()(delete_project)

# Task tools
mcp.tool()(create_task)
mcp.tool()(list_tasks)
mcp.tool()(update_task_status)
mcp.tool()(update_task_priority)
mcp.tool()(delete_task)

# Knowledge tools
mcp.tool()(upload_document)

if __name__ == "__main__":
    mcp.run()