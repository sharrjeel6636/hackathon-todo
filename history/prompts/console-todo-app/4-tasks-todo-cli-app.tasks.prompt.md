---
id: 4
title: tasks-todo-cli-app
stage: tasks
date: 2025-12-31
surface: agent
model: Qwen
feature: console-todo-app
branch: 1-console-todo-app
user: Alpha-tech
command: /sp.tasks
labels: [tasks,todo,cli,python]
links:
  spec: specs/phase-1/001-in-memory-console-app.md
  plan: specs/phase-1/002-implementation-plan.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/phase-1/003-tasks-breakdown.md
 - .specify/scripts/powershell/check-prerequisites.ps1
tests:
 - none
---

## Prompt

```
/sp.tasks for Phase I: In-Memory Python Console Todo App Concise & Structured Tasks File: specs/phase-1/003-tasks-breakdown.md Version: 1.0 Date: December 31, 2025 Author: sharjeel Repo: https://github.com/sharrjeel6636/hackathon-todo Rule Reminder: Feed one task at a time to Claude Code. Save output exactly → commit → test. Refine prompt if needed, never edit code manually. Atomic Tasks (Execute in Order) Task ModelFile:src/models.pyPrompt for Claude Code: "Create a Python dataclass called Task with: id: int title: str description: str = '' completed: bool = False Use @dataclass, full type hints, and make fields readable. No other code." Task Manager & OperationsFile:src/operations.pyPrompt: "Create TaskManager class (standard library only): _tasks: list[Task] = [] _next_id: int = 1 Methods with type hints and error handling: add_task(title: str, description: str = '') → Task (raise ValueError if title empty) get_all_tasks() → list[Task] find_task_by_id(id: int) → Task | None (raise ValueError if not found) update_task(id: int, title: str | None = None, description: str | None = None) delete_task(id: int) toggle_complete(id: int) format_tasks() → str: return pretty table with columns ID | Status ([x]/[ ]) | Title | Description (truncate desc to 50 chars + '...')" CLI Main LoopFile:src/main.pyPrompt: "Create main.py as entry point: from operations import TaskManager manager = TaskManager() Infinite loop showing menu: Add task 2. View all tasks 3. Update task 4. Delete task 5. Toggle complete 6. Exit Clear input handling with try/except for integers User-friendly messages for success/errors (task not found, empty title, etc.) On view: print manager.format_tasks() Exit on option 6" Project ConfigFile:pyproject.tomlPrompt: "Minimal pyproject.toml for UV: [project] name = 'hackathon-todo' requires-python = '>=3.13' No dependencies. Add script: [tool.uv.scripts] run = 'python src/main.py'" READMEFile:README.mdPrompt: "Write complete README.md: Title: Hackathon II Phase I – In-Memory Todo Console App Short description Setup: uv sync && uv run src/main.py Usage example with sample output Note: 100% spec-driven with Claude Code" Claude InstructionsFile:CLAUDE.md (root) Prompt: "Write CLAUDE.md: This project follows strict spec-driven development No manual code edits Always reference constitution and specs Built with Claude Code + Spec-Kit Plus" Final Steps (Manual) Run uv run src/main.py → test full flow (add → view → update → toggle → delete) Record <90-second demo video Commit all → push → ready for Phase I submission
```

## Response snapshot

Successfully generated the tasks breakdown for the Phase I In-Memory Python Console Todo Application. Created a comprehensive tasks.md file with 47 atomic tasks organized by user story priority. Tasks are structured to enable independent implementation and testing, following the MVP-first approach. Each task follows the required checklist format with proper Task IDs, story labels, and clear descriptions with file paths.

## Outcome

- ✅ Impact: Complete tasks breakdown created for the Phase I Todo CLI application
- 🧪 Tests: none
- 📁 Files: Created specs/phase-1/003-tasks-breakdown.md and supporting script
- 🔁 Next prompts: /sp.implement to start executing the tasks
- 🧠 Reflection: The tasks breakdown provides a clear roadmap for implementing the application with Claude Code

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin with /sp.implement to execute the tasks