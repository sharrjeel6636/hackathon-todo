# Data Model for Phase I: In-Memory Python Console Todo Application

## Task Entity

**Entity Name**: Task

**Fields**:
- id: int (unique, auto-incremented integer ID, starting from 1)
- title: str (required string, non-empty)
- description: str | None (optional string, can be None)
- completed: bool (boolean, default: False)

**Validation Rules**:
- id must be unique and auto-incremented
- title must not be empty when creating a new task
- completed must be a boolean value

**State Transitions**:
- completed: False → True (when task is marked as complete)
- completed: True → False (when task is marked as incomplete)

## TaskList Entity

**Entity Name**: TaskList

**Fields**:
- tasks: List[Task] (collection of Task entities stored in-memory)

**Operations**:
- add_task(task: Task) → adds a new task to the list
- get_task_by_id(task_id: int) → retrieves a specific task
- update_task(task_id: int, new_title: str, new_description: str) → modifies an existing task
- delete_task(task_id: int) → removes a task from the list
- toggle_task_completion(task_id: int) → toggles the completion status of a task
- get_all_tasks() → returns all tasks in the list