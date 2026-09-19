"""
Personal To-Do List Manager (CLI)

A simple command-line application that allows you to:
- Add new tasks
- List all tasks with status
- Mark tasks as completed
- Delete tasks
- Automatically save and load data using JSON
"""

import json
from pathlib import Path

# File where tasks are permanently stored
DATA_FILE = Path("tasks.json")


# Main list that holds all tasks (each task is a dictionary)
tasks = []


def save_tasks():
    """Save the current list of tasks to a JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def load_tasks():
    """Load tasks from the JSON file if it exists, otherwise start with an empty list."""
    global tasks
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    else:
        tasks = []


def show_menu():
    print("\n===== TO_DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. List Task")
    print("3. Mark Task As Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("===============================")


def add_task():
    """Ask the user for a task description and add it to the list."""
    print("\n ===== Add Task =====")
    description = input("Task Description: ").strip().capitalize()

    if not description:
        print("Task Description cannot be empty")
        return
    task =  {
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print("Task Added Successfully")
    save_tasks()


def list_tasks():
    """Display all tasks with their current status."""
    print("\n===== Your Task =====")
    if not tasks:
        print("No tasks yet")
        return
    for i, task in enumerate(tasks, start=1):
        status = "completed" if task ["completed"] else "pending"
        print(f"{i}. {task['description']} [{status}]")
    

def mark_completed():
    """Mark a selected task as completed."""
    print("\n ===== Mark Task As Completed =====")
    if not tasks:
        print("No Tasks yet")
        return

    list_tasks()

    user_input = input("\n Enter the task number: ").strip()
    if not user_input.isdigit():
        print("Please Enter a Valid number.")
        return
    number = int(user_input)

    if number < 1 or number > len(tasks):
        print("Invalid Task Number!")
        return

    index = number - 1
    tasks[index]["completed"] = True
    print(f"Task '{tasks[index]['description']}' marked as completed!")
    save_tasks()


def delete_task():
    """Delete a selected task from the list."""
    print("\n ===== Delete Task =====")
    if not tasks:
        print("No tasks yet.")
        return

    list_tasks()

    user_input = input("\n Enter the number to be deleted: ").strip()
    if not user_input.isdigit():
        print("Please Enter a Valid number.")
        return
    
    number = int(user_input)

    if number < 1 or number > len(tasks):
        print("Invalid Task Number!")
        return

    index = number - 1
    removed_task = tasks.pop(index)
    print(f"Task '{removed_task['description']}' has been deleted.")
    save_tasks()

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
        
