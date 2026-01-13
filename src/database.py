from sqlmodel import SQLModel, create_engine, Session, select
from typing import List, Optional
from .models import Task
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Get database URL from environment or use SQLite as fallback
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")

# For SQLite, we need to handle the path differently
if DATABASE_URL.startswith("sqlite:///"):
    # Ensure the directory exists for SQLite file
    db_path = DATABASE_URL[10:]  # Remove "sqlite:///" prefix
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)

# Create engine
engine = create_engine(DATABASE_URL, echo=False)  # Changed echo to False to reduce logging

# Set up logging
logger = logging.getLogger(__name__)

def create_db_and_tables():
    """Create database tables if they don't exist."""
    SQLModel.metadata.create_all(engine)


class TaskDatabase:
    def __init__(self):
        self.engine = engine

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task to the database."""
        task = Task(title=title, description=description, completed=False)
        with Session(self.engine) as session:
            session.add(task)
            session.commit()
            session.refresh(task)
            return task

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks from the database."""
        with Session(self.engine) as session:
            tasks = session.exec(select(Task)).all()
            return tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve a specific task by its ID."""
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
            return task

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """Update a task's title and/or description."""
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
            if not task:
                return None

            # Update fields if provided
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description

            session.add(task)
            session.commit()
            session.refresh(task)
            return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
            if not task:
                return False

            session.delete(task)
            session.commit()
            return True

    def toggle_task_completion(self, task_id: int) -> Optional[Task]:
        """Toggle the completion status of a task."""
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
            if not task:
                return None

            task.completed = not task.completed
            session.add(task)
            session.commit()
            session.refresh(task)
            return task

    def get_task_stats(self) -> dict:
        """Get task statistics."""
        with Session(self.engine) as session:
            all_tasks = session.exec(select(Task)).all()
            total = len(all_tasks)
            completed = len([task for task in all_tasks if task.completed])
            pending = total - completed

            return {
                "total": total,
                "completed": completed,
                "pending": pending
            }