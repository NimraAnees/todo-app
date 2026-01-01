import pytest
from src.services.todo_service import TodoService
from src.models.todo import Todo


class TestTodoService:
    """
    Unit tests for the TodoService.
    """

    def test_initial_state(self):
        """Test that TodoService starts with empty todos and ID 1."""
        service = TodoService()

        assert len(service.todos) == 0
        assert service.next_id == 1

    def test_create_todo_success(self):
        """Test successful creation of a todo."""
        service = TodoService()
        todo = service.create_todo("Test description")

        assert len(service.todos) == 1
        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.completed is False
        assert service.next_id == 2

    def test_create_multiple_todos_incremental_ids(self):
        """Test that multiple todos get incremental IDs."""
        service = TodoService()

        todo1 = service.create_todo("First todo")
        todo2 = service.create_todo("Second todo")
        todo3 = service.create_todo("Third todo")

        assert todo1.id == 1
        assert todo2.id == 2
        assert todo3.id == 3
        assert service.next_id == 4

    def test_create_todo_invalid_description_empty(self):
        """Test that creating a todo with empty description raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            service.create_todo("")

    def test_create_todo_invalid_description_whitespace(self):
        """Test that creating a todo with whitespace-only description raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            service.create_todo("   ")

    def test_create_todo_invalid_description_too_long(self):
        """Test that creating a todo with too long description raises ValueError."""
        service = TodoService()
        long_desc = "a" * 501

        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            service.create_todo(long_desc)

    def test_get_all_todos_empty(self):
        """Test getting all todos when the list is empty."""
        service = TodoService()

        todos = service.get_all_todos()

        assert len(todos) == 0

    def test_get_all_todos_with_items(self):
        """Test getting all todos when the list has items."""
        service = TodoService()

        service.create_todo("First todo")
        service.create_todo("Second todo")

        todos = service.get_all_todos()

        assert len(todos) == 2
        assert todos[0].id == 1
        assert todos[0].description == "First todo"
        assert todos[1].id == 2
        assert todos[1].description == "Second todo"

    def test_get_all_todos_returns_copy(self):
        """Test that get_all_todos returns a copy of the internal list."""
        service = TodoService()
        service.create_todo("Test todo")

        todos1 = service.get_all_todos()
        todos2 = service.get_all_todos()

        # Modify the first list
        todos1.append("dummy")

        # The second list should not be affected
        assert len(todos2) == 1

    def test_get_todo_by_id_found(self):
        """Test getting a todo by ID when it exists."""
        service = TodoService()

        service.create_todo("Test todo")
        todo = service.create_todo("Another todo")

        found_todo = service.get_todo_by_id(2)

        assert found_todo is not None
        assert found_todo.id == 2
        assert found_todo.description == "Another todo"

    def test_get_todo_by_id_not_found(self):
        """Test getting a todo by ID when it doesn't exist."""
        service = TodoService()

        service.create_todo("Test todo")

        found_todo = service.get_todo_by_id(5)

        assert found_todo is None

    def test_get_todo_by_id_with_negative_id(self):
        """Test getting a todo by negative ID."""
        service = TodoService()

        service.create_todo("Test todo")

        found_todo = service.get_todo_by_id(-1)

        assert found_todo is None

    def test_update_todo_success(self):
        """Test successfully updating a todo description."""
        service = TodoService()

        service.create_todo("Original description")
        updated_todo = service.update_todo(1, "Updated description")

        assert updated_todo is not None
        assert updated_todo.id == 1
        assert updated_todo.description == "Updated description"
        # Ensure the original todo in the list was updated
        assert service.todos[0].description == "Updated description"

    def test_update_todo_not_found(self):
        """Test updating a todo that doesn't exist."""
        service = TodoService()

        service.create_todo("Test todo")
        result = service.update_todo(5, "Updated description")

        assert result is None

    def test_update_todo_invalid_description_empty(self):
        """Test updating a todo with empty description raises ValueError."""
        service = TodoService()

        service.create_todo("Original description")

        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            service.update_todo(1, "")

    def test_update_todo_invalid_description_too_long(self):
        """Test updating a todo with too long description raises ValueError."""
        service = TodoService()

        service.create_todo("Original description")
        long_desc = "a" * 501

        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            service.update_todo(1, long_desc)

    def test_mark_complete_success(self):
        """Test successfully marking a todo as complete."""
        service = TodoService()

        service.create_todo("Test todo")
        result = service.mark_complete(1)

        assert result is True
        assert service.todos[0].completed is True

    def test_mark_complete_not_found(self):
        """Test marking a todo as complete when it doesn't exist."""
        service = TodoService()

        service.create_todo("Test todo")
        result = service.mark_complete(5)

        assert result is False

    def test_mark_incomplete_success(self):
        """Test successfully marking a todo as incomplete."""
        service = TodoService()

        service.create_todo("Test todo")
        # First mark it complete
        service.mark_complete(1)
        # Then mark it incomplete
        result = service.mark_incomplete(1)

        assert result is True
        assert service.todos[0].completed is False

    def test_mark_incomplete_not_found(self):
        """Test marking a todo as incomplete when it doesn't exist."""
        service = TodoService()

        service.create_todo("Test todo")
        result = service.mark_incomplete(5)

        assert result is False

    def test_delete_todo_success(self):
        """Test successfully deleting a todo."""
        service = TodoService()

        service.create_todo("First todo")
        service.create_todo("Second todo")
        result = service.delete_todo(1)

        assert result is True
        assert len(service.todos) == 1
        assert service.todos[0].id == 2  # The second todo should now be at index 0

    def test_delete_todo_not_found(self):
        """Test deleting a todo that doesn't exist."""
        service = TodoService()

        service.create_todo("Test todo")
        result = service.delete_todo(5)

        assert result is False
        assert len(service.todos) == 1

    def test_get_todos_by_status(self):
        """Test getting todos by completion status."""
        service = TodoService()

        service.create_todo("Incomplete todo 1")
        service.create_todo("Incomplete todo 2")
        service.create_todo("Complete todo")

        # Mark the third todo as complete
        service.mark_complete(3)

        completed_todos = service.get_todos_by_status(True)
        incomplete_todos = service.get_todos_by_status(False)

        assert len(completed_todos) == 1
        assert completed_todos[0].id == 3

        assert len(incomplete_todos) == 2
        assert incomplete_todos[0].id == 1
        assert incomplete_todos[1].id == 2