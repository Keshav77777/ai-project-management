from project_management_agent.services.project_store import project_store


def list_projects():
    """
    Return all existing projects.

    Returns:
        A list of existing projects or a message if no projects exist.
    """
    return project_store.list_projects()