# Todo CLI Application

A simple command-line interface application for managing todo items. This application allows you to add, list, update, delete, and mark todos as complete/incomplete directly from your terminal.

## Features

- Add new todo items with title and optional description
- List all todos with their completion status
- Update existing todos by ID
- Delete todos by ID
- Mark todos as complete or incomplete
- Persistent storage (todos are saved between sessions)
- Interactive menu system for easier use

## Requirements

- Python 3.13 or higher

## Installation

No installation required! Simply clone the repository and run the application directly with Python.

```bash
git clone <repository-url>
cd evolution-of-todo
```

## Usage

The application can be used in two ways:

### 1. Direct CLI Commands

The application is run using Python with various commands and options:

#### Add a Todo
```bash
python main.py add --title "My Task" --description "Detailed description of the task"
```

#### List All Todos
```bash
python main.py list
```

#### Update a Todo
```bash
python main.py update --id 1 --title "Updated Title" --description "Updated description"
```

#### Delete a Todo
```bash
python main.py delete --id 1
```

#### Mark Todo as Complete
```bash
python main.py complete --id 1
```

#### Mark Todo as Incomplete
```bash
python main.py incomplete --id 1
```

### 2. Interactive Mode

For a more user-friendly experience, you can use the interactive menu system:

```bash
python interactive_todo.py
```

This will start an interactive menu where you can:
1. Add a new todo
2. List all todos
3. Update a todo
4. Delete a todo
5. Mark a todo as complete
6. Mark a todo as incomplete
7. Show help
0. Exit

## Example Workflow

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

## Project Structure

```
.
├── main.py              # CLI interface and argument parsing
├── models.py            # Todo dataclass definition
├── services.py          # Business logic for CRUD operations
├── interactive_todo.py  # Interactive menu system
├── requirements.txt     # Project dependencies
├── todos.json           # Persistent storage for todos (created automatically)
├── tests/               # Test files
│   ├── test_models.py   # Unit tests for data models
│   ├── test_services.py # Unit tests for business logic
│   └── test_main.py     # Integration tests for CLI
└── README.md            # This file
```

## Architecture

The application follows a modular architecture:

- **models.py**: Contains the Todo dataclass definition
- **services.py**: Implements the business logic for all CRUD operations
- **main.py**: Handles CLI argument parsing and user interaction
- **interactive_todo.py**: Provides an interactive menu system for easier use

## Data Model

Each todo item has the following structure:
- `id` (int): Unique identifier for the todo item
- `title` (str): Title of the todo item (required)
- `description` (str): Detailed description of the todo item (optional)
- `completed` (bool): Completion status of the todo item

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).