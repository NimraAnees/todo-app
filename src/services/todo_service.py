from typing import List, Optional
from datetime import datetime

# Handle imports based on execution context
import sys
import os

# Add the parent directory to the path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.models.todo import Todo
except ImportError:
    # If the above fails, try direct import
    try:
        from models.todo import Todo
    except ImportError:
        # If both fail, try relative import
        from ..models.todo import Todo


class TodoService:
    """
    Service class to handle all todo-related operations.
    Manages in-memory storage of todos with CRUD operations.
    """

    def __init__(self):
        """
        Initialize the TodoService with an empty list of todos and next ID tracker.
        """
        self.todos: List[Todo] = []
        self.next_id: int = 1

    def create_todo(self, description: str) -> Todo:
        """
        Create a new todo with the provided description.

        Args:
            description: Description of the todo task

        Returns:
            Created Todo instance

        Raises:
            ValueError: If description is empty or exceeds 500 characters
        """
        if not isinstance(description, str) or not description.strip() or len(description.strip()) > 500:
            raise ValueError("Description must be a non-empty string (1-500 characters)")

        todo = Todo(
            id=self.next_id,
            description=description.strip()
        )
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in the system.

        Returns:
            List of all Todo instances
        """
        return self.todos.copy()

    def get_todo_by_id(self, id: int) -> Optional[Todo]:
        """
        Get a specific todo by its ID.

        Args:
            id: ID of the todo to retrieve

        Returns:
            Todo instance if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == id:
                return todo
        return None

    def update_todo(self, id: int, description: str) -> Optional[Todo]:
        """
        Update the description of an existing todo.

        Args:
            id: ID of the todo to update
            description: New description for the todo

        Returns:
            Updated Todo instance if found, None otherwise

        Raises:
            ValueError: If description is empty or exceeds 500 characters
        """
        if not isinstance(description, str) or not description.strip() or len(description.strip()) > 500:
            raise ValueError("Description must be a non-empty string (1-500 characters)")

        todo = self.get_todo_by_id(id)
        if todo:
            todo.description = description.strip()
            return todo
        return None

    def mark_complete(self, id: int) -> bool:
        """
        Mark a todo as complete.

        Args:
            id: ID of the todo to mark as complete

        Returns:
            True if todo was found and updated, False otherwise
        """
        todo = self.get_todo_by_id(id)
        if todo:
            todo.completed = True
            return True
        return False

    def mark_incomplete(self, id: int) -> bool:
        """
        Mark a todo as incomplete.

        Args:
            id: ID of the todo to mark as incomplete

        Returns:
            True if todo was found and updated, False otherwise
        """
        todo = self.get_todo_by_id(id)
        if todo:
            todo.completed = False
            return True
        return False

    def delete_todo(self, id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            id: ID of the todo to delete

        Returns:
            True if todo was found and deleted, False otherwise
        """
        for i, todo in enumerate(self.todos):
            if todo.id == id:
                del self.todos[i]
                return True
        return False

    def get_todos_by_status(self, completed: bool) -> List[Todo]:
        """
        Get todos filtered by completion status.

        Args:
            completed: Status to filter by (True for completed, False for incomplete)

        Returns:
            List of Todo instances with the specified status
        """
        return [todo for todo in self.todos if todo.completed == completed]