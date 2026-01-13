import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from dotenv import load_dotenv
# Load environment variables
load_dotenv()

# Set up logging
from src.logging_config import setup_logging
setup_logging()

from src.operations import TaskManager
from src.models import Task


def demo_application():
    print("=== Hackathon II Phase I – Database-Powered Todo Console App Demo ===\n")

    # Create a task manager instance with database
    manager = TaskManager()

    # Demo: Add tasks
    print("1. Adding tasks:")
    task1 = manager.add_task("Buy groceries", "Milk, eggs, bread")
    print(f"   Added task: ID {task1.id}, Title: '{task1.title}', Description: '{task1.description}'")

    task2 = manager.add_task("Complete project", "Finish the Hackathon project")
    print(f"   Added task: ID {task2.id}, Title: '{task2.title}', Description: '{task2.description}'")

    # Demo: View all tasks
    print("\n2. Viewing all tasks:")
    print(manager.format_tasks())

    # Demo: Update a task
    print("\n3. Updating a task:")
    print(f"   Before update - Task ID {task1.id}: {task1.title}")
    manager.update_task(task1.id, "Buy groceries updated", "Milk, eggs, bread, fruits")
    print(f"   After update - Task ID {task1.id}: {task1.title}")
    print("   Updated task list:")
    print(manager.format_tasks())

    # Demo: Toggle task completion
    print("\n4. Toggling task completion:")
    print(f"   Before toggle - Task ID {task1.id}: {'[x] Completed' if task1.completed else '[ ] Incomplete'}")
    manager.toggle_complete(task1.id)
    print(f"   After toggle - Task ID {task1.id}: {'[x] Completed' if task1.completed else '[ ] Incomplete'}")
    print("   Updated task list:")
    print(manager.format_tasks())

    # Demo: Delete a task
    print("\n5. Deleting a task:")
    print(f"   Deleting task ID {task2.id}")
    manager.delete_task(task2.id)
    print("   Task deleted. Updated task list:")
    print(manager.format_tasks())

    print("\n=== Demo completed ===")


if __name__ == "__main__":
    demo_application()