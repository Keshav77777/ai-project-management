from project_management_agent.database.database import database_manager
from project_management_agent.models.project import Project


class ProjectStore:
    """
    Service layer for project operations.

    Delegates persistence to the DatabaseManager.
    """

    def __init__(self):
        pass

    def create_project(
        self,
        name: str,
        description: str = "",
    ) -> str:

        project = Project(
            name=name,
            description=description,
        )
        print(project)

        return database_manager.create_project(project)

    def list_projects(self) -> list[Project]:
        return database_manager.list_projects()

    def delete_project(self, name: str) -> str:
        return database_manager.delete_project(name)


project_store = ProjectStore()