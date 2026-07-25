from project_management_agent.services.project_store import project_store


def create_project(
    name: str,
    description: str = "",
) -> str:
    return project_store.create_project(
        name=name,
        description=description,
    )


def list_projects() -> str:
    projects = project_store.list_projects()

    if not projects:
        return "No projects found."

    return "\n".join(
        f"- {project.name}: {project.description}"
        for project in projects
    )


def delete_project(name: str) -> str:
    return project_store.delete_project(name)