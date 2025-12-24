from To_Do_List import ToDoList
def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            todo.add_task(title)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            index = int(input("Enter task number: "))
            todo.mark_task_done(index)

        elif choice == "4":
            index = int(input("Enter task number: "))
            new_title = input("Enter new task title: ")
            todo.edit_task(index, new_title)

        elif choice == "5":
            index = int(input("Enter task number: "))
            todo.delete_task(index)

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")

        # 👇 السؤال اللي انت عايزه
        again = input("\nDo you want to perform another operation? (y/n): ")
        if again.lower() != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()
