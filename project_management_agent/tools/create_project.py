from project_management_agent.memory.memory_manager import memory_manager
from project_management_agent.services.project_store import project_store


def create_project(
    name: str,
    description: str = "",
) -> str:
    """
    Creates a new project.

    Args:
        name: Name of the project.
        description: Short description of the project.

    Returns:
        Success or error message.
    """

    result = project_store.create_project(name, description)

    if result.startswith("Project created"):
        memory_manager.set_current_project(name)

    return result