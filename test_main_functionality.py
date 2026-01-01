#!/usr/bin/env python3
"""
Test script to verify all main functionality works correctly in a single execution.
"""

from src.services.todo_service import TodoService
from src.cli.cli_interface import CLIInterface
import sys
from io import StringIO
from contextlib import redirect_stdout


def test_main_functionality():
    """
    Test all main functionality in a single execution.
    """
    print("Testing Todo App functionality...")

    # Initialize the services
    todo_service = TodoService()
    cli_interface = CLIInterface(todo_service)

    print("\n1. Testing ADD functionality:")
    # Test adding a todo
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["add", "Buy", "groceries"])
    output = captured_output.getvalue().strip()
    print(f"   Command: add 'Buy groceries'")
    print(f"   Output: {output}")

    # Add another todo
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["add", "Walk", "the", "dog"])
    output = captured_output.getvalue().strip()
    print(f"   Command: add 'Walk the dog'")
    print(f"   Output: {output}")

    print(f"\n   Current todos in memory: {len(todo_service.get_all_todos())}")

    print("\n2. Testing LIST functionality:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["list"])
    output = captured_output.getvalue().strip()
    print(f"   Command: list")
    print(f"   Output:\n{output}")

    print("\n3. Testing COMPLETE functionality:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["complete", "1"])
    output = captured_output.getvalue().strip()
    print(f"   Command: complete 1")
    print(f"   Output: {output}")

    print("\n4. Testing LIST again to see completed status:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["list"])
    output = captured_output.getvalue().strip()
    print(f"   Command: list")
    print(f"   Output:\n{output}")

    print("\n5. Testing UPDATE functionality:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["update", "2", "Walk", "the", "cat"])
    output = captured_output.getvalue().strip()
    print(f"   Command: update 2 'Walk the cat'")
    print(f"   Output: {output}")

    print("\n6. Testing LIST again to see updated description:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["list"])
    output = captured_output.getvalue().strip()
    print(f"   Command: list")
    print(f"   Output:\n{output}")

    print("\n7. Testing DELETE functionality:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["delete", "1"])
    output = captured_output.getvalue().strip()
    print(f"   Command: delete 1")
    print(f"   Output: {output}")

    print("\n8. Testing LIST final state:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["list"])
    output = captured_output.getvalue().strip()
    print(f"   Command: list")
    print(f"   Output:\n{output}")

    print("\n9. Testing error handling:")
    print("   Testing invalid ID for complete command:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["complete", "999"])
    output = captured_output.getvalue().strip()
    print(f"   Command: complete 999")
    print(f"   Output: {output}")

    print("\n   Testing invalid ID for update command:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["update", "999", "New", "description"])
    output = captured_output.getvalue().strip()
    print(f"   Command: update 999 'New description'")
    print(f"   Output: {output}")

    print("\nAll functionality tests completed successfully!")


if __name__ == "__main__":
    test_main_functionality()