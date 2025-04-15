import json
import re
from datetime import datetime


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
        def validate_date_format(date_text):
            return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", date_text))

        def validate_time_format(time_text):
            return bool(re.match(r"^\d{2}:\d{2}$", time_text))

        def get_validated_input(prompt, validation_func, error_message):
            while True:
                user_input = input(prompt)
                if validation_func(user_input):
                    return user_input
                else:
                    print(error_message)

        file = open("Project_2_json.json", "r")
        tasks = json.load(file)

        while True:
            try:
                choice = int(input("\nChoose Number:\n(1) Personal Task\n(2) Work Task\n: "))
            except ValueError:
                print("Please enter a valid number!\n")
            else:
                break
        if choice in range(1, 3):
            if choice == 1:
                task_type = "Personal"
                while True:
                    title = input("Enter task title: ")
                    if any(task['title'] == title for task in tasks):
                        print("Title already exists, please enter a different title.\n")
                    else:
                        break
                description = input("Enter task description: ")
                due_date = get_validated_input("Enter task deadline date (DD/MM/YYYY): ", validate_date_format, "Invalid date format, please try again.")
                due_time = get_validated_input("Enter task deadline time (HH:MM): ", validate_time_format, "Invalid time format, please try again.")
                creation_datetime = datetime.now().strftime("%d/%m/%Y %H:%M")
                category = input("Enter task category: ")
                location = input("Enter task location: ")
                assignee = input("Enter task assignee: ")
                new_task = {"title": title, "description": description, "deadline date": due_date,
                            "deadline time": due_time, "creation datetime": creation_datetime,
                            "status": "Incomplete", "type": task_type, "category": category,
                            "location": location, "assignee": assignee}
                tasks.append(new_task)
                print("Task added successfully.\n")
            if choice == 2:
                task_type = "Work"
                while True:
                    title = input("Enter task title: ")
                    if any(task['title'] == title for task in tasks):
                        print("Title already exists, please enter a different title.\n")
                    else:
                        break
                description = input("Enter task description: ")
                due_date = get_validated_input("Enter task deadline date (DD/MM/YYYY): ", validate_date_format, "Invalid date format, please try again.")
                due_time = get_validated_input("Enter task deadline time (HH:MM): ", validate_time_format, "Invalid time format, please try again.")
                creation_datetime = datetime.now().strftime("%d/%m/%Y %H:%M")
                priority = input("Enter task priority: ")
                location = input("Enter task location: ")
                assignee = input("Enter task assignee: ")
                new_task = {"title": title, "description": description, "deadline date": due_date,
                            "deadline time": due_time, "creation datetime": creation_datetime,
                            "status": "Incomplete", "type": task_type, "priority": priority,
                            "location": location, "assignee": assignee}
                tasks.append(new_task)
                print("Task added successfully.\n")
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

    def update_deadline_date():
        def validate_date_format(date_text):
            return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", date_text))

        def get_validated_input(prompt, validation_func, error_message):
            while True:
                user_input = input(prompt)
                if validation_func(user_input):
                    return user_input
                else:
                    print(error_message)

        file = open("Project_2_json.json", "r")
        tasks = json.load(file)

        while True:
            value = input("Enter a name of the task: ")
            task_found = False
            for item in tasks:
                if item["title"] == value:
                    new_due_date = get_validated_input("Enter a new task deadline date (DD/MM/YYYY): ", validate_date_format, "Invalid date format, please try again.")
                    item['deadline date'] = new_due_date
                    print("Task deadline date updated successfully.")
                    task_found = True
                    break
            if task_found:
                break
            else:
                print("Task not found, please enter a valid task name.")

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

    def filter_tasks_by_status():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)
        file.close()

        while True:
            status = input("Enter status to filter by (completed/incomplete): ").lower()
            if status in ['Completed', 'Incompleted']:
                break
            else:
                print("Invalid status, please enter 'Completed' or 'Incompleted'.")

        filtered_tasks = [task for task in tasks if task['status'].lower() == status]

        if filtered_tasks:
            print(f"Filtered tasks ({len(filtered_tasks)}):")
            for task in filtered_tasks:
                print(task)
        else:
            print("No tasks found with the status: " + status)

    def search_task_by_title():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)
        file.close()

        title = input("Enter the title of the task to search for: ")
        found_tasks = [task for task in tasks if task['title'].lower() == title.lower()]

        if found_tasks:
            print("Tasks found:")
            for task in found_tasks:
                print(task)
        else:
            print("No tasks found with the title: " + title)

    def update_priority():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)
        file.close()

        title = input("Enter the title of the task to update priority: ")
        for item in tasks:
            if item["title"] == title:
                new_priority = input("Enter new priority: ")
                item['priority'] = new_priority
                print("Task priority updated successfully.")
                break
        else:
            print("Task not found!")

        file = open("Project_2_json.json", "w")
        json.dump(tasks, file, indent=2)
        file.close()

    def add_notes():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)
        file.close()

        title = input("Enter the title of the task to add notes: ")
        for item in tasks:
            if item["title"] == title:
                notes = input("Enter notes: ")
                item['notes'] = notes
                print("Notes added successfully.")
                break
        else:
            print("Task not found!")

        file = open("Project_2_json.json", "w")
        json.dump(tasks, file, indent=2)
        file.close()

    def task_statistics():
        file = open("Project_2_json.json", "r")
        tasks = json.load(file)
        file.close()

        total_tasks = len(tasks)
        completed_tasks = len([task for task in tasks if task['status'].lower() == 'completed'])
        incomplete_tasks = total_tasks - completed_tasks

        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Incomplete tasks: {incomplete_tasks}")
