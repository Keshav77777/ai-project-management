from project_management_agent.memory.memory_manager import memory_manager
from project_management_agent.services.project_store import project_store


def delete_project(name: str) -> str:
    """
    Delete an existing project.

    Args:
        name: Name of the project to delete.

    Returns:
        Success or error message.
    """
    result = project_store.delete_project(name)

    if result.startswith("Project deleted"):
        if memory_manager.get_current_project() == name:
            memory_manager.clear_current_project()

    return result