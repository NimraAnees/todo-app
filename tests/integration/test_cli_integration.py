import pytest
import sys
from io import StringIO
from contextlib import redirect_stdout
from src.services.todo_service import TodoService
from src.cli.cli_interface import CLIInterface


class TestCLIIntegration:
    """
    Integration tests for the CLI interface.
    """

    def test_add_todo_command(self):
        """Test the add command through CLI."""
        service = TodoService()
        cli = CLIInterface(service)

        # Capture stdout to check the output
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["add", "Buy", "groceries"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "Todo added successfully with ID 1" in output
        assert len(service.get_all_todos()) == 1
        assert service.get_all_todos()[0].description == "Buy groceries"

    def test_list_todos_command_empty(self):
        """Test the list command when there are no todos."""
        service = TodoService()
        cli = CLIInterface(service)

        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["list"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "No todos found" in output

    def test_list_todos_command_with_items(self):
        """Test the list command when there are todos."""
        service = TodoService()
        cli = CLIInterface(service)

        # Add some todos first
        service.create_todo("Buy groceries")
        service.create_todo("Walk the dog")

        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["list"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "[1] Buy groceries - Incomplete" in output
        assert "[2] Walk the dog - Incomplete" in output

    def test_complete_todo_command(self):
        """Test the complete command."""
        service = TodoService()
        cli = CLIInterface(service)

        # Add a todo first
        service.create_todo("Buy groceries")

        # Mark it as complete
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["complete", "1"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "Todo 1 marked as complete successfully" in output

        # Verify the todo is marked as complete
        todo = service.get_todo_by_id(1)
        assert todo is not None
        assert todo.completed is True

    def test_complete_todo_command_not_found(self):
        """Test the complete command with non-existent ID."""
        service = TodoService()
        cli = CLIInterface(service)

        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["complete", "999"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0  # CLI doesn't exit with error code for business logic errors
        assert "Error: Todo with ID 999 does not exist" in output

    def test_incomplete_todo_command(self):
        """Test the incomplete command."""
        service = TodoService()
        cli = CLIInterface(service)

        # Add and complete a todo first
        service.create_todo("Buy groceries")
        service.mark_complete(1)

        # Mark it as incomplete
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["incomplete", "1"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "Todo 1 marked as incomplete successfully" in output

        # Verify the todo is marked as incomplete
        todo = service.get_todo_by_id(1)
        assert todo is not None
        assert todo.completed is False

    def test_update_todo_command(self):
        """Test the update command."""
        service = TodoService()
        cli = CLIInterface(service)

        # Add a todo first
        service.create_todo("Old description")

        # Update the todo
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["update", "1", "New", "description"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "Todo 1 updated successfully" in output

        # Verify the todo description was updated
        todo = service.get_todo_by_id(1)
        assert todo is not None
        assert todo.description == "New description"

    def test_delete_todo_command(self):
        """Test the delete command."""
        service = TodoService()
        cli = CLIInterface(service)

        # Add a todo first
        service.create_todo("Buy groceries")

        # Delete the todo
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["delete", "1"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "Todo 1 deleted successfully" in output

        # Verify the todo was deleted
        assert service.get_todo_by_id(1) is None
        assert len(service.get_all_todos()) == 0

    def test_list_completed_filter(self):
        """Test the list command with completed filter."""
        service = TodoService()
        cli = CLIInterface(service)

        # Add todos and mark some as complete
        service.create_todo("Incomplete todo")
        service.create_todo("Complete todo")
        service.mark_complete(2)

        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["list", "--completed"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "[2] Complete todo - Complete" in output
        assert "[1] Incomplete todo - Incomplete" not in output

    def test_list_incomplete_filter(self):
        """Test the list command with incomplete filter."""
        service = TodoService()
        cli = CLIInterface(service)

        # Add todos and mark some as complete
        service.create_todo("Incomplete todo")
        service.create_todo("Complete todo")
        service.mark_complete(2)

        captured_output = StringIO()
        with redirect_stdout(captured_output):
            exit_code = cli.run(["list", "--incomplete"])

        output = captured_output.getvalue().strip()
        assert exit_code == 0
        assert "[1] Incomplete todo - Incomplete" in output
        assert "[2] Complete todo - Complete" not in output

    def test_invalid_command(self):
        """Test CLI with an invalid command."""
        service = TodoService()
        cli = CLIInterface(service)

        captured_output = StringIO()
        with redirect_stdout(captured_output):
            # Using a non-existent command
            exit_code = cli.run(["invalidcommand"])

        output = captured_output.getvalue().strip()
        assert exit_code == 1  # Should return error code for invalid command