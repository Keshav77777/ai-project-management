from project_management_agent.memory.memory_manager import memory_manager
from project_management_agent.services.task_store import task_store


def delete_task(title: str) -> str:
    """
    Delete an existing task.

    Args:
        title: Title of the task.

    Returns:
        Success or error message.
    """

    result = task_store.delete_task(title)

    # Clear the current task from memory if it was deleted.
    if result.startswith("Task deleted"):
        if memory_manager.get_current_task() == title:
            memory_manager.clear_current_task()

    return result