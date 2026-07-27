from project_management_agent.services.task_store import task_store


def create_task(
    project_name: str,
    title: str,
    description: str = "",
    status: str = "Pending",
    priority: str = "Medium",
) -> str:
    """
    Create a new task for a project.
    """

    return task_store.create_task(
        project_name=project_name,
        title=title,
        description=description,
        status=status,
        priority=priority,
    )


def list_tasks(project_name: str | None = None) -> str:
    """
    List tasks.

    If project_name is provided, list tasks for that project.
    Otherwise list all tasks.
    """

    tasks = task_store.list_tasks(project_name)

    if not tasks:
        return "No tasks found."

    result = []

    for task in tasks:
        result.append(
            f"""
Title      : {task.title}
Status     : {task.status}
Priority   : {task.priority}
Description: {task.description}
""".strip()
        )

    return "\n\n".join(result)


def update_task_status(
    title: str,
    status: str,
) -> str:
    """
    Update the status of a task.
    """

    return task_store.update_task_status(
        title=title,
        status=status,
    )


def update_task_priority(
    title: str,
    priority: str,
) -> str:
    """
    Update the priority of a task.
    """

    return task_store.update_task_priority(
        title=title,
        priority=priority,
    )


def delete_task(title: str) -> str:
    """
    Delete a task.
    """

    return task_store.delete_task(title)