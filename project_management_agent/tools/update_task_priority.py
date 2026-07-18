from project_management_agent.services.task_store import task_store


def update_task_priority(
    title: str,
    priority: str,
) -> str:
    """
    Update the priority of an existing task.
    """

    return task_store.update_task_priority(
        title=title,
        priority=priority,
    )