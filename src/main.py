#!/usr/bin/env python3
"""
Main entry point for the Todo Application.
Menu-based CLI interface for managing todos in memory.
"""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.services.todo_service import TodoService
except ImportError:
    # If direct import fails, try relative imports
    try:
        from .services.todo_service import TodoService
    except ImportError:
        # If both fail, try importing directly
        from services.todo_service import TodoService


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("TODO APPLICATION - MAIN MENU")
    print("="*40)
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Update Todo")
    print("4. Mark Todo Complete")
    print("5. Mark Todo Incomplete")
    print("6. Delete Todo")
    print("7. Exit")
    print("="*40)


def get_user_choice():
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = input("Select an option (1-7): ").strip()
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= 7:
                    return choice_num
                else:
                    print("Error: Please enter a number between 1 and 7.")
            else:
                print("Error: Please enter a valid number.")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting application...")
            return 7


def add_todo(todo_service):
    """Add a new todo to the list."""
    print("\n--- ADD TODO ---")
    description = input("Enter todo description: ").strip()

    if not description:
        print("Error: Description cannot be empty.")
        return

    try:
        todo = todo_service.create_todo(description)
        print(f"Todo added successfully with ID {todo.id}")
    except ValueError as e:
        print(f"Error: {str(e)}")


def view_todos(todo_service):
    """Display all todos in the list."""
    print("\n--- VIEW TODOS ---")
    todos = todo_service.get_all_todos()

    if not todos:
        print("No todos found.")
        return

    print("Current Todos:")
    for i, todo in enumerate(todos, 1):
        status = "Complete" if todo.completed else "Incomplete"
        print(f"{i}. [{todo.id}] {todo.description} - {status}")


def get_todo_selection(todo_service, prompt="Select a todo number: "):
    """Get and validate user's selection of a todo."""
    todos = todo_service.get_all_todos()

    if not todos:
        print("No todos available.")
        return None

    while True:
        try:
            selection = input(prompt).strip()
            if selection.isdigit():
                selection_num = int(selection)
                if 1 <= selection_num <= len(todos):
                    return todos[selection_num - 1]
                else:
                    print(f"Error: Please enter a number between 1 and {len(todos)}.")
            else:
                print("Error: Please enter a valid number.")
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to main menu...")
            return None


def update_todo(todo_service):
    """Update a todo's description."""
    print("\n--- UPDATE TODO ---")
    todo = get_todo_selection(todo_service, "Select a todo to update (1-{}): ")

    if not todo:
        return

    print(f"Current description: {todo.description}")
    new_description = input("Enter new description: ").strip()

    if not new_description:
        print("Error: Description cannot be empty.")
        return

    try:
        updated_todo = todo_service.update_todo(todo.id, new_description)
        if updated_todo:
            print(f"Todo {todo.id} updated successfully")
        else:
            print(f"Error: Todo with ID {todo.id} does not exist")
    except ValueError as e:
        print(f"Error: {str(e)}")


def mark_complete(todo_service):
    """Mark a todo as complete."""
    print("\n--- MARK TODO COMPLETE ---")
    todo = get_todo_selection(todo_service, "Select a todo to mark complete (1-{}): ")

    if not todo:
        return

    if todo_service.mark_complete(todo.id):
        print(f"Todo {todo.id} marked as complete successfully")
    else:
        print(f"Error: Todo with ID {todo.id} does not exist")


def mark_incomplete(todo_service):
    """Mark a todo as incomplete."""
    print("\n--- MARK TODO INCOMPLETE ---")
    todo = get_todo_selection(todo_service, "Select a todo to mark incomplete (1-{}): ")

    if not todo:
        return

    if todo_service.mark_incomplete(todo.id):
        print(f"Todo {todo.id} marked as incomplete successfully")
    else:
        print(f"Error: Todo with ID {todo.id} does not exist")


def delete_todo(todo_service):
    """Delete a todo from the list."""
    print("\n--- DELETE TODO ---")
    todo = get_todo_selection(todo_service, "Select a todo to delete (1-{}): ")

    if not todo:
        return

    if todo_service.delete_todo(todo.id):
        print(f"Todo {todo.id} deleted successfully")
    else:
        print(f"Error: Todo with ID {todo.id} does not exist")


def main():
    """Main function to run the Todo application with menu interface."""
    print("Welcome to the Todo Application!")

    # Initialize the services
    todo_service = TodoService()

    # Main application loop
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add_todo(todo_service)
        elif choice == 2:
            view_todos(todo_service)
        elif choice == 3:
            update_todo(todo_service)
        elif choice == 4:
            mark_complete(todo_service)
        elif choice == 5:
            mark_incomplete(todo_service)
        elif choice == 6:
            delete_todo(todo_service)
        elif choice == 7:
            print("\nThank you for using the Todo Application!")
            break

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()