# API Contracts for Phase I: In-Memory Python Console Todo Application

## Task Operations Interface

### add_task(title: str, description: str | None) -> int
- **Purpose**: Adds a new task to the in-memory storage
- **Parameters**: 
  - title: Required string (non-empty)
  - description: Optional string (can be None)
- **Returns**: int - the unique ID of the newly created task
- **Exceptions**: ValueError if title is empty

### list_tasks() -> List[dict]
- **Purpose**: Retrieves all tasks in the system
- **Returns**: List of dictionaries containing task information with keys: id, title, description, completed
- **Format**: Each task dict contains {id: int, title: str, description: str | None, completed: bool}

### update_task(task_id: int, new_title: str | None, new_description: str | None) -> bool
- **Purpose**: Updates an existing task's title and/or description
- **Parameters**:
  - task_id: int - the unique ID of the task to update
  - new_title: str | None - new title (if None, preserve existing)
  - new_description: str | None - new description (if None, preserve existing)
- **Returns**: bool - True if successful, False if task not found

### delete_task(task_id: int) -> bool
- **Purpose**: Removes a task from the system permanently
- **Parameters**: task_id: int - the unique ID of the task to delete
- **Returns**: bool - True if successful, False if task not found

### toggle_task_completion(task_id: int) -> bool
- **Purpose**: Toggles the completion status of a task
- **Parameters**: task_id: int - the unique ID of the task to toggle
- **Returns**: bool - True if successful, False if task not found

## CLI Interface

### display_menu() -> None
- **Purpose**: Shows the main menu options to the user
- **Output**: Prints the menu with numbered options

### handle_user_input() -> None
- **Purpose**: Processes user input and calls appropriate functions
- **Behavior**: Runs in a loop until user selects "Exit"