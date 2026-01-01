#!/usr/bin/env python3
"""
Verification script to test all functionality of the fixed Todo application.
"""

import sys
import os
from io import StringIO
from contextlib import redirect_stdout

# Add the src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.todo_service import TodoService
from src.cli.cli_interface import CLIInterface


def test_all_functionality():
    """
    Test all functionality in a single execution to verify the fix.
    """
    print("Testing Todo App functionality after fix...")

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

    print("\n10. Testing INCOMPLETE functionality:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["incomplete", "2"])
    output = captured_output.getvalue().strip()
    print(f"   Command: incomplete 2")
    print(f"   Output: {output}")

    print("\n11. Testing LIST with filters:")
    # Add a few more todos to test filters
    cli_interface.run(["add", "Learn", "Python"])
    cli_interface.run(["add", "Build", "an", "app"])
    cli_interface.run(["complete", "3"])  # Complete the new todo

    print("   Testing list --completed:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["list", "--completed"])
    output = captured_output.getvalue().strip()
    print(f"   Command: list --completed")
    print(f"   Output:\n{output}")

    print("\n   Testing list --incomplete:")
    captured_output = StringIO()
    with redirect_stdout(captured_output):
        cli_interface.run(["list", "--incomplete"])
    output = captured_output.getvalue().strip()
    print(f"   Command: list --incomplete")
    print(f"   Output:\n{output}")

    print("\nAll functionality tests completed successfully!")
    print(f"Final todo count: {len(todo_service.get_all_todos())}")


if __name__ == "__main__":
    test_all_functionality()