from typing import List, Optional
from models import Task


class TaskManager:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        if not title:
            raise ValueError("Title cannot be empty")
        
        task = Task(id=self._next_id, title=title, description=description, completed=False)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return self._tasks

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        task = self.find_task_by_id(task_id)
        if task is None:
            return False
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        
        return True

    def delete_task(self, task_id: int) -> bool:
        task = self.find_task_by_id(task_id)
        if task is None:
            return False
        
        self._tasks.remove(task)
        return True

    def toggle_complete(self, task_id: int) -> bool:
        task = self.find_task_by_id(task_id)
        if task is None:
            return False
        
        task.completed = not task.completed
        return True

    def format_tasks(self) -> str:
        if not self._tasks:
            return "No tasks available."
        
        # Create a formatted table
        result = f"{'ID':<4} {'Status':<8} {'Title':<20} {'Description':<30}\n"
        result += "-" * 65 + "\n"
        
        for task in self._tasks:
            status = "[x]" if task.completed else "[ ]"
            description = task.description if task.description else ""
            # Truncate description if too long
            if len(description) > 27:
                description = description[:27] + "..."
            
            result += f"{task.id:<4} {status:<8} {task.title:<20} {description:<30}\n"
        
        return result