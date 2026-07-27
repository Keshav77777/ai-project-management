import asyncio

from project_management_agent.mcp.client import project_management_mcp


async def main():
    tools = await project_management_mcp.get_tools()

    print(f"Found {len(tools)} tools")

    for tool in tools:
        print(tool.name)


asyncio.run(main())