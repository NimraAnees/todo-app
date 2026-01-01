# Quickstart: Todo App — Phase I: In-Memory Python Console

## Getting Started

### Prerequisites
- Python 3.13+ installed on your system

### Running the Application

1. **Clone or access the project directory**
   ```bash
   cd path/to/todo-app
   ```

2. **Run the todo application**
   ```bash
   python src/main.py
   ```

### Available Commands

Once the application is running, you can use the following commands:

- **Add a new todo**:
  ```bash
  python src/main.py add "Your todo description here"
  ```

- **List all todos**:
  ```bash
  python src/main.py list
  ```

- **Mark a todo as complete**:
  ```bash
  python src/main.py complete 1  # where 1 is the todo ID
  ```

- **Mark a todo as incomplete**:
  ```bash
  python src/main.py incomplete 1  # where 1 is the todo ID
  ```

- **Update a todo description**:
  ```bash
  python src/main.py update 1 "New description"
  ```

- **Delete a todo**:
  ```bash
  python src/main.py delete 1  # where 1 is the todo ID
  ```

### Example Usage

```bash
# Add a few todos
python src/main.py add "Buy groceries"
python src/main.py add "Complete project documentation"
python src/main.py add "Schedule team meeting"

# View all todos
python src/main.py list

# Mark the first todo as complete
python src/main.py complete 1

# Update the second todo
python src/main.py update 2 "Complete project documentation and review"

# Delete the third todo
python src/main.py delete 3

# View updated list
python src/main.py list
```

### Expected Output

The application will provide clear feedback for each operation:

- Success messages when operations complete successfully
- Error messages when invalid inputs or operations are attempted
- Formatted list display showing all todos with their status and IDs

### Troubleshooting

- **Command not found**: Ensure you're running Python from the project root
- **Invalid ID error**: Check that the todo ID exists in the current list
- **Empty list**: The application will indicate when there are no todos to display