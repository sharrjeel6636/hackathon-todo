from operations import TaskManager
from models import Task


def display_menu():
    print("\nTodo CLI Menu:")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Toggle complete")
    print("6. Exit")


def handle_user_input():
    try:
        choice = int(input("\nEnter your choice (1-6): "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return None


def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = handle_user_input()

        if choice is None:
            continue

        if choice == 6:
            print("Exiting the application. Goodbye!")
            break
        elif choice == 1:
            add_task_ui(manager)
        elif choice == 2:
            print(manager.format_tasks())
        elif choice == 3:
            update_task_ui(manager)
        elif choice == 4:
            delete_task_ui(manager)
        elif choice == 5:
            toggle_complete_ui(manager)
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


def add_task_ui(manager):
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Title cannot be empty.")
        return

    description = input("Enter task description (optional): ").strip()
    if not description:
        description = None

    try:
        task = manager.add_task(title, description)
        print(f"Task added successfully with ID: {task.id}")
    except ValueError as e:
        print(f"Error: {e}")


def update_task_ui(manager):
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
        return

    # Get the current task to show existing values
    task = manager.find_task_by_id(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    print(f"Current title: {task.title}")
    new_title = input("Enter new title (or press Enter to keep current): ").strip()
    if not new_title:
        new_title = None  # Keep current title

    print(f"Current description: {task.description or ''}")
    new_description = input("Enter new description (or press Enter to keep current): ").strip()
    if not new_description:
        new_description = None  # Keep current description

    success = manager.update_task(task_id, new_title, new_description)
    if success:
        print("Task updated successfully.")
    else:
        print("Failed to update task.")


def delete_task_ui(manager):
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
        return

    success = manager.delete_task(task_id)
    if success:
        print(f"Task with ID {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def toggle_complete_ui(manager):
    try:
        task_id = int(input("Enter task ID to toggle: "))
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
        return

    success = manager.toggle_complete(task_id)
    if success:
        task = manager.find_task_by_id(task_id)
        status = "completed" if task.completed else "incomplete"
        print(f"Task with ID {task_id} marked as {status}.")
    else:
        print(f"Error: Task with ID {task_id} not found.")


if __name__ == "__main__":
    main()