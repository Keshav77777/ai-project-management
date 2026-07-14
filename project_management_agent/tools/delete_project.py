from project_management_agent.services.project_store import project_store


def delete_project(name: str) -> str:
    """
    Delete an existing project.

    Args:
        name: Name of the project to delete.

    Returns:
        Success or error message.
    """
    return project_store.delete_project(name)