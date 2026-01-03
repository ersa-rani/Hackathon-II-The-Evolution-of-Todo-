"""
Todo CLI Application
Data models for the application.
"""
from dataclasses import dataclass


@dataclass
class Todo:
    """
    Represents a single todo item.
    
    Attributes:
        id (int): Unique identifier for the todo item
        title (str): Title of the todo item
        description (str): Detailed description of the todo item
        completed (bool): Completion status of the todo item
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not self.title:
            raise ValueError("Title cannot be empty")
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")
        if not isinstance(self.completed, bool):
            raise ValueError("Completed must be a boolean value")