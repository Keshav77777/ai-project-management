from project_management_agent.memory.memory_manager import memory_manager
from project_management_agent.services.task_store import task_store


def create_task(
    title: str,
    project_name: str | None = None,
    description: str = "",
    status: str = "Pending",
    priority: str = "Medium",
) -> str:
    """
    Creates a new task for a project.

    Args:
        title: Title of the task.
        project_name: Name of the project. If omitted, uses the current project from memory.
        description: Task description.
        status: Task status.
        priority: Task priority.

    Returns:
        Success or error message.
    """

    if not project_name:
        project_name = memory_manager.get_current_project()

    if not project_name:
        return "No active project found. Please specify a project name."

    result = task_store.create_task(
        project_name=project_name,
        title=title,
        description=description,
        status=status,
        priority=priority,
    )

    if result.startswith("Task"):
        memory_manager.set_current_task(title)

    return result