"""
Tests for the TodoService.
"""
import pytest
from models import Todo
from services import TodoService


def test_add_todo():
    """Test adding a new todo."""
    service = TodoService()
    todo = service.add_todo("Test Todo", "Test Description")
    
    assert todo.id == 1
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert todo.completed is False
    assert len(service.todos) == 1


def test_add_todo_without_description():
    """Test adding a new todo without description."""
    service = TodoService()
    todo = service.add_todo("Test Todo")
    
    assert todo.id == 1
    assert todo.title == "Test Todo"
    assert todo.description == ""
    assert todo.completed is False


def test_add_todo_empty_title_error():
    """Test that adding a todo with empty title raises an error."""
    service = TodoService()
    with pytest.raises(ValueError, match="Title cannot be empty"):
        service.add_todo("", "Test Description")


def test_list_todos():
    """Test listing all todos."""
    service = TodoService()
    service.add_todo("First Todo", "First Description")
    service.add_todo("Second Todo", "Second Description")
    
    todos = service.list_todos()
    
    assert len(todos) == 2
    assert todos[0].title == "First Todo"
    assert todos[1].title == "Second Todo"


def test_list_todos_empty():
    """Test listing todos when there are none."""
    service = TodoService()
    todos = service.list_todos()
    
    assert len(todos) == 0


def test_get_todo_by_id():
    """Test getting a todo by its ID."""
    service = TodoService()
    added_todo = service.add_todo("Test Todo", "Test Description")
    
    retrieved_todo = service.get_todo_by_id(added_todo.id)
    
    assert retrieved_todo is not None
    assert retrieved_todo.id == added_todo.id
    assert retrieved_todo.title == added_todo.title


def test_get_todo_by_id_not_found():
    """Test getting a todo by ID that doesn't exist."""
    service = TodoService()
    retrieved_todo = service.get_todo_by_id(999)
    
    assert retrieved_todo is None


def test_update_todo():
    """Test updating a todo."""
    service = TodoService()
    original_todo = service.add_todo("Original Title", "Original Description")
    
    updated_todo = service.update_todo(original_todo.id, "New Title", "New Description")
    
    assert updated_todo is not None
    assert updated_todo.id == original_todo.id
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "New Description"


def test_update_todo_partial():
    """Test updating only some fields of a todo."""
    service = TodoService()
    original_todo = service.add_todo("Original Title", "Original Description")
    
    # Update only the title
    updated_todo = service.update_todo(original_todo.id, title="New Title")
    
    assert updated_todo is not None
    assert updated_todo.id == original_todo.id
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "Original Description"  # Should remain unchanged


def test_update_todo_not_found():
    """Test updating a todo that doesn't exist."""
    service = TodoService()
    result = service.update_todo(999, "New Title", "New Description")
    
    assert result is None


def test_update_todo_empty_title_error():
    """Test that updating a todo with empty title raises an error."""
    service = TodoService()
    original_todo = service.add_todo("Original Title", "Original Description")
    
    with pytest.raises(ValueError, match="Title cannot be empty"):
        service.update_todo(original_todo.id, "")


def test_delete_todo():
    """Test deleting a todo."""
    service = TodoService()
    todo_to_delete = service.add_todo("Todo to Delete", "Description")
    other_todo = service.add_todo("Other Todo", "Other Description")
    
    result = service.delete_todo(todo_to_delete.id)
    
    assert result is True
    assert len(service.todos) == 1
    assert service.todos[0].id == other_todo.id


def test_delete_todo_not_found():
    """Test deleting a todo that doesn't exist."""
    service = TodoService()
    result = service.delete_todo(999)
    
    assert result is False


def test_toggle_complete():
    """Test toggling the completion status of a todo."""
    service = TodoService()
    todo = service.add_todo("Test Todo", "Test Description")
    
    # Initially should be False
    assert todo.completed is False
    
    # Mark as complete
    result = service.toggle_complete(todo.id, True)
    assert result is True
    assert todo.completed is True
    
    # Mark as incomplete
    result = service.toggle_complete(todo.id, False)
    assert result is True
    assert todo.completed is False


def test_toggle_complete_not_found():
    """Test toggling completion status for a todo that doesn't exist."""
    service = TodoService()
    result = service.toggle_complete(999, True)
    
    assert result is False