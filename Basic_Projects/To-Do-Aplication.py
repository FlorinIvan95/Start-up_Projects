tasks = []


def display_tasks():
    print("\nTasks:")
    for i, task in enumerate(tasks):
        print("{}. {}".format(i + 1, task))


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")


def edit_task():
    display_tasks()
    index = int(input("Enter task number to edit: "))
    if index > 0 and index <= len(tasks):
        task = input("Enter updated task: ")
        tasks[index - 1] = task
        print("Task updated.")
    else:
        print("Invalid task number.")


def delete_task():
    display_tasks()
    index = int(input("Enter task number to delete: "))
    if index > 0 and index <= len(tasks):
        tasks.pop(index - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")


while True:
    print("\nTo-Do List Application\n")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_tasks()
    elif choice == 2:
        add_task()
    elif choice == 3:
        edit_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
