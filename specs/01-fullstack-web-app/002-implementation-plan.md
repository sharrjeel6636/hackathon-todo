# Implementation Plan for Phase II: Todo Full-Stack Web Application

**Plan ID**: phase-2-implementation-plan
**Version**: 1.0
**Date**: 2026-01-06
**Author**: Qwen
**GitHub Repository**: https://github.com/sharrjeel6636/hackathon-todo
**Spec Reference**: specs/01-fullstack-web-app/spec.md (Version 1.0)
**Constitution Adherence**: FULL - Following all architectural constraints and technology choices specified in the feature requirements.

## Technical Context

Next.js 16+ with App Router as specified in the project constitution and feature requirements.
TypeScript for type safety and maintainability.
Tailwind CSS for styling as specified.
shadcn/ui components for UI elements.
FastAPI for the backend API.
SQLModel for database modeling.
Neon Serverless PostgreSQL for persistent storage.
Better Auth for JWT-based authentication.

## Constitution Check

Based on the project constitution and feature requirements, this implementation must:
- [x] Use Next.js 16+ with App Router
- [x] Use TypeScript for type safety
- [x] Use Tailwind CSS for styling
- [x] Use shadcn/ui components exclusively
- [x] Use FastAPI for the backend
- [x] Use SQLModel for database modeling
- [x] Use Neon Serverless PostgreSQL
- [x] Implement Better Auth for JWT-based authentication
- [x] Follow responsive design principles
- [x] Implement proper error handling and loading states
- [x] Ensure user data isolation

All constitution requirements have been verified and implemented in this plan.

## Gates

- [x] All technology choices align with Phase II constraints
- [x] Frontend stack matches requirements (Next.js 16+, TypeScript, Tailwind, shadcn/ui)
- [x] Backend stack matches requirements (FastAPI, SQLModel, PostgreSQL)
- [x] Authentication approach matches requirements (Better Auth with JWT)
- [x] Implementation plan adheres to constitution principles

## Phase 0: Research

Research tasks to resolve all technical decisions and technology choices.

### 0.1 Next.js App Router Setup
- [x] Determine Next.js 16+ setup with TypeScript
- [x] Configure App Router structure
- [x] Set up project structure with proper routing

### 0.2 shadcn/ui Integration
- [x] Determine shadcn/ui installation process
- [x] Identify required components (Card, Input, Button, Dialog, etc.)
- [x] Configure shadcn/ui with Tailwind

### 0.3 Better Auth Integration
- [x] Research Better Auth setup for Next.js
- [x] Understand JWT token handling
- [x] Determine how to attach JWT to API requests

### 0.4 FastAPI Backend Setup
- [x] Determine FastAPI project structure
- [x] Configure SQLModel with PostgreSQL
- [x] Set up database connection and models

### 0.5 API Design
- [x] Design REST API endpoints for task management
- [x] Determine authentication flow between frontend and backend
- [x] Plan error handling and status codes

## Phase 1: Design & Contracts

### 1.1 Data Model Design

**User Entity**:
- id: string (from JWT)
- name: string
- email: string
- created_at: timestamp

**Task Entity**:
- id: integer (primary key)
- user_id: string (from JWT)
- title: string (required)
- description: text (nullable)
- completed: boolean (default false)
- created_at: timestamp
- updated_at: timestamp

### 1.2 API Contracts

**Authentication Endpoints** (handled by Better Auth):
- POST /api/auth/signup
- POST /api/auth/signin
- POST /api/auth/signout

**Task Management Endpoints**:
- GET /api/tasks - Returns all tasks for authenticated user, supports filter by status (all/pending/completed)
- POST /api/tasks - Create new task, title required
- PUT /api/tasks/{id} - Update title and/or description, only if task belongs to user
- DELETE /api/tasks/{id} - Delete task, only if task belongs to user
- PATCH /api/tasks/{id}/complete - Toggle completed status

### 1.3 Quickstart Guide

**Frontend Setup**:
1. Create Next.js app with TypeScript
2. Install and configure Tailwind CSS
3. Install and configure shadcn/ui components
4. Install and configure required libraries (lucide-react, Framer Motion, React Hook Form, Zod, TanStack Query, Sonner)
5. Integrate Better Auth

**Backend Setup**:
1. Create FastAPI application
2. Configure SQLModel with PostgreSQL
3. Create database models
4. Implement API endpoints with authentication and user isolation
5. Configure CORS and middleware

### 1.4 Agent Context Update

The following technologies have been added to the agent context for this implementation:
- Next.js 16+ with App Router
- TypeScript
- Tailwind CSS
- shadcn/ui components
- FastAPI
- SQLModel
- Neon Serverless PostgreSQL
- Better Auth with JWT
- TanStack Query
- React Hook Form + Zod
- Framer Motion
- Sonner notifications

## Re-evaluated Constitution Check Post-Design

- [x] All API endpoints follow REST conventions
- [x] User data isolation is enforced through user_id checks
- [x] JWT authentication is properly implemented
- [x] Frontend and backend technologies match requirements
- [x] Responsive design principles are incorporated
- [x] Error handling and loading states are planned