from project_management_agent.memory.memory_manager import memory_manager


class ContextManager:
    """
    Builds conversation context from the current session memory.

    This context can be injected into prompts so the AI remembers
    the current project, task, and uploaded document.
    """

    def __init__(self):
        self.memory = memory_manager

    def build_context(self) -> str:
        """
        Build a formatted context string from session memory.
        """

        context = []

        current_project = self.memory.get_current_project()
        if current_project:
            context.append(f"Current Project: {current_project}")

        current_task = self.memory.get_current_task()
        if current_task:
            context.append(f"Current Task: {current_task}")

        last_document = self.memory.get_last_uploaded_document()
        if last_document:
            context.append(f"Last Uploaded Document: {last_document}")

        if not context:
            return "No active session context."

        return "\n".join(context)

    def has_context(self) -> bool:
        """
        Check whether any session context exists.
        """
        return bool(self.memory.get_all())

    def clear_context(self) -> None:
        """
        Clear the current session context.
        """
        self.memory.clear_all()


context_manager = ContextManager()