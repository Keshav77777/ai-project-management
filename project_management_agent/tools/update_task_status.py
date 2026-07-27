from project_management_agent.memory.memory_manager import memory_manager
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

    result = task_store.update_task_status(
        title=title,
        status=status,
    )

    if result.startswith(f"Task '{title}' status updated"):
        memory_manager.set_current_task(title)

    return result