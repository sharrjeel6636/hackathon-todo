---
id: 003
title: final-ui-tasks
stage: tasks
date: 2026-01-06
surface: agent
model: Qwen
feature: fix-frontend-ui
branch: 1-fix-frontend-ui
user: Alpha-tech
command: /sp.tasks
labels: ["ui", "styling", "frontend", "tasks"]
links:
  tasks: "specs/phase-2/004-final-ui-tasks.md"
  plan: "specs/phase-2/003-final-ui-plan.md"
  spec: "specs/phase-2/004-final-ui-fix.md"
  ticket: null
  adr: null
  pr: null
files: 
  - "specs/phase-2/004-final-ui-tasks.md"
tests: []
outcome: "Successfully created tasks file for final premium UI implementation"
evaluation: "Tasks organized by user story with proper dependencies and execution order"
prompt_text: |
  $ARGUMENTS
  — Phase II: Todo Full-Stack Web Application (Final Premium UI Fix) Tasks File: specs/phase-2/004-final-ui-tasks.md Version: 1.0 Date: January 06, 2026 Author: sharjeel Repo: https://github.com/sharrjeel6636/hackathon-todo Rule Reminder: Feed one task at a time to Claude Code. Save output exactly → commit → test. Refine prompt if needed, never edit code manually. Atomic Tasks (Execute in Order) Frontend Tailwind Base ConfigurationFile:frontend/app/globals.cssPrompt: "Generate globals.css with exact Tailwind directives: @tailwind base; @tailwind components; @tailwind utilities; Add dark mode body styles: background black, text white, font system-ui, min-height 100vh." Frontend Tailwind ConfigFile:frontend/tailwind.config.tsPrompt: "Generate tailwind.config.ts with content paths: ['./app//*.{js,ts,jsx,tsx,mdx}', './components//*.{js,ts,jsx,tsx,mdx}']. Enable darkMode: 'class'. Extend theme if needed for premium look." Frontend Root LayoutFile:frontend/app/layout.tsxPrompt: "Generate root layout: import './globals.css', <html lang='en' className='dark'>, <body className='min-h-screen bg-black text-white'> with {children}." Frontend Auth LayoutFile:frontend/app/(auth)/layout.tsxPrompt: "Generate centered dark layout for auth pages: full-screen flex center, glassmorphism card container with max-w-md, rounded-xl, backdrop-blur, subtle border." Frontend Signin PageFile:frontend/app/(auth)/signin/page.tsxPrompt: "Generate premium signin page: 'use client', ShadCN Card, Input, Button. Floating labels. Centered form. Toast on error. Redirect to /tasks on success." Frontend Signup PageFile:frontend/app/(auth)/signup/page.tsxPrompt: "Generate premium signup page: 'use client', same style as signin, add confirm password field, check match, toast on error." Frontend Tasks PageFile:frontend/app/tasks/page.tsxPrompt: "Generate premium tasks page: 'use client', protected route, ShadCN Table or Cards for tasks, custom checkbox [ ] / [x], add form, edit dialog, delete confirmation, toast notifications, loading states." Frontend API ClientFile:frontend/lib/api.tsPrompt: "Generate API client: base URL localhost:8000, Bearer token from JWT, extract user_id, functions for all CRUD with correct paths." Documentation UpdateFile:README.mdPrompt: "Update README with troubleshooting: delete .next cache, npm install, shadcn init, run commands. Add note about cache clearing for styling issues." Final Steps Clear Next.js cache: rm -rf frontend/.next Reinstall and init ShadCN Run frontend Verify premium UI appears with full styling and interactivity Save this file as: specs/phase-2/004-final-ui-tasks.md
response_text: |
  Created tasks file for the final premium UI implementation. The tasks are organized by user story with proper dependencies and execution order:
  - Phase 1: Setup (shared infrastructure)
  - Phase 2: Foundational (blocking prerequisites)
  - Phase 3: User Story 1 - Access Premium UI
  - Phase 4: User Story 2 - Use Interactive Components
  - Phase 5: User Story 3 - Navigate Authenticated Sections
  - Phase 6: Polish & Cross-Cutting Concerns
  Each task follows the required checklist format with ID, story labels, and file paths.
---