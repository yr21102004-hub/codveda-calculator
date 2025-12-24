import json
import os

class ToDoList:
    def __init__(self, filename="tasks.json"):

        # Constructor
        # - filename: اسم ملف JSON لتخزين المهام
        # - tasks: قائمة المهام

        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        # Load tasks from JSON file
        # - لو الملف موجود: يقرا المهام
        # - لو مش موجود: يبدأ بقائمة فاضية
        # 
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self): 
        # Save tasks to JSON file
        #- يحفظ المهام علشان تفضل موجودة بعد قفل البرنامج
        
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title): 
        # Add new task 
        # - title: اسم المهمة 
        # - done: False (لسه مخلصتش)
       
        task = {
            "title": title,
            "done": False
        }
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
         # Display all tasks
         #  - يعرض المهام بشكل منظم

        if not self.tasks:
            print("No tasks available.")
            return
        
        for index, task in enumerate(self.tasks, start=1):
            status = "✔" if task["done"] else " "
            print(f"{index}. [{status}] {task['title']}")
    def mark_task_done(self, index):
         # Mark task as done 
         # - index: رقم المهمة

        try:
            self.tasks[index - 1]["done"] = True
            self.save_tasks()
            print("Task marked as done.")
        except IndexError:
            print("Invalid task number.")

    def edit_task(self, index, new_title):
         # Edit task title 
         # - index: رقم المهمة 
         # - new_title: الاسم الجديد

        try:
            self.tasks[index - 1]["title"] = new_title
            self.save_tasks()
            print("Task updated successfully.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index): 
        # Delete task with confirmation 
        # - index: رقم المهمة

        try:
            task = self.tasks[index - 1]
            confirm = input(f"Are you sure you want to delete '{task['title']}'? (y/n): ")

            if confirm.lower() == "y":
                self.tasks.pop(index - 1)
                self.save_tasks()
                print("Task deleted successfully.")
                
            else:
                print("Delete cancelled.")
        except IndexError:
            print("Invalid task number.")