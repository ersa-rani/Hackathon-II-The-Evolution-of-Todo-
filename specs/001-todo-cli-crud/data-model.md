# Data Model: Todo CLI

## Todo Entity

**Entity Name**: Todo

**Fields**:
- `id` (int): Unique identifier for the todo item, assigned sequentially starting from 1
- `title` (str): Title of the todo item, required field
- `description` (str): Detailed description of the todo item, optional field (can be empty string)
- `completed` (bool): Completion status of the todo item, defaults to False when created

**Relationships**: None (standalone entity)

**Validation Rules**:
- `id` must be a positive integer
- `title` must not be empty or None
- `completed` must be a boolean value

**State Transitions**:
- `completed` can transition from False to True (mark complete)
- `completed` can transition from True to False (mark incomplete)

## In-Memory Storage

**Data Structure**: List of Todo objects
- `todos: List[Todo]` - Maintains all todo items in memory during application runtime
- Operations (add, update, delete) modify this list directly
- Data is lost when the application terminates