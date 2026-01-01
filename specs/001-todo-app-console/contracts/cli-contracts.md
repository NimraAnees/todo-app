# CLI Contracts: Todo App — Phase I: In-Memory Python Console

## Command Interface Specification

### Add Todo Command
- **Command**: `python main.py add <description>`
- **Input**: description (string, required)
- **Output**: Success message with assigned ID
- **Error cases**:
  - Empty description → Error message
- **Example**: `python main.py add "Buy groceries"`

### List Todos Command
- **Command**: `python main.py list`
- **Input**: None
- **Output**: Formatted list of all todos with ID, description, and status
- **Error cases**:
  - No todos exist → "No todos found" message
- **Example**: `python main.py list`

### Complete Todo Command
- **Command**: `python main.py complete <id>`
- **Input**: id (integer, required)
- **Output**: Success message confirming completion
- **Error cases**:
  - Invalid ID → Error message
  - Todo doesn't exist → Error message
- **Example**: `python main.py complete 1`

### Incomplete Todo Command
- **Command**: `python main.py incomplete <id>`
- **Input**: id (integer, required)
- **Output**: Success message confirming status change
- **Error cases**:
  - Invalid ID → Error message
  - Todo doesn't exist → Error message
- **Example**: `python main.py incomplete 1`

### Update Todo Command
- **Command**: `python main.py update <id> <new_description>`
- **Input**: id (integer, required), new_description (string, required)
- **Output**: Success message confirming update
- **Error cases**:
  - Invalid ID → Error message
  - Todo doesn't exist → Error message
  - Empty new_description → Error message
- **Example**: `python main.py update 1 "Updated description"`

### Delete Todo Command
- **Command**: `python main.py delete <id>`
- **Input**: id (integer, required)
- **Output**: Success message confirming deletion
- **Error cases**:
  - Invalid ID → Error message
  - Todo doesn't exist → Error message
- **Example**: `python main.py delete 1`

## Data Format Contracts

### Todo Representation
- **Format**: Text display in console
- **Fields**:
  - ID: Integer identifier
  - Description: String content
  - Status: "Complete" or "Incomplete"
  - Created: Timestamp (displayed as needed)

### Error Message Format
- **Format**: "Error: <descriptive message>"
- **Examples**:
  - "Error: Todo with ID 5 does not exist"
  - "Error: Description cannot be empty"

### Success Message Format
- **Format**: "<action> successful" or "Todo <ID> <action> successfully"
- **Examples**:
  - "Todo added successfully with ID 1"
  - "Todo 1 marked as complete successfully"