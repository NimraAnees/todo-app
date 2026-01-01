import pytest
from datetime import datetime
from src.models.todo import Todo


class TestTodo:
    """
    Unit tests for the Todo model.
    """

    def test_create_todo_success(self):
        """Test successful creation of a Todo with valid parameters."""
        todo = Todo(id=1, description="Test description")

        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.completed is False
        assert isinstance(todo.created_at, datetime)

    def test_create_todo_with_completion_status(self):
        """Test creating a Todo with completion status set to True."""
        todo = Todo(id=1, description="Test description", completed=True)

        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.completed is True

    def test_create_todo_with_custom_timestamp(self):
        """Test creating a Todo with a custom creation timestamp."""
        custom_time = datetime(2023, 1, 1)
        todo = Todo(id=1, description="Test description", created_at=custom_time)

        assert todo.created_at == custom_time

    def test_create_todo_auto_timestamp(self):
        """Test that Todo gets current timestamp when none provided."""
        before_creation = datetime.now()
        todo = Todo(id=1, description="Test description")
        after_creation = datetime.now()

        assert before_creation <= todo.created_at <= after_creation

    def test_create_todo_invalid_id_negative(self):
        """Test that creating a Todo with negative ID raises ValueError."""
        with pytest.raises(ValueError, match="ID must be a positive integer"):
            Todo(id=-1, description="Test description")

    def test_create_todo_invalid_id_zero(self):
        """Test that creating a Todo with zero ID raises ValueError."""
        with pytest.raises(ValueError, match="ID must be a positive integer"):
            Todo(id=0, description="Test description")

    def test_create_todo_invalid_id_non_integer(self):
        """Test that creating a Todo with non-integer ID raises TypeError."""
        with pytest.raises(TypeError):
            Todo(id="invalid", description="Test description")

    def test_create_todo_empty_description(self):
        """Test that creating a Todo with empty description raises ValueError."""
        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            Todo(id=1, description="")

    def test_create_todo_whitespace_description(self):
        """Test that creating a Todo with whitespace-only description raises ValueError."""
        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            Todo(id=1, description="   ")

    def test_create_todo_long_description(self):
        """Test that creating a Todo with too long description raises ValueError."""
        long_desc = "a" * 501  # 501 characters, exceeding 500 limit
        with pytest.raises(ValueError, match="Description must be a non-empty string"):
            Todo(id=1, description=long_desc)

    def test_create_todo_valid_max_length_description(self):
        """Test that creating a Todo with exactly 500 char description works."""
        desc_500 = "a" * 500
        todo = Todo(id=1, description=desc_500)
        assert todo.description == desc_500

    def test_create_todo_invalid_completed_type(self):
        """Test that creating a Todo with non-boolean completed raises ValueError."""
        with pytest.raises(ValueError, match="Completed must be a boolean value"):
            Todo(id=1, description="Test description", completed="true")

    def test_todo_str_representation(self):
        """Test string representation of Todo."""
        todo = Todo(id=1, description="Test description", completed=False)
        expected = "[1] Test description - Incomplete"
        assert str(todo) == expected

    def test_todo_str_representation_completed(self):
        """Test string representation of completed Todo."""
        todo = Todo(id=1, description="Test description", completed=True)
        expected = "[1] Test description - Complete"
        assert str(todo) == expected

    def test_todo_repr_representation(self):
        """Test developer representation of Todo."""
        todo = Todo(id=1, description="Test description", completed=True)
        repr_str = repr(todo)
        assert "Todo(id=1, description='Test description', completed=True" in repr_str

    def test_todo_to_dict(self):
        """Test conversion of Todo to dictionary."""
        custom_time = datetime(2023, 1, 1, 12, 0, 0)
        todo = Todo(id=1, description="Test description", completed=True, created_at=custom_time)

        expected_dict = {
            "id": 1,
            "description": "Test description",
            "completed": True,
            "created_at": "2023-01-01T12:00:00"
        }

        result_dict = todo.to_dict()
        assert result_dict == expected_dict

    def test_description_stripped(self):
        """Test that description is automatically stripped of leading/trailing whitespace."""
        todo = Todo(id=1, description="  Test description with spaces  ")
        assert todo.description == "Test description with spaces"