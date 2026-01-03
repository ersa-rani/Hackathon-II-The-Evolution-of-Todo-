"""
Integration tests for the main CLI functionality.
"""
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
import pytest
from unittest.mock import patch, MagicMock
from main import main, create_parser
from models import Todo
from services import TodoService


def test_create_parser():
    """Test that the argument parser is created correctly."""
    parser = create_parser()
    
    # Test that all expected subcommands exist
    assert 'add' in parser._subparsers_action.choices
    assert 'list' in parser._subparsers_action.choices
    assert 'update' in parser._subparsers_action.choices
    assert 'delete' in parser._subparsers_action.choices
    assert 'complete' in parser._subparsers_action.choices
    assert 'incomplete' in parser._subparsers_action.choices


def test_main_add_command(capsys):
    """Test the add command through main."""
    test_args = ['main.py', 'add', '--title', 'Test Title', '--description', 'Test Description']
    
    with patch('sys.argv', test_args):
        # Mock the TodoService to avoid actual file operations
        with patch('main.TodoService') as mock_service:
            mock_todo = Todo(id=1, title='Test Title', description='Test Description', completed=False)
            mock_service_instance = MagicMock()
            mock_service_instance.add_todo.return_value = mock_todo
            mock_service.return_value = mock_service_instance
            
            # Capture stdout
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                main()
            
            output = captured_output.getvalue()
            assert "Added todo: 1 - Test Title" in output


def test_main_list_command(capsys):
    """Test the list command through main."""
    test_args = ['main.py', 'list']
    
    with patch('sys.argv', test_args):
        with patch('main.TodoService') as mock_service:
            mock_todo = Todo(id=1, title='Test Title', description='Test Description', completed=False)
            mock_service_instance = MagicMock()
            mock_service_instance.list_todos.return_value = [mock_todo]
            mock_service.return_value = mock_service_instance
            
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                main()
            
            output = captured_output.getvalue()
            assert "○ [1] Test Title - Test Description" in output


def test_main_list_empty(capsys):
    """Test the list command when no todos exist."""
    test_args = ['main.py', 'list']
    
    with patch('sys.argv', test_args):
        with patch('main.TodoService') as mock_service:
            mock_service_instance = MagicMock()
            mock_service_instance.list_todos.return_value = []
            mock_service.return_value = mock_service_instance
            
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                main()
            
            output = captured_output.getvalue()
            assert "No todos found." in output


def test_main_update_command():
    """Test the update command through main."""
    test_args = ['main.py', 'update', '--id', '1', '--title', 'Updated Title']
    
    with patch('sys.argv', test_args):
        with patch('main.TodoService') as mock_service:
            mock_todo = Todo(id=1, title='Updated Title', description='Original Description', completed=False)
            mock_service_instance = MagicMock()
            mock_service_instance.update_todo.return_value = mock_todo
            mock_service.return_value = mock_service_instance
            
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                main()
            
            output = captured_output.getvalue()
            assert "Updated todo: 1 - Updated Title" in output


def test_main_update_not_found(capsys):
    """Test the update command when todo is not found."""
    test_args = ['main.py', 'update', '--id', '999', '--title', 'Updated Title']
    
    with patch('sys.argv', test_args):
        with patch('main.TodoService') as mock_service:
            mock_service_instance = MagicMock()
            mock_service_instance.update_todo.return_value = None
            mock_service.return_value = mock_service_instance
            
            with pytest.raises(SystemExit) as exc_info:
                main()
            
            assert exc_info.value.code == 1


def test_main_delete_command():
    """Test the delete command through main."""
    test_args = ['main.py', 'delete', '--id', '1']
    
    with patch('sys.argv', test_args):
        with patch('main.TodoService') as mock_service:
            mock_service_instance = MagicMock()
            mock_service_instance.delete_todo.return_value = True
            mock_service.return_value = mock_service_instance
            
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                main()
            
            output = captured_output.getvalue()
            assert "Deleted todo with ID 1" in output


def test_main_complete_command():
    """Test the complete command through main."""
    test_args = ['main.py', 'complete', '--id', '1']
    
    with patch('sys.argv', test_args):
        with patch('main.TodoService') as mock_service:
            mock_service_instance = MagicMock()
            mock_service_instance.toggle_complete.return_value = True
            mock_service.return_value = mock_service_instance
            
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                main()
            
            output = captured_output.getvalue()
            assert "Marked todo 1 as complete" in output


def test_main_incomplete_command():
    """Test the incomplete command through main."""
    test_args = ['main.py', 'incomplete', '--id', '1']
    
    with patch('sys.argv', test_args):
        with patch('main.TodoService') as mock_service:
            mock_service_instance = MagicMock()
            mock_service_instance.toggle_complete.return_value = True
            mock_service.return_value = mock_service_instance
            
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                main()
            
            output = captured_output.getvalue()
            assert "Marked todo 1 as incomplete" in output


def test_main_invalid_command(capsys):
    """Test main with an invalid command."""
    test_args = ['main.py', 'invalid_command']
    
    with patch('sys.argv', test_args):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            main()
        
        output = captured_output.getvalue()
        assert "usage:" in output.lower() or "show this help message" in output.lower()