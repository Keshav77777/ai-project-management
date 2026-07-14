from project_management_agent.services.project_store import project_store

def create_project(name: str) -> str:
    """
    Creates a new project.

    Args:
        name: Name of the project.

    Returns:
        Success or error message.
    """
    return project_store.create_project(name)