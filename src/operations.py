from typing import List, Optional
import logging

from .models import Task
from .database import TaskDatabase

# Set up logging
logger = logging.getLogger(__name__)


class TaskManager:
    def __init__(self):
        self._db = TaskDatabase()

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        return self._db.add_task(title, description)

    def get_all_tasks(self) -> List[Task]:
        return self._db.get_all_tasks()

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        return self._db.get_task_by_id(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        updated_task = self._db.update_task(task_id, title, description)
        return updated_task is not None

    def delete_task(self, task_id: int) -> bool:
        return self._db.delete_task(task_id)

    def toggle_complete(self, task_id: int) -> bool:
        toggled_task = self._db.toggle_task_completion(task_id)
        return toggled_task is not None

    def get_task_stats(self) -> dict:
        return self._db.get_task_stats()

    def format_tasks(self) -> str:
        tasks = self.get_all_tasks()
        if not tasks:
            return "No tasks available."

        # Create a formatted table
        result = f"{'ID':<4} {'Status':<8} {'Title':<20} {'Description':<30}\n"
        result += "-" * 65 + "\n"

        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            description = task.description if task.description else ""
            # Truncate description if too long
            if len(description) > 27:
                description = description[:27] + "..."

            result += f"{task.id:<4} {status:<8} {task.title:<20} {description:<30}\n"

        return result