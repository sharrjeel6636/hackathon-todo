# Tasks Breakdown: Phase I: In-Memory Python Console Todo Application

**Feature**: Phase I: In-Memory Python Console Todo Application
**Version**: 1.0
**Date**: December 31, 2025
**Author**: sharjeel
**Repo**: https://github.com/sharrjeel6636/hackathon-todo

## Implementation Strategy

This document breaks down the implementation of the Phase I In-Memory Python Console Todo Application into atomic, executable tasks. Each task is designed to be specific enough for an LLM to complete without additional context. Tasks are organized by user story to enable independent implementation and testing, following the MVP-first approach.

## Dependencies

- User Story 6 (Navigate CLI Menu) must be implemented first as it provides the foundation for all other user stories
- User Stories 1, 2, 5 (Add, View, Mark Complete) are foundational and should be completed before Stories 3, 4 (Update, Delete)
- All user stories depend on the foundational Task model and operations

## Parallel Execution Examples

- [P] Tasks that operate on different files can be executed in parallel (e.g., T002 and T003)
- [P] Model creation can happen in parallel with configuration setup
- [P] Individual user story implementations can happen in parallel once foundational components exist

## Phase 1: Setup

### Goal
Initialize the project structure and configure dependencies as specified in the implementation plan.

### Independent Test Criteria
- Project directory structure matches specifications
- Dependencies can be installed with UV
- Basic configuration files exist

### Tasks

- [X] T001 Create project structure per implementation plan: mkdir src, touch src/__init__.py
- [X] T002 [P] Create pyproject.toml with minimal UV configuration for Python 3.13+ and run script
- [X] T003 [P] Create initial README.md with project title, description, setup instructions
- [X] T004 [P] Create CLAUDE.md with project instructions for Claude Code


## Phase 2: User Story 6 - Navigate CLI Menu (Priority: P1)

### Goal
Implement the main CLI menu loop that allows users to interact with the application through numbered options.

### Independent Test Criteria
- Menu displays all 6 options correctly
- User can select options and see appropriate responses
- Application exits cleanly when option 6 is selected

### Tasks

- [X] T011 [US6] Create main.py with imports from operations and models
- [X] T012 [US6] Implement display_menu function that prints the numbered menu options
- [X] T013 [US6] Implement handle_user_input function with integer validation
- [X] T014 [US6] Create main loop that displays menu and processes user input
- [X] T015 [US6] Add graceful exit functionality when user selects option 6

## Phase 3: User Story 1 - Add New Tasks (Priority: P1)

### Goal
Enable users to add new tasks to their todo list with a title and optional description.

### Independent Test Criteria
- User can select "Add task" option from menu
- User is prompted for title and optional description
- New task is created with unique auto-incremented ID and "incomplete" status
- Error is displayed if title is empty

### Tasks

- [X] T016 [US1] Add "Add task" option to the menu display
- [X] T017 [US1] Implement input handling for adding tasks in main loop
- [X] T018 [US1] Call TaskManager.add_task with user-provided title and description
- [X] T019 [US1] Display success message with new task's ID after adding
- [X] T020 [US1] Handle ValueError from empty title and display appropriate error message

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

### Goal
Allow users to see all their tasks in a clear, readable format showing ID, title, completion status, and description.

### Independent Test Criteria
- User can select "View all tasks" option from menu
- All tasks are displayed in a formatted table with ID, title, status indicator, and description
- Appropriate message is shown when no tasks exist

### Tasks

- [X] T021 [US2] Add "View all tasks" option to the menu display
- [X] T022 [US2] Implement input handling for viewing tasks in main loop
- [X] T023 [US2] Call TaskManager.format_tasks to get formatted task list
- [X] T024 [US2] Display formatted task list to user
- [X] T025 [US2] Show appropriate message when no tasks exist

## Phase 5: User Story 5 - Mark Tasks as Complete/Incomplete (Priority: P1)

### Goal
Enable users to update the completion status of a task when they finish or restart work on it.

### Independent Test Criteria
- User can select "Toggle complete" option from menu
- User is prompted for task ID
- Task's completion status is toggled (complete ↔ incomplete)
- Appropriate error is shown for invalid task IDs

### Tasks

- [X] T026 [US5] Add "Toggle complete" option to the menu display
- [X] T027 [US5] Implement input handling for toggling task completion in main loop
- [X] T028 [US5] Prompt user for task ID and validate input
- [X] T029 [US5] Call TaskManager.toggle_complete with provided task ID
- [X] T030 [US5] Display success message or error if task not found

## Phase 6: User Story 3 - Update Task Details (Priority: P2)

### Goal
Allow users to modify an existing task's title or description.

### Independent Test Criteria
- User can select "Update task" option from menu
- User is prompted for task ID and new values
- Task's title and/or description are updated while preserving unchanged values
- Appropriate error is shown for invalid task IDs

### Tasks

- [X] T031 [US3] Add "Update task" option to the menu display
- [X] T032 [US3] Implement input handling for updating tasks in main loop
- [X] T033 [US3] Prompt user for task ID and validate input
- [X] T034 [US3] Prompt user for new title and description (allowing empty for no change)
- [X] T035 [US3] Call TaskManager.update_task with provided values
- [X] T036 [US3] Display success message or error if task not found

## Phase 7: User Story 4 - Delete Tasks (Priority: P2)

### Goal
Enable users to remove completed or unwanted tasks from their list.

### Independent Test Criteria
- User can select "Delete task" option from menu
- User is prompted for task ID
- Task is permanently removed from the system
- Appropriate error is shown for invalid task IDs

### Tasks

- [X] T037 [US4] Add "Delete task" option to the menu display
- [X] T038 [US4] Implement input handling for deleting tasks in main loop
- [X] T039 [US4] Prompt user for task ID and validate input
- [X] T040 [US4] Call TaskManager.delete_task with provided task ID
- [X] T041 [US4] Display success message or error if task not found

## Phase 8: Polish & Cross-Cutting Concerns

### Goal
Complete the implementation with proper error handling, input validation, and final touches.

### Independent Test Criteria
- All menu options work correctly with proper input validation
- Error messages are user-friendly
- Application handles edge cases gracefully
- All functionality can be tested end-to-end

### Tasks

- [X] T042 Add comprehensive error handling throughout the CLI interface
- [X] T043 Implement input validation for all numeric inputs with appropriate error messages
- [X] T044 Enhance README.md with usage examples and sample output
- [X] T045 Test full workflow: add → view → update → toggle → delete tasks
- [X] T046 Verify application runs correctly with `uv run src/main.py`
- [X] T047 Prepare for <90-second demo video by documenting key interactions