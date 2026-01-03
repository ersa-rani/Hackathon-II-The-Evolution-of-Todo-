"""
Tests for the Todo data model.
"""
import pytest
from models import Todo


def test_todo_creation():
    """Test creating a Todo object with valid data."""
    todo = Todo(id=1, title="Test Todo", description="Test Description", completed=False)
    assert todo.id == 1
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert todo.completed is False


def test_todo_creation_defaults():
    """Test creating a Todo object with default values."""
    todo = Todo(id=1, title="Test Todo")
    assert todo.id == 1
    assert todo.title == "Test Todo"
    assert todo.description == ""
    assert todo.completed is False


def test_todo_creation_completed():
    """Test creating a Todo object with completed status."""
    todo = Todo(id=1, title="Test Todo", completed=True)
    assert todo.id == 1
    assert todo.title == "Test Todo"
    assert todo.completed is True


def test_todo_empty_title_error():
    """Test that creating a Todo with empty title raises an error."""
    with pytest.raises(ValueError, match="Title cannot be empty"):
        Todo(id=1, title="")


def test_todo_invalid_id_error():
    """Test that creating a Todo with invalid ID raises an error."""
    with pytest.raises(ValueError, match="ID must be a positive integer"):
        Todo(id=0, title="Test Todo")


def test_todo_invalid_completed_error():
    """Test that creating a Todo with invalid completed value raises an error."""
    with pytest.raises(ValueError, match="Completed must be a boolean value"):
        Todo(id=1, title="Test Todo", completed="invalid")