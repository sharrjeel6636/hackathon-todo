# CLAUDE.md

## Project Instructions for Claude Code

This project follows strict spec-driven development with no manual code edits.

### Technology Stack
- Python 3.13+
- UV for dependency management
- In-memory storage only (no databases or files)
- Standard library only (no external packages)

### Project Structure
```
hackathon-todo/
├── src/
│   ├── __init__.py
│   ├── main.py          # Entry point + menu loop
│   ├── models.py        # Task dataclass
│   └── operations.py    # CRUD functions
├── pyproject.toml       # UV config
├── README.md
└── CLAUDE.md
```

### Implementation Guidelines
- Follow clean code principles
- Use type hints throughout
- Implement modular design (separate model, operations, CLI)
- Follow PEP 8 standards
- Use meaningful variable/function names
- Create a Task dataclass with id, title, description, and completed fields
- Implement in-memory storage using a list of Task objects
- Create a CLI with numbered menu options (1-6)
- Handle errors gracefully with user-friendly messages