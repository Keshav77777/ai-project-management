import sqlite3
from pathlib import Path

from project_management_agent.models.project import Project


class DatabaseManager:
    """
    Handles all SQLite database operations.
    """

    def __init__(self):
        self.db_path = Path(__file__).parent / "projects.db"
        self.initialize_database()
    def initialize_database(self):
        """
        Create the database and projects table if they don't exist.
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id TEXT PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    description TEXT,
                    created_at TEXT
                )
            """)

            conn.commit()
    def create_project(self, project: Project) -> str:
        """
        Save a project to the database.

        Args:
            project: Project object to save.

        Returns:
            Success or error message.
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
        Retrieve all projects from the database.
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM projects")

            rows = cursor.fetchall()

            projects = []

            for row in rows:
                projects.append(
                    Project(
                        id=row[0],
                        name=row[1],
                        description=row[2],
                        created_at=row[3],
                    )
                )

            return projects
        

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
        

database_manager = DatabaseManager()