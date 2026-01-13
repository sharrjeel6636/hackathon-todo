# Running the Hackathon II Todo CLI Application

## Overview
This is a command-line interface (CLI) todo application that stores tasks in a local SQLite database. It allows users to add, view, update, delete, and mark tasks as complete through an interactive console interface.

## Prerequisites
- Python 3.13 or higher
- uv package manager

## Setup and Installation

1. Clone or download the repository
2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Running the Application

To run the application, use the following command:

```bash
python main.py console
```

This will start the interactive console application with a menu system.

Alternatively, you can run:

```bash
python main.py test    # To run the application tests
python main.py migrate # To run database migrations
```

## Application Features

Once the application is running with the console command, you'll see the following menu:

```
Todo CLI Menu:
1. Add task
2. View all tasks
3. Update task
4. Delete task
5. Toggle complete
6. Exit
```

### Menu Options

1. **Add task**: Create a new task with a title and optional description
2. **View all tasks**: Display all tasks in a formatted table
3. **Update task**: Modify an existing task's title or description
4. **Delete task**: Remove a task from the list
5. **Toggle complete**: Mark a task as complete/incomplete
6. **Exit**: Quit the application

## Example Usage

1. **Add a task**: Select option 1, enter "Buy groceries" as title, "Milk, eggs, bread" as description
2. **View tasks**: Select option 2 to see the formatted table with your task
3. **Update a task**: Select option 3, enter the task ID, and modify the description
4. **Mark as complete**: Select option 5, enter the task ID to toggle completion status
5. **Delete a task**: Select option 4, enter the task ID to remove it

## Troubleshooting

- If you encounter import errors, make sure you're using the correct Python version (3.13+)
- Ensure all dependencies are installed with `uv sync`
- The application requires an interactive terminal to accept user input
- Make sure the database file has proper read/write permissions

## Testing

To run the tests for the application:

```bash
python main.py test
```

This will execute all functionality tests and verify that the application is working correctly.