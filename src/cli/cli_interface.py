import argparse
from typing import Optional

# Handle imports based on execution context
import sys
import os

# Add the parent directory to the path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.services.todo_service import TodoService
except ImportError:
    # If the above fails, try direct import
    try:
        from services.todo_service import TodoService
    except ImportError:
        # If both fail, try relative import
        from ..services.todo_service import TodoService


class CLIInterface:
    """
    Command-line interface for the Todo application.
    Handles user input and provides feedback.
    """

    def __init__(self, todo_service: TodoService):
        """
        Initialize the CLI interface with a TodoService.

        Args:
            todo_service: Service to handle todo operations
        """
        self.todo_service = todo_service
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """
        Create and configure the argument parser.

        Returns:
            Configured ArgumentParser instance
        """
        parser = argparse.ArgumentParser(
            description="Todo Application - Manage your tasks from the command line",
            prog="todo"
        )

        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Add command
        add_parser = subparsers.add_parser("add", help="Add a new todo")
        add_parser.add_argument("description", nargs="+", help="Description of the todo")

        # List command
        list_parser = subparsers.add_parser("list", help="List all todos")
        list_parser.add_argument("--completed", action="store_true", help="Show only completed todos")
        list_parser.add_argument("--incomplete", action="store_true", help="Show only incomplete todos")

        # Complete command
        complete_parser = subparsers.add_parser("complete", help="Mark a todo as complete")
        complete_parser.add_argument("id", type=int, help="ID of the todo to mark complete")

        # Incomplete command
        incomplete_parser = subparsers.add_parser("incomplete", help="Mark a todo as incomplete")
        incomplete_parser.add_argument("id", type=int, help="ID of the todo to mark incomplete")

        # Update command
        update_parser = subparsers.add_parser("update", help="Update a todo description")
        update_parser.add_argument("id", type=int, help="ID of the todo to update")
        update_parser.add_argument("description", nargs="+", help="New description for the todo")

        # Delete command
        delete_parser = subparsers.add_parser("delete", help="Delete a todo")
        delete_parser.add_argument("id", type=int, help="ID of the todo to delete")

        return parser

    def run(self, args: Optional[list] = None) -> int:
        """
        Run the CLI interface with the provided arguments.

        Args:
            args: List of arguments to parse (default: sys.argv[1:])

        Returns:
            Exit code (0 for success, 1 for error)
        """
        try:
            parsed_args = self.parser.parse_args(args)

            if not parsed_args.command:
                self.parser.print_help()
                return 0

            # Handle each command
            if parsed_args.command == "add":
                description = " ".join(parsed_args.description)
                self._handle_add(description)
            elif parsed_args.command == "list":
                self._handle_list(parsed_args.completed, parsed_args.incomplete)
            elif parsed_args.command == "complete":
                self._handle_complete(parsed_args.id)
            elif parsed_args.command == "incomplete":
                self._handle_incomplete(parsed_args.id)
            elif parsed_args.command == "update":
                description = " ".join(parsed_args.description)
                self._handle_update(parsed_args.id, description)
            elif parsed_args.command == "delete":
                self._handle_delete(parsed_args.id)

            return 0
        except SystemExit:
            # argparse calls sys.exit on error, so we catch it to return proper exit code
            return 1
        except Exception as e:
            print(f"Error: {str(e)}")
            return 1

    def _handle_add(self, description: str) -> None:
        """
        Handle the add command.

        Args:
            description: Description of the new todo
        """
        try:
            todo = self.todo_service.create_todo(description)
            print(f"Todo added successfully with ID {todo.id}")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def _handle_list(self, completed_only: bool, incomplete_only: bool) -> None:
        """
        Handle the list command.

        Args:
            completed_only: If True, show only completed todos
            incomplete_only: If True, show only incomplete todos
        """
        if completed_only and incomplete_only:
            print("Error: Cannot filter by both completed and incomplete")
            return

        if completed_only:
            todos = self.todo_service.get_todos_by_status(True)
        elif incomplete_only:
            todos = self.todo_service.get_todos_by_status(False)
        else:
            todos = self.todo_service.get_all_todos()

        if not todos:
            print("No todos found")
            return

        for todo in todos:
            status = "Complete" if todo.completed else "Incomplete"
            print(f"[{todo.id}] {todo.description} - {status}")

    def _handle_complete(self, id: int) -> None:
        """
        Handle the complete command.

        Args:
            id: ID of the todo to mark as complete
        """
        if self.todo_service.mark_complete(id):
            print(f"Todo {id} marked as complete successfully")
        else:
            print(f"Error: Todo with ID {id} does not exist")

    def _handle_incomplete(self, id: int) -> None:
        """
        Handle the incomplete command.

        Args:
            id: ID of the todo to mark as incomplete
        """
        if self.todo_service.mark_incomplete(id):
            print(f"Todo {id} marked as incomplete successfully")
        else:
            print(f"Error: Todo with ID {id} does not exist")

    def _handle_update(self, id: int, description: str) -> None:
        """
        Handle the update command.

        Args:
            id: ID of the todo to update
            description: New description for the todo
        """
        try:
            todo = self.todo_service.update_todo(id, description)
            if todo:
                print(f"Todo {id} updated successfully")
            else:
                print(f"Error: Todo with ID {id} does not exist")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def _handle_delete(self, id: int) -> None:
        """
        Handle the delete command.

        Args:
            id: ID of the todo to delete
        """
        if self.todo_service.delete_todo(id):
            print(f"Todo {id} deleted successfully")
        else:
            print(f"Error: Todo with ID {id} does not exist")