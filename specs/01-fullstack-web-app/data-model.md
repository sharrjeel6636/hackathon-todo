# Data Model for Phase II: Todo Full-Stack Web Application

## User Entity

**Entity Name**: User

**Fields**:
- id: string (unique identifier from JWT)
- name: string (user's name)
- email: string (user's email, unique)
- created_at: timestamp (when the account was created)

**Validation Rules**:
- email must be a valid email format
- name must not be empty
- email must be unique across all users

## Task Entity

**Entity Name**: Task

**Fields**:
- id: integer (unique, auto-incremented primary key)
- user_id: string (foreign key to User.id from JWT)
- title: string (required, 1-200 characters)
- description: text | None (optional, can be null)
- completed: bool (boolean, default: False)
- created_at: timestamp (when the task was created)
- updated_at: timestamp (when the task was last updated)

**Validation Rules**:
- title must be between 1 and 200 characters
- user_id must correspond to an existing user
- completed must be a boolean value

**State Transitions**:
- completed: False → True (when task is marked as complete)
- completed: True → False (when task is marked as incomplete)

## Relationships

**User to Task**:
- One User can have many Tasks (1 to many relationship)
- Tasks are always associated with a single User via user_id
- All operations on Tasks are filtered by the authenticated user's id