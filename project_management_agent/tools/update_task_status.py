from project_management_agent.services.task_store import task_store


def update_task_status(title: str, status: str) -> str:
    """
    Update the status of an existing task.

    Args:
        title: Title of the task.
        status: New status for the task.

    Returns:
        Success or error message.
    """

    return task_store.update_task_status(
        title=title,
        status=status,
    )