from project_management_agent.services.task_store import task_store


def delete_task(title: str) -> str:
    """
    Delete an existing task.
    """

    return task_store.delete_task(title)