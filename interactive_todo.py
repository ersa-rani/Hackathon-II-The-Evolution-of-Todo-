#!/usr/bin/env python3
"""
Interactive Todo CLI Application
Provides a menu-based interface for the Todo application.
"""

from main import main as run_main
import sys
import subprocess


def show_menu():
    """Display the interactive menu."""
    print("\n" + "="*50)
    print("TODO APPLICATION - INTERACTIVE MODE")
    print("="*50)
    print("Select an option:")
    print("1. Add a new todo")
    print("2. List all todos")
    print("3. Update a todo")
    print("4. Delete a todo")
    print("5. Mark todo as complete")
    print("6. Mark todo as incomplete")
    print("7. Show help")
    print("0. Exit")
    print("="*50)


def get_user_choice():
    """Get and validate user choice."""
    try:
        choice = input("Enter your choice (0-7): ").strip()
        return int(choice)
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 7.")
        return None


def handle_add():
    """Handle adding a new todo."""
    title = input("Enter title: ").strip()
    if not title:
        print("Title is required!")
        return
    
    description = input("Enter description (optional, press Enter to skip): ").strip()
    
    cmd = [sys.executable, "main.py", "add", "--title", title]
    if description:
        cmd.extend(["--description", description])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())


def handle_list():
    """Handle listing all todos."""
    result = subprocess.run([sys.executable, "main.py", "list"], capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())


def handle_update():
    """Handle updating a todo."""
    try:
        todo_id = int(input("Enter todo ID to update: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    
    title = input("Enter new title (or press Enter to keep current): ").strip()
    description = input("Enter new description (or press Enter to keep current): ").strip()
    
    cmd = [sys.executable, "main.py", "update", "--id", str(todo_id)]
    
    if title:
        cmd.extend(["--title", title])
    if description:
        cmd.extend(["--description", description])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())


def handle_delete():
    """Handle deleting a todo."""
    try:
        todo_id = int(input("Enter todo ID to delete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    
    result = subprocess.run([sys.executable, "main.py", "delete", "--id", str(todo_id)], capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())


def handle_complete():
    """Handle marking a todo as complete."""
    try:
        todo_id = int(input("Enter todo ID to mark as complete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    
    result = subprocess.run([sys.executable, "main.py", "complete", "--id", str(todo_id)], capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())


def handle_incomplete():
    """Handle marking a todo as incomplete."""
    try:
        todo_id = int(input("Enter todo ID to mark as incomplete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    
    result = subprocess.run([sys.executable, "main.py", "incomplete", "--id", str(todo_id)], capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())


def handle_help():
    """Show help information."""
    result = subprocess.run([sys.executable, "main.py", "--help"], capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())


def main():
    """Main interactive loop."""
    print("Welcome to the Interactive Todo Application!")
    
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == 1:
            handle_add()
        elif choice == 2:
            handle_list()
        elif choice == 3:
            handle_update()
        elif choice == 4:
            handle_delete()
        elif choice == 5:
            handle_complete()
        elif choice == 6:
            handle_incomplete()
        elif choice == 7:
            handle_help()
        elif choice == 0:
            print("Thank you for using the Todo Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 7.")
        
        # Pause to let user see the result
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()