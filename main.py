"""
Todo CLI Application
Main entry point for the command-line interface.
"""
import argparse
import sys
from models import Todo
from services import TodoService


def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Todo CLI - Manage your tasks from the command line"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new todo")
    add_parser.add_argument("--title", required=True, help="Title of the todo")
    add_parser.add_argument("--description", help="Description of the todo")

    # List command
    list_parser = subparsers.add_parser("list", help="List all todos")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a todo")
    update_parser.add_argument("--id", type=int, required=True, help="ID of the todo to update")
    update_parser.add_argument("--title", help="New title for the todo")
    update_parser.add_argument("--description", help="New description for the todo")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a todo")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the todo to delete")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a todo as complete")
    complete_parser.add_argument("--id", type=int, required=True, help="ID of the todo to mark complete")

    # Incomplete command
    incomplete_parser = subparsers.add_parser("incomplete", help="Mark a todo as incomplete")
    incomplete_parser.add_argument("--id", type=int, required=True, help="ID of the todo to mark incomplete")

    return parser


def main():
    """Main entry point for the application."""
    parser = create_parser()
    args = parser.parse_args()

    # Initialize the todo service
    service = TodoService()

    if args.command == "add":
        todo = service.add_todo(args.title, args.description or "")
        print(f"Added todo: {todo.id} - {todo.title}")
    elif args.command == "list":
        todos = service.list_todos()
        if not todos:
            print("No todos found.")
        else:
            for todo in todos:
                status = "X" if todo.completed else "O"
                print(f"[{status}] [{todo.id}] {todo.title} - {todo.description}")
    elif args.command == "update":
        try:
            updated_todo = service.update_todo(args.id, args.title, args.description)
            if updated_todo:
                print(f"Updated todo: {updated_todo.id} - {updated_todo.title}")
            else:
                print(f"Todo with ID {args.id} not found.")
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    elif args.command == "delete":
        success = service.delete_todo(args.id)
        if success:
            print(f"Deleted todo with ID {args.id}")
        else:
            print(f"Todo with ID {args.id} not found.")
            sys.exit(1)
    elif args.command == "complete":
        success = service.toggle_complete(args.id, True)
        if success:
            print(f"Marked todo {args.id} as complete")
        else:
            print(f"Todo with ID {args.id} not found.")
            sys.exit(1)
    elif args.command == "incomplete":
        success = service.toggle_complete(args.id, False)
        if success:
            print(f"Marked todo {args.id} as incomplete")
        else:
            print(f"Todo with ID {args.id} not found.")
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()