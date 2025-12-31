# Quickstart Guide for Phase I: In-Memory Python Console Todo Application

## Prerequisites

- Python 3.13+
- UV package manager

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sharrjeel6636/hackathon-todo
   cd hackathon-todo
   ```

2. Install dependencies using UV:
   ```bash
   uv sync
   ```

## Running the Application

To run the Todo CLI application:

```bash
uv run src/main.py
```

## Development

To run in development mode:

```bash
uv run src/main.py
```

## Project Structure

```
hackathon-todo/
├── .spec-kit/
│   └── config.yaml
├── specs/
│   ├── constitution.md
│   └── phase-1/
│       ├── 001-in-memory-console-app.md
│       ├── 002-implementation-plan.md
│       └── research.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── operations.py
├── CLAUDE.md
├── README.md
└── pyproject.toml
```

## Using the CLI

Once the application is running, you'll see the main menu:

```
Todo CLI Menu:
1. Add task
2. View all tasks
3. Update task
4. Delete task
5. Toggle complete
6. Exit
```

Follow the prompts to interact with your todo list.