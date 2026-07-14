from project_management_agent.models.project import Project

class ProjectStore:
    """
    A simple in-memory store for projects.

    This is temporary. In Module 4 we'll replace it
    with a database (SQLite).
    """

    def __init__(self):
        self.projects: dict[str, Project] = {}
    
    def create_project(self,name: str,description: str = "",) -> str:
        """
        Create a new project.

        Args:
            name: Name of the project.
            description: Short description of the project.

        Returns:
            Success or error message.
        """

        # Check if a project with the same name already exists
        if any(
            project.name.lower() == name.lower()
            for project in self.projects.values()
        ):
            return f"Project '{name}' already exists."

        # Create a new Project object
        project = Project(
            name=name,
            description=description,
        )

        # Store the project using its ID as the key
        self.projects[project.id] = project

        return f"Project '{name}' created successfully."

    def list_projects(self) -> list[Project]:
        """
        Return all existing projects.

        Returns:
            A list of Project objects.
        """

        return list(self.projects.values())

    def delete_project(self, name: str) -> str:
        """
        Delete a project by its name.
        """

        for project_id, project in self.projects.items():
            if project.name.lower() == name.lower():
                del self.projects[project_id]
                return f"Project '{name}' deleted successfully."

        return f"Project '{name}' not found."
    
    def get_project(self, name: str) -> Project | None:
        """
        Retrieve a project by name.
        """
    
        for project in self.projects.values():
            if project.name.casefold() == name.casefold():
                return project
    
        return None


# Singleton instance
project_store = ProjectStore()