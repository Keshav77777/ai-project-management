from project_management_agent.memory.memory_manager import memory_manager
from project_management_agent.services.task_store import task_store


def update_task_priority(title: str, priority: str) -> str:
    """
    Update the priority of an existing task.

    Args:
        title: Title of the task.
        priority: New priority.

    Returns:
        Success or error message.
    """

    result = task_store.update_task_priority(
        title=title,
        priority=priority,
    )

    # Update memory only if the task was updated successfully.
    if result.startswith("Task updated"):
        memory_manager.set_current_task(title)

    return result