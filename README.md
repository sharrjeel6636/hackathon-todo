# Hackathon II Phase I – In-Memory Todo Console App

A simple command-line todo application that stores tasks in memory.

## Setup

```bash
uv sync
uv run src/main.py
```

## Usage

Run the application with `uv run src/main.py` and follow the menu prompts to add, view, update, delete, and mark tasks as complete.

### Menu Options

1. Add task - Create a new task with title and optional description
2. View all tasks - Display all tasks in a formatted table
3. Update task - Modify an existing task's title or description
4. Delete task - Remove a task from the list
5. Toggle complete - Mark a task as complete/incomplete
6. Exit - Quit the application

### Sample Output

```
Todo CLI Menu:
1. Add task
2. View all tasks
3. Update task
4. Delete task
5. Toggle complete
6. Exit

Enter your choice (1-6): 1
Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread
Task added successfully with ID: 1

Enter your choice (1-6): 2
ID   Status   Title                Description
-----------------------------------------------------------------
1    [ ]      Buy groceries        Milk, eggs, bread

Enter your choice (1-6): 5
Enter task ID to toggle: 1
Task with ID 1 marked as completed.
```

## Demo Video Key Interactions

For the <90-second demo video, follow these key interactions:

1. **Add a task**: Select option 1, enter "Buy groceries" as title, "Milk, eggs, bread" as description
2. **View tasks**: Select option 2 to see the formatted table with your task
3. **Update a task**: Select option 3, enter the task ID, and modify the description
4. **Mark as complete**: Select option 5, enter the task ID to toggle completion status
5. **Delete a task**: Select option 4, enter the task ID to remove it

## Note

This project follows strict spec-driven development with 100% code generation via Claude Code.