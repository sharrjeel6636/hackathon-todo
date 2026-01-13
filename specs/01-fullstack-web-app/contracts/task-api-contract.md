# Task Management API Contract

## Overview
This document describes the API endpoints for the task management functionality in the Todo Full-Stack Web Application. All endpoints require JWT authentication in the Authorization header.

## Authentication
All API endpoints (except authentication endpoints) require a JWT token in the Authorization header:
```
Authorization: Bearer <token>
```

## Common Response Format
All responses follow the JSON format.

## Endpoints

### GET /api/tasks
**Description**: Returns all tasks for the authenticated user

**Parameters**:
- status (optional): Filter by task status (all, pending, completed). Default: all

**Headers**:
- Authorization: Bearer <token>

**Response**:
- 200: Array of Task objects
- 401: Unauthorized (invalid or missing JWT)

**Example Response**:
```json
[
  {
    "id": 1,
    "user_id": "user123",
    "title": "Complete project",
    "description": "Finish the Hackathon project",
    "completed": false,
    "created_at": "2026-01-06T10:00:00Z",
    "updated_at": "2026-01-06T10:00:00Z"
  }
]
```

### POST /api/tasks
**Description**: Create a new task

**Headers**:
- Authorization: Bearer <token>

**Request Body**:
```json
{
  "title": "string (required, 1-200 characters)",
  "description": "string (optional, nullable)"
}
```

**Response**:
- 201: Created Task object
- 400: Bad request (invalid input)
- 401: Unauthorized (invalid or missing JWT)

**Example Response**:
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Complete project",
  "description": "Finish the Hackathon project",
  "completed": false,
  "created_at": "2026-01-06T10:00:00Z",
  "updated_at": "2026-01-06T10:00:00Z"
}
```

### PUT /api/tasks/{id}
**Description**: Update title and/or description of a task

**Path Parameters**:
- id: Task ID (integer)

**Headers**:
- Authorization: Bearer <token>

**Request Body**:
```json
{
  "title": "string (optional, 1-200 characters)",
  "description": "string (optional, nullable)"
}
```

**Response**:
- 200: Updated Task object
- 400: Bad request (invalid input)
- 401: Unauthorized (invalid or missing JWT)
- 404: Task not found (or doesn't belong to user)

**Example Response**:
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Updated project title",
  "description": "Updated description",
  "completed": false,
  "created_at": "2026-01-06T10:00:00Z",
  "updated_at": "2026-01-06T11:00:00Z"
}
```

### DELETE /api/tasks/{id}
**Description**: Delete a task

**Path Parameters**:
- id: Task ID (integer)

**Headers**:
- Authorization: Bearer <token>

**Response**:
- 204: Task successfully deleted
- 401: Unauthorized (invalid or missing JWT)
- 404: Task not found (or doesn't belong to user)

### PATCH /api/tasks/{id}/complete
**Description**: Toggle the completed status of a task

**Path Parameters**:
- id: Task ID (integer)

**Headers**:
- Authorization: Bearer <token>

**Response**:
- 200: Updated Task object with toggled completion status
- 401: Unauthorized (invalid or missing JWT)
- 404: Task not found (or doesn't belong to user)

**Example Response**:
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Complete project",
  "description": "Finish the Hackathon project",
  "completed": true,
  "created_at": "2026-01-06T10:00:00Z",
  "updated_at": "2026-01-06T11:30:00Z"
}
```

## Error Responses

All error responses follow this format:
```json
{
  "error": "Error message describing the issue"
}
```

## Task Object Definition

```json
{
  "id": "integer (unique, auto-incremented primary key)",
  "user_id": "string (foreign key to User.id from JWT)",
  "title": "string (required, 1-200 characters)",
  "description": "string | null (optional)",
  "completed": "boolean (default: false)",
  "created_at": "timestamp (when the task was created)",
  "updated_at": "timestamp (when the task was last updated)"
}
```