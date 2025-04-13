import json


class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def get_task():
        pass


class PersonalTask(Task):
    def __init__(self, title, description, due_date, status, category):
        super().__init__(title, description, due_date, status)
        self.category = category

    def get_task():
        return "Personal"


class WorkTask(Task):
    def __init__(self, title, description, due_date, status, priority):
        super().__init__(title, description, due_date, status)
        self.priority = priority

    def get_task():
        return "Work"


class TaskManager:
    def __init__(self, title, description, due_date, status):
        super().__init__(title, description, due_date, status)

    def add_task():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)

        while True:
            try:
                choice = int(input("Enter (1) for personal task\n"
                                   "Enter (2) for work task : "))
            except ValueError:
                print("Enter a valid value!")
            else:
                break
        if choice in range(1, 3):
            if choice == 1:
                task_type = "Personal"
                title = input("Enter a task title : ")
                description = input("Enter a task description : ")
                due_date = input("Enter a task due date (DD/MM/YYYY) : ")
                category = input("Enter a task category : ")
                new_task = {"title": title, "description": description, "due date": due_date,
                            "status": "Incomplete", "type": task_type, "category": category}
                tasks.append(new_task)
                print("Task added successfully.")
            if choice == 2:
                task_type = "Work"
                title = input("Enter a task title : ")
                description = input("Enter a task description : ")
                due_date = input("Enter a task due date (DD/MM/YYYY) : ")
                priority = input("Enter a task priority : ")
                new_task = {"title": title, "description": description, "due date": due_date,
                            "status": "Incomplete", "type": task_type, "priority": priority}
                tasks.append(new_task)
                print("Task added successfully.")
        else:
            print("Invalid Number!")
        file = open("Project_2_json.json", "w")
        json.dump(tasks, file, indent=2)
        file.close()

    def delete_task():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)

        value = input("Enter a name of the task you want to delete : ")
        for item in tasks:
            if item["title"] == value:
                tasks.remove(item)
                print("Task deleted successfully.")
                break
        else:
            print("Task not found!")

        file = open("Project_2_json.json", "w")
        json.dump(tasks, file, indent=2)
        file.close()

    def view_tasks():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)
        print(tasks)
        file.close()

    def update_due_date():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)

        value = input("Enter a name of the task : ")
        for item in tasks:
            if item["title"] == value:
                new_due_date = input("Enter a new task due date (DD/MM/YYYY): ")
                item['due date'] = new_due_date
                print("Task due date updated successfully.")
                break
        else:
            print("Task not found!")

        file = open("Project_2_json.json", "w")
        json.dump(tasks, file, indent=2)
        file.close()

    def mark_task_as_completed():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)

        value = input("Enter a name of the task : ")
        for item in tasks:
            if item["title"] == value:
                if item['status'] == "completed":
                    print("Task already completed")
                    break
                else:
                    item['status'] = "completed"
                    print("Task status marked as completed successfully.")
                    break
        else:
            print("Task not found!")

        file = open("Project_2_json.json", "w")
        json.dump(tasks, file, indent=2)
        file.close()
