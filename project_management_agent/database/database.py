import sqlite3
from pathlib import Path

from project_management_agent.models.project import Project
from project_management_agent.models.task import Task


class DatabaseManager:
    """
    Handles all SQLite database operations.
    """

    def __init__(self):
        self.db_path = Path(__file__).parent / "projects.db"
        self.initialize_database()

    def initialize_database(self):
        """
        Initialize the SQLite database.

        Creates the required tables if they do not already exist.
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("PRAGMA foreign_keys = ON")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id TEXT PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    description TEXT,
                    created_at TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    project_id TEXT NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    created_at TEXT,

                    FOREIGN KEY(project_id)
                        REFERENCES projects(id)
                        ON DELETE CASCADE
                )
            """)

            conn.commit()

    # ------------------------------------------------------------------
    # Helper Methods
    # ------------------------------------------------------------------

    def _row_to_project(self, row: tuple) -> Project:
        """
        Convert a database row into a Project object.
        """

        return Project(
            id=row[0],
            name=row[1],
            description=row[2],
            created_at=row[3],
        )
    
    def _row_to_task(self, row: tuple) -> Task:
        """
        Convert a database row into a Task object.
        """ 
        return Task(
            id=row[0],
            project_id=row[1],
            title=row[2],
            description=row[3],
            status=row[4],
            priority=row[5],
            created_at=row[6],
        )

    # ------------------------------------------------------------------
    # Project Operations
    # ------------------------------------------------------------------

    def create_project(self, project: Project) -> str:
        """
        Save a project to the database.
        """

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                cursor.execute(
                    """
                    INSERT INTO projects
                    (id, name, description, created_at)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        project.id,
                        project.name,
                        project.description,
                        project.created_at,
                    ),
                )

                conn.commit()

            return f"Project '{project.name}' created successfully."

        except sqlite3.IntegrityError:
            return f"Project '{project.name}' already exists."

    def list_projects(self) -> list[Project]:
        """
        Retrieve all projects.
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM projects")

            rows = cursor.fetchall()

            return [self._row_to_project(row) for row in rows]

    def get_project_by_name(self, name: str) -> Project | None:
        """
        Retrieve a project by its name.
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM projects
                WHERE name = ?
                """,
                (name,),
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return self._row_to_project(row)

    def delete_project(self, name: str) -> str:
        """
        Delete a project by name.
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM projects
                WHERE name = ?
                """,
                (name,),
            )

            conn.commit()

            if cursor.rowcount == 0:
                return f"Project '{name}' not found."

            return f"Project '{name}' deleted successfully."

    # ------------------------------------------------------------------
    # Task Operations
    # ------------------------------------------------------------------

    def create_task(self, task: Task) -> str:
        """
        Save a task to the database.
        """

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                cursor.execute("PRAGMA foreign_keys = ON")

                cursor.execute(
                    """
                    INSERT INTO tasks
                    (id, project_id, title, description,
                     status, priority, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        task.id,
                        task.project_id,
                        task.title,
                        task.description,
                        task.status,
                        task.priority,
                        task.created_at,
                    ),
                )

                conn.commit()

            return f"Task '{task.title}' created successfully."

        except sqlite3.IntegrityError:
            return f"Unable to create task '{task.title}'."
    
    def list_tasks(self, project_id: str | None = None) -> list[Task]:
        """
        Retrieve tasks.
    
        If project_id is provided, return only tasks for that project.
        Otherwise return all tasks.
        """
    
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
    
            if project_id is None:
                cursor.execute("SELECT * FROM tasks")
            else:
                cursor.execute(
                    """
                    SELECT * FROM tasks
                    WHERE project_id = ?
                    """,
                    (project_id,),
                )
    
            rows = cursor.fetchall()
    
            return [self._row_to_task(row) for row in rows]
    
    def update_task_status(self, title: str, status: str) -> str:
        """
        Update the status of a task.
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE tasks
                SET status = ?
                WHERE title = ?
                """,
                (status, title),
            )

            conn.commit()

            if cursor.rowcount == 0:
                return f"Task '{title}' not found."

            return f"Task '{title}' status updated successfully."
        
    def delete_task(self, title: str) -> str:
        """
        Delete a task by title.
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM tasks
                WHERE title = ?
                """,
                (title,),
            )

            conn.commit()

            if cursor.rowcount == 0:
                return f"Task '{title}' not found."

            return f"Task '{title}' deleted successfully."
        
    def update_task_priority(self, title: str, priority: str) -> str:
        """
        Update the priority of a task.
        """
    
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
    
            cursor.execute(
                """
                UPDATE tasks
                SET priority = ?
                WHERE title = ?
                """,
                (priority, title),
            )
    
            conn.commit()
    
            if cursor.rowcount == 0:
                return f"Task '{title}' not found."
    
            return f"Task '{title}' priority updated successfully."

database_manager = DatabaseManager()