from project_management_agent.memory.session_memory import session_memory


class MemoryManager:
    """
    High-level interface for managing session memory.

    This class hides the underlying SessionMemory implementation and
    provides business-specific memory operations.
    """

    CURRENT_PROJECT_KEY = "current_project"
    CURRENT_TASK_KEY = "current_task"
    LAST_UPLOADED_DOCUMENT_KEY = "last_uploaded_document"

    def __init__(self):
        self.memory = session_memory

    # --------------------------------------------------
    # Current Project
    # --------------------------------------------------

    def set_current_project(self, project_name: str) -> None:
        """
        Store the currently active project.
        """
        self.memory.set(self.CURRENT_PROJECT_KEY, project_name)

    def get_current_project(self) -> str | None:
        """
        Retrieve the currently active project.
        """
        return self.memory.get(self.CURRENT_PROJECT_KEY)

    def clear_current_project(self) -> None:
        """
        Remove the current project from memory.
        """
        self.memory.delete(self.CURRENT_PROJECT_KEY)

    # --------------------------------------------------
    # Current Task
    # --------------------------------------------------

    def set_current_task(self, task_name: str) -> None:
        """
        Store the currently active task.
        """
        self.memory.set(self.CURRENT_TASK_KEY, task_name)

    def get_current_task(self) -> str | None:
        """
        Retrieve the currently active task.
        """
        return self.memory.get(self.CURRENT_TASK_KEY)

    def clear_current_task(self) -> None:
        """
        Remove the current task from memory.
        """
        self.memory.delete(self.CURRENT_TASK_KEY)

    # --------------------------------------------------
    # Last Uploaded Document
    # --------------------------------------------------

    def set_last_uploaded_document(self, document_name: str) -> None:
        """
        Store the last uploaded document.
        """
        self.memory.set(self.LAST_UPLOADED_DOCUMENT_KEY, document_name)

    def get_last_uploaded_document(self) -> str | None:
        """
        Retrieve the last uploaded document.
        """
        return self.memory.get(self.LAST_UPLOADED_DOCUMENT_KEY)

    def clear_last_uploaded_document(self) -> None:
        """
        Remove the last uploaded document.
        """
        self.memory.delete(self.LAST_UPLOADED_DOCUMENT_KEY)

    # --------------------------------------------------
    # General
    # --------------------------------------------------

    def clear_all(self) -> None:
        """
        Clear all session memory.
        """
        self.memory.clear()

    def get_all(self) -> dict[str, object]:
        """
        Return all stored session memory.
        """
        return self.memory.get_all()


memory_manager = MemoryManager()