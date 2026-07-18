from project_management_agent.services.task_store import task_store


def list_tasks(project_name: str | None = None):
    tasks = task_store.list_tasks(project_name)

    if not tasks:
        return "No tasks found."

    result = []

    for i, task in enumerate(tasks, start=1):
        result.append(
            f"{i}. {task.title}\n"
            f"   Status: {task.status}\n"
            f"   Priority: {task.priority}"
        )

    return "\n\n".join(result)