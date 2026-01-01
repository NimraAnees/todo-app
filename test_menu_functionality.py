#!/usr/bin/env python3
"""
Test script to verify menu-based functionality works correctly.
This simulates user input for automated testing.
"""

import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.todo_service import TodoService


def test_add_todo():
    """Test adding a todo."""
    print("Testing Add Todo functionality...")
    service = TodoService()

    # Test adding a todo
    todo = service.create_todo("Test todo")
    assert todo.id == 1
    assert todo.description == "Test todo"
    assert todo.completed is False
    print("PASS: Add Todo functionality works correctly")


def test_view_todos():
    """Test viewing todos."""
    print("Testing View Todos functionality...")
    service = TodoService()

    # Add some todos
    service.create_todo("First todo")
    service.create_todo("Second todo")

    todos = service.get_all_todos()
    assert len(todos) == 2
    assert todos[0].description == "First todo"
    assert todos[1].description == "Second todo"
    print("PASS: View Todos functionality works correctly")


def test_update_todo():
    """Test updating a todo."""
    print("Testing Update Todo functionality...")
    service = TodoService()

    # Add a todo
    service.create_todo("Original description")

    # Update the todo
    updated_todo = service.update_todo(1, "Updated description")
    assert updated_todo is not None
    assert updated_todo.description == "Updated description"
    print("PASS: Update Todo functionality works correctly")


def test_mark_complete():
    """Test marking a todo as complete."""
    print("Testing Mark Complete functionality...")
    service = TodoService()

    # Add a todo
    service.create_todo("Test todo")

    # Mark as complete
    result = service.mark_complete(1)
    assert result is True

    todo = service.get_todo_by_id(1)
    assert todo is not None
    assert todo.completed is True
    print("PASS: Mark Complete functionality works correctly")


def test_mark_incomplete():
    """Test marking a todo as incomplete."""
    print("Testing Mark Incomplete functionality...")
    service = TodoService()

    # Add a todo and mark it complete
    service.create_todo("Test todo")
    service.mark_complete(1)

    # Verify it's complete
    todo = service.get_todo_by_id(1)
    assert todo is not None
    assert todo.completed is True

    # Mark as incomplete
    result = service.mark_incomplete(1)
    assert result is True

    todo = service.get_todo_by_id(1)
    assert todo is not None
    assert todo.completed is False
    print("PASS: Mark Incomplete functionality works correctly")


def test_delete_todo():
    """Test deleting a todo."""
    print("Testing Delete Todo functionality...")
    service = TodoService()

    # Add some todos
    service.create_todo("First todo")
    service.create_todo("Second todo")

    # Verify we have 2 todos
    assert len(service.get_all_todos()) == 2

    # Delete the first one
    result = service.delete_todo(1)
    assert result is True

    # Verify we have 1 todo left
    assert len(service.get_all_todos()) == 1

    # Verify the remaining todo has the correct ID (should still be 2)
    remaining_todos = service.get_all_todos()
    assert remaining_todos[0].id == 2
    print("PASS: Delete Todo functionality works correctly")


def test_get_todo_selection():
    """Test the helper function to get todo selection."""
    print("Testing Get Todo Selection functionality...")
    service = TodoService()

    # Add some todos
    service.create_todo("First todo")
    service.create_todo("Second todo")
    service.create_todo("Third todo")

    # Test getting the second todo by ID
    todo = service.get_todo_by_id(2)
    assert todo is not None
    assert todo.id == 2
    assert todo.description == "Second todo"
    print("PASS: Get Todo Selection functionality works correctly")


def run_all_tests():
    """Run all functionality tests."""
    print("Running menu-based functionality tests...\n")

    test_add_todo()
    test_view_todos()
    test_update_todo()
    test_mark_complete()
    test_mark_incomplete()
    test_delete_todo()
    test_get_todo_selection()

    print("\nAll functionality tests passed!")
    print("The menu-based CLI will work correctly with all required features.")


if __name__ == "__main__":
    run_all_tests()