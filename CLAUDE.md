# CLAUDE.md

## Project Instructions for Claude Code

This project follows strict spec-driven development with no manual code edits.

### Technology Stack
- Python 3.13+, UV for dependency management, SQLModel for database models, SQLite for persistent storage

### Project Structure
```
hackathon-todo/
├── .spec-kit/
│   └── config.yaml
├── specs/
│   ├── constitution.md
│   └── phase-1/
│       ├── 001-in-memory-console-app.md
│       ├── 002-implementation-plan.md
│       ├── 003-tasks-breakdown.md
│       ├── data-model.md
│       ├── quickstart.md
│       ├── research.md
│       └── checklists/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── operations.py
│   ├── database.py
│   └── logging_config.py
├── CLAUDE.md
├── README.md
├── pyproject.toml
└── todo.db
```

### Implementation Guidelines
- Follow clean code principles
- Use type hints throughout
- Implement modular design (separate model, operations, CLI)
- Follow PEP 8 standards for Python
- Use meaningful variable names
- Handle errors gracefully with user-friendly messages
- Implement database persistence using SQLModel
- Support both SQLite and PostgreSQL database backends
- Use environment variables for configuration
- Implement proper logging