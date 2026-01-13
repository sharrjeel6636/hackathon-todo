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

def test_app():
    print("Testing the Todo CLI application functionality...\n")

    # Create a task manager instance with database
    manager = TaskManager()
    
    # Test adding tasks
    print("1. Testing add_task functionality:")
    task1 = manager.add_task("Buy groceries", "Milk, eggs, bread")
    print(f"   Added task: ID={task1.id}, Title='{task1.title}', Description='{task1.description}', Completed={task1.completed}")
    
    task2 = manager.add_task("Complete project", "Finish the hackathon project")
    print(f"   Added task: ID={task2.id}, Title='{task2.title}', Description='{task2.description}', Completed={task2.completed}")
    
    # Test viewing tasks
    print("\n2. Testing view all tasks:")
    print(manager.format_tasks())
    
    # Test toggling completion
    print("3. Testing toggle complete:")
    manager.toggle_complete(task1.id)
    print(f"   Toggled task {task1.id} completion status. Now completed: {task1.completed}")
    
    # Test viewing tasks again to see the updated status
    print("\n4. Viewing tasks after toggling completion:")
    print(manager.format_tasks())
    
    # Test updating a task
    print("5. Testing update task:")
    manager.update_task(task2.id, "Complete Hackathon project", "Finish the hackathon project by tonight")
    print(f"   Updated task {task2.id}")
    
    # Test viewing tasks after update
    print("\n6. Viewing tasks after update:")
    print(manager.format_tasks())
    
    # Test deleting a task
    print("7. Testing delete task:")
    delete_result = manager.delete_task(task1.id)
    print(f"   Deleted task {task1.id}: {delete_result}")
    
    # Final view of tasks
    print("\n8. Final view of tasks:")
    print(manager.format_tasks())
    
    print("\nAll functionality tests completed successfully!")

if __name__ == "__main__":
    test_app()