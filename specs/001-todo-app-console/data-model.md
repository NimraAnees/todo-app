# Data Model: Todo App — Phase I: In-Memory Python Console

## Todo Entity

### Fields
- **id**: int (unique identifier, auto-incremented)
- **description**: str (text description of the todo task)
- **completed**: bool (status indicating completion, default: False)
- **created_at**: datetime (timestamp of creation, auto-generated)

### Relationships
- No relationships needed as this is a simple, single-entity model

### Validation Rules
- **id**: Must be a positive integer, auto-generated
- **description**: Must be a non-empty string (1-500 characters)
- **completed**: Must be a boolean value (True/False)
- **created_at**: Must be a valid datetime object, auto-generated

### State Transitions
- **Incomplete → Complete**: When user marks todo as complete
- **Complete → Incomplete**: When user marks todo as incomplete

## Todo Service Data Operations

### Methods
- **create_todo(description: str)**: Creates a new todo with provided description
- **get_all_todos()**: Returns list of all todos
- **get_todo_by_id(id: int)**: Returns specific todo by ID
- **update_todo(id: int, description: str)**: Updates description of existing todo
- **mark_complete(id: int)**: Marks todo as complete
- **mark_incomplete(id: int)**: Marks todo as incomplete
- **delete_todo(id: int)**: Removes todo from the list

### In-Memory Storage Structure
- **todos**: List[Todo] - Maintains all todo objects in memory
- **next_id**: int - Tracks the next available ID for new todos