#!/usr/bin/env python3
"""
Manual test script to demonstrate the menu-based functionality.
This script shows how the menu-based interface works.
"""

import sys
import os

# Add the src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.todo_service import TodoService
from src.main import display_menu, add_todo, view_todos, update_todo, mark_complete, mark_incomplete, delete_todo, get_user_choice


def demo_menu_functionality():
    """
    Demonstrate the menu-based functionality by simulating the service layer.
    """
    print("DEMONSTRATION: Menu-based Todo Application Functionality")
    print("="*60)

    # Initialize the service
    todo_service = TodoService()

    print("\n1. ADDING TODOS:")
    print("-" * 20)
    # Add some todos manually for demonstration
    todo1 = todo_service.create_todo("Buy groceries")
    print(f"Added: {todo1.description} (ID: {todo1.id})")

    todo2 = todo_service.create_todo("Walk the dog")
    print(f"Added: {todo2.description} (ID: {todo2.id})")

    todo3 = todo_service.create_todo("Finish project")
    print(f"Added: {todo3.description} (ID: {todo3.id})")

    print(f"\nTotal todos: {len(todo_service.get_all_todos())}")

    print("\n2. VIEWING TODOS:")
    print("-" * 20)
    view_todos(todo_service)

    print("\n3. UPDATING A TODO:")
    print("-" * 20)
    print("Updating 'Walk the dog' to 'Walk the cat'")
    updated_todo = todo_service.update_todo(2, "Walk the cat")
    if updated_todo:
        print(f"Updated todo ID {updated_todo.id} to: {updated_todo.description}")

    print("\n4. VIEWING UPDATED TODOS:")
    print("-" * 20)
    view_todos(todo_service)

    print("\n5. MARKING A TODO AS COMPLETE:")
    print("-" * 30)
    print("Marking 'Buy groceries' as complete")
    if todo_service.mark_complete(1):
        print("Todo ID 1 marked as complete")

    print("\n6. VIEWING TODOS WITH COMPLETED STATUS:")
    print("-" * 40)
    view_todos(todo_service)

    print("\n7. MARKING A TODO AS INCOMPLETE:")
    print("-" * 30)
    print("Marking 'Finish project' as incomplete")
    if todo_service.mark_incomplete(3):
        print("Todo ID 3 marked as incomplete")

    print("\n8. FINAL VIEW:")
    print("-" * 15)
    view_todos(todo_service)

    print("\n9. DELETING A TODO:")
    print("-" * 20)
    print("Deleting 'Walk the cat' (ID 2)")
    if todo_service.delete_todo(2):
        print("Todo ID 2 deleted successfully")

    print("\n10. FINAL STATE:")
    print("-" * 18)
    view_todos(todo_service)

    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETE")
    print("All menu options would work as expected in the interactive menu.")
    print("The application maintains state within a single session.")
    print("="*60)


if __name__ == "__main__":
    demo_menu_functionality()