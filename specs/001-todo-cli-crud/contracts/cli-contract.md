# CLI Contract: Todo CLI

## Command Structure

The Todo CLI follows the structure:
```
python main.py [command] [options]
```

## Commands and Options

### Add Command
- **Command**: `add`
- **Options**:
  - `--title` (required): Title of the todo item
  - `--description` (optional): Description of the todo item
- **Response**: Creates a new todo with a unique ID and displays confirmation
- **Example**: `python main.py add --title "Buy groceries" --description "Milk, bread, eggs"`

### List Command
- **Command**: `list`
- **Options**: None
- **Response**: Displays all todos with their ID, title, description, and completion status
- **Example**: `python main.py list`

### Update Command
- **Command**: `update`
- **Options**:
  - `--id` (required): ID of the todo to update
  - `--title` (optional): New title for the todo
  - `--description` (optional): New description for the todo
- **Response**: Updates the specified todo and displays confirmation
- **Example**: `python main.py update --id 1 --title "Updated title" --description "Updated description"`

### Delete Command
- **Command**: `delete`
- **Options**:
  - `--id` (required): ID of the todo to delete
- **Response**: Deletes the specified todo and displays confirmation
- **Example**: `python main.py delete --id 1`

### Complete Command
- **Command**: `complete`
- **Options**:
  - `--id` (required): ID of the todo to mark as complete
- **Response**: Marks the specified todo as complete and displays confirmation
- **Example**: `python main.py complete --id 1`

### Incomplete Command
- **Command**: `incomplete`
- **Options**:
  - `--id` (required): ID of the todo to mark as incomplete
- **Response**: Marks the specified todo as incomplete and displays confirmation
- **Example**: `python main.py incomplete --id 1`

## Error Handling

- Invalid command: Displays help message and exits with error code
- Missing required option: Displays error message and exits with error code
- Invalid ID: Displays error message indicating the ID does not exist
- Invalid option format: Displays error message and exits with error code

## Exit Codes

- `0`: Success
- `1`: General error
- `2`: Command-line usage error