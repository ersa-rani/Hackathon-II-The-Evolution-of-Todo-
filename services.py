"""
Todo CLI Application
Business logic and services for the application.
"""
import json
import os
from typing import List, Optional
from models import Todo


class TodoService:
    """
    Service class for managing todos.
    Provides CRUD operations for todo items.
    """

    def __init__(self, data_file: str = "todos.json"):
        """Initialize the service with an empty list of todos."""
        self.data_file = data_file
        self.todos: List[Todo] = []
        self._next_id = 1
        self._load_from_file()

    def _load_from_file(self):
        """Load todos from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.todos = [Todo(**todo) for todo in data['todos']]
                    self._next_id = data.get('next_id', 1)
            except (json.JSONDecodeError, KeyError, TypeError):
                # If there's an error loading the file, start fresh
                self.todos = []
                self._next_id = 1
        else:
            self.todos = []
            self._next_id = 1

    def _save_to_file(self):
        """Save todos to the data file."""
        # Convert todos to dictionaries for JSON serialization
        todos_data = []
        for todo in self.todos:
            todos_data.append({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed
            })

        data = {
            'todos': todos_data,
            'next_id': self._next_id
        }

        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def _get_next_id(self) -> int:
        """Get the next available ID for a new todo."""
        next_id = self._next_id
        self._next_id += 1
        return next_id

    def add_todo(self, title: str, description: str = "") -> Todo:
        """
        Add a new todo to the list.

        Args:
            title: Title of the todo
            description: Description of the todo (optional)

        Returns:
            The newly created Todo object
        """
        if not title:
            raise ValueError("Title cannot be empty")

        new_todo = Todo(
            id=self._get_next_id(),
            title=title,
            description=description,
            completed=False
        )
        self.todos.append(new_todo)
        self._save_to_file()  # Persist changes
        return new_todo

    def list_todos(self) -> List[Todo]:
        """
        Get all todos.

        Returns:
            List of all Todo objects
        """
        return self.todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id: ID of the todo to retrieve

        Returns:
            Todo object if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Todo]:
        """
        Update an existing todo.

        Args:
            todo_id: ID of the todo to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            Updated Todo object if found, None otherwise
        """
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            return None

        if title is not None:
            if not title:
                raise ValueError("Title cannot be empty")
            todo.title = title

        if description is not None:
            todo.description = description

        self._save_to_file()  # Persist changes
        return todo

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: ID of the todo to delete

        Returns:
            True if the todo was deleted, False if not found
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                self._save_to_file()  # Persist changes
                return True
        return False

    def toggle_complete(self, todo_id: int, completed: bool) -> bool:
        """
        Toggle the completion status of a todo.

        Args:
            todo_id: ID of the todo to update
            completed: Whether the todo should be marked as completed

        Returns:
            True if the todo was updated, False if not found
        """
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.completed = completed
            self._save_to_file()  # Persist changes
            return True
        return False