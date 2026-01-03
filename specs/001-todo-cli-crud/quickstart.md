# Quickstart: Todo CLI

## Getting Started

The Todo CLI is a command-line application for managing todo items. It requires Python 3.13+ to run.

## Installation

No installation required. The application runs directly with Python:

```bash
python main.py [command] [options]
```

## Commands

### Add a Todo
```bash
python main.py add --title "My Task" --description "Detailed description of the task"
```

### List All Todos
```bash
python main.py list
```

### Update a Todo
```bash
python main.py update --id 1 --title "Updated Title" --description "Updated description"
```

### Delete a Todo
```bash
python main.py delete --id 1
```

### Mark Todo as Complete
```bash
python main.py complete --id 1
```

### Mark Todo as Incomplete
```bash
python main.py incomplete --id 1
```

## Example Usage

```bash
# Add a new todo
python main.py add --title "Buy groceries" --description "Milk, bread, eggs"

# List all todos
python main.py list

# Mark the first todo as complete
python main.py complete --id 1

# Update a todo
python main.py update --id 1 --title "Buy groceries (completed)"

# Delete a todo
python main.py delete --id 1
```

## Notes

- All data is stored in memory only and will be lost when the application exits
- IDs are assigned sequentially starting from 1
- The application follows PEP8 style guidelines