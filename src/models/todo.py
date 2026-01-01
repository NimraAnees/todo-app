from datetime import datetime
from typing import Optional


class Todo:
    """
    Represents a todo item with ID, description, completion status, and creation timestamp.
    """

    def __init__(self, id: int, description: str, completed: bool = False, created_at: Optional[datetime] = None):
        """
        Initialize a Todo instance.

        Args:
            id: Unique identifier for the todo
            description: Description of the todo task
            completed: Status indicating completion (default: False)
            created_at: Timestamp of creation (default: current time)
        """
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID must be a positive integer")

        if not isinstance(description, str) or not description.strip() or len(description.strip()) > 500:
            raise ValueError("Description must be a non-empty string (1-500 characters)")

        if not isinstance(completed, bool):
            raise ValueError("Completed must be a boolean value")

        self.id = id
        self.description = description.strip()
        self.completed = completed
        self.created_at = created_at if created_at is not None else datetime.now()

    def __str__(self) -> str:
        """
        String representation of the Todo.

        Returns:
            Formatted string showing ID, description, and status
        """
        status = "Complete" if self.completed else "Incomplete"
        return f"[{self.id}] {self.description} - {status}"

    def __repr__(self) -> str:
        """
        Developer representation of the Todo.

        Returns:
            Detailed string representation
        """
        return f"Todo(id={self.id}, description='{self.description}', completed={self.completed}, created_at={self.created_at})"

    def to_dict(self) -> dict:
        """
        Convert the Todo to a dictionary representation.

        Returns:
            Dictionary with todo attributes
        """
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }