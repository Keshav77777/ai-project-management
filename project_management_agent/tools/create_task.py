from project_management_agent.services.task_store import task_store


def create_task(
    project_name: str,
    title: str,
    description: str = "",
    status: str = "Pending",
    priority: str = "Medium",
) -> str:
    """
    Creates a new task for a project.

    Args:
        project_name: Name of the project.
        title: Title of the task.
        description: Task description.
        status: Task status.
        priority: Task priority.

    Returns:
        Success or error message.
    """

    return task_store.create_task(
        project_name=project_name,
        title=title,
        description=description,
        status=status,
        priority=priority,
    )