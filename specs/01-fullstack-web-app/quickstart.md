# Quickstart Guide for Phase II: Todo Full-Stack Web Application

## Prerequisites

- Node.js 18+ for the frontend
- Python 3.13+ for the backend
- PostgreSQL database (Neon Serverless recommended)
- Git for version control

## Frontend Setup

1. **Create Next.js Application**
   ```bash
   npx create-next-app@latest frontend --typescript --tailwind --eslint
   cd frontend
   ```

2. **Install shadcn/ui**
   ```bash
   npx shadcn-ui@latest init
   npx shadcn-ui@latest add card input button dialog dropdown-menu form label checkbox toast sonner
   ```

3. **Install Additional Dependencies**
   ```bash
   npm install lucide-react framer-motion react-hook-form zod @hookform/resolvers @tanstack/react-query sonner
   npm install -D @types/react
   ```

4. **Install Better Auth**
   ```bash
   npm install better-auth
   ```

5. **Configure Environment Variables**
   Create a `.env.local` file in the frontend directory:
   ```
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
   ```

## Backend Setup

1. **Initialize Python Project**
   ```bash
   mkdir backend
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install fastapi sqlmodel uvicorn python-multipart python-dotenv
   pip install psycopg2-binary  # For PostgreSQL
   ```

2. **Install Better Auth**
   ```bash
   pip install better-auth
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the backend directory:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/todoapp
   JWT_SECRET=your-super-secret-jwt-key
   ```

## Project Structure

```
todo-fullstack-app/
├── frontend/                 # Next.js application
│   ├── app/                  # App Router pages
│   │   ├── login/            # Login page
│   │   ├── signup/           # Signup page
│   │   ├── dashboard/        # Protected dashboard page
│   │   └── layout.tsx        # Root layout
│   ├── components/           # Reusable components
│   │   ├── ui/               # shadcn/ui components
│   │   └── task-card.tsx     # Task card component
│   ├── lib/
│   │   └── utils.ts          # Utility functions
│   ├── hooks/                # Custom React hooks
│   └── types/                # TypeScript type definitions
└── backend/                  # FastAPI application
    ├── main.py               # FastAPI app entry point
    ├── models.py             # SQLModel database models
    ├── database.py           # Database session management
    ├── auth.py               # Authentication middleware
    ├── api/                  # API routes
    │   └── tasks.py          # Task management endpoints
    └── config.py             # Configuration settings
```

## Running the Application

1. **Start the Backend**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

2. **Start the Frontend**
   ```bash
   cd frontend
   npm run dev
   ```

The frontend will be available at http://localhost:3000 and the backend API at http://localhost:8000.

## Key Implementation Notes

- The frontend uses Next.js App Router with protected routes for the dashboard
- Authentication is handled by Better Auth with JWT tokens
- The backend enforces user isolation by checking user_id in all requests
- TanStack Query is used for server state management with optimistic updates
- All UI components come from shadcn/ui as required
- The application is responsive and works on mobile, tablet, and desktop