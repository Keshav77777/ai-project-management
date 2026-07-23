class SessionMemory:
    """
    Stores short-term memory for the current conversation.

    This is an in-memory key-value store that exists only for the
    lifetime of the application.
    """

    def __init__(self):
        self._memory: dict[str, object] = {}

    def set(self, key: str, value: object) -> None:
        """
        Store a value in memory.
        """
        self._memory[key] = value

    def get(self, key: str) -> object | None:
        """
        Retrieve a value from memory.

        Returns None if the key does not exist.
        """
        return self._memory.get(key)

    def delete(self, key: str) -> bool:
        """
        Remove a value from memory.

        Returns True if the key existed.
        """
        if key in self._memory:
            del self._memory[key]
            return True

        return False

    def clear(self) -> None:
        """
        Remove all stored memory.
        """
        self._memory.clear()

    def contains(self, key: str) -> bool:
        """
        Check whether a key exists.
        """
        return key in self._memory

    def get_all(self) -> dict[str, object]:
        """
        Return all stored memory.
        """
        return self._memory.copy()


session_memory = SessionMemory()