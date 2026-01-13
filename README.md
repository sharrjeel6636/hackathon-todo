# Hackathon Todo CLI Application

A command-line interface todo application with advanced filtering capabilities.

## Features

- Task management (Create, Read, Update, Delete, Mark Complete)
- Database-powered storage
- Console-based user interface

## Tech Stack

- **CLI Application**: Python with SQLModel
- **Database**: Local SQLite database

## Setup

1. Clone the repository
2. Install dependencies: `uv sync`
3. Create a `.env` file based on `.env.example` with your database configuration:
   ```
   DATABASE_URL="sqlite:///./todo.db"
   ```

## Running the Application

1. Run the console application: `python main.py console`
2. Run tests: `python main.py test`
3. Run database migrations: `python main.py migrate`
4. Or run the demo: `python demo_app.py`

## CLI Commands

The application supports the following commands:

- `python main.py console` - Starts the interactive console application
- `python main.py test` - Runs the application tests
- `python main.py migrate` - Runs database migrations

## Console Application Usage

The console application provides an interactive menu system for managing your tasks:

```
Todo CLI Menu:
1. Add task
2. View all tasks
3. Update task
4. Delete task
5. Toggle complete
6. Exit
```

## Usage Examples

### Managing Tasks
1. Run the console application: `python main.py console`
2. Use the menu options to add, view, update, or delete tasks
3. Follow the prompts to interact with the application

## Security Features

- Secure database storage

## Performance Optimizations

- Optimized database queries
- Efficient data handling