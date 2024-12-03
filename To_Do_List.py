# app.py
tasks = []

def display_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{index}. {task['title']} - {status}")

def add_task():
    title = input("Enter the task: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added successfully.")

def mark_task_complete():
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as complete: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['title']}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()