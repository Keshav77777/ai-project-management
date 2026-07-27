from project_management_agent.database.database import database_manager
from project_management_agent.models.task import Task

class TaskStore:
    """
    Service layer for Task operations.

    Delegates persistence to the DatabaseManager.
    """
    VALID_STATUSES = {
    "Pending",
    "In Progress",
    "Completed",
    }
    VALID_PRIORITIES = {
    "Low",
    "Medium",
    "High",
    }

    def create_task(
        self,
        project_name: str,
        title: str,
        description: str = "",
        status: str = "Pending",
        priority: str = "Medium",
    ) -> str:
        """
        Creates a new task for a project.
        """

        project = database_manager.get_project_by_name(project_name)

        if project is None:
            return f"Project '{project_name}' not found."

        task = Task(
            project_id=project.id,
            title=title,
            description=description,
            status=status,
            priority=priority,
        )

        return database_manager.create_task(task)

    def list_tasks(
        self,
        project_name: str | None = None,
    ) -> list[Task]:
        """
        List tasks.

        If project_name is provided, return tasks only for that project.
        Otherwise return all tasks.
        """

        # User wants all tasks
        if project_name is None:
            return database_manager.list_tasks()

        # Find the project first
        project = database_manager.get_project_by_name(project_name)

        if project is None:
            return []

        # Return only tasks for this project
        return database_manager.list_tasks(project.id)



    def update_task_status(self, title: str, status: str) -> str:
        """
        Update the status of an existing task.
    
        Args:
            title: Title of the task.
            status: New task status.
    
        Returns:
            Success or error message.
        """
    
        status = " ".join(word.capitalize() for word in status.split())
    
        if status not in self.VALID_STATUSES:
            return (
                f"Invalid status '{status}'. "
                f"Valid statuses are: "
                f"{', '.join(sorted(self.VALID_STATUSES))}."
            )
    
        return database_manager.update_task_status(
            title=title,
            status=status,
        )
    
    def delete_task(self, title: str) -> str:
        """
        Delete an existing task.
        """

        return database_manager.delete_task(title)
    def update_task_priority(self, title: str, priority: str) -> str:
        """
        Update the priority of an existing task.
        """
    
        priority = priority.capitalize()
    
        if priority not in self.VALID_PRIORITIES:
            return (
                f"Invalid priority '{priority}'. "
                f"Valid priorities are: "
                f"{', '.join(sorted(self.VALID_PRIORITIES))}."
            )
    
        return database_manager.update_task_priority(
            title=title,
            priority=priority,
        )
task_store = TaskStore()