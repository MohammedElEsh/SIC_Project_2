from Project_2_classes import *


def main():
    while True:
        print("******************** Welcome to Task Manager system ********************\n"
              "[1] Add task\n"
              "[2] Delete a task\n"
              "[3] Show list of tasks\n"
              "[4] Update due date\n"
              "[5] Mark task as completed\n"
              "[6] Quit")
        while True:
            try:
                choice = int(input("Please enter your choice "))
            except ValueError:
                print("Enter a valid value!")
            else:
                break
        if choice in range(1, 7):
            if choice == 1:
                TaskManager.add_task()
                print("Task added successfully.")
            elif choice == 2:
                TaskManager.delete_task()
            elif choice == 3:
                TaskManager.view_tasks()
            elif choice == 4:
                TaskManager.update_due_date()
            elif choice == 5:
                TaskManager.mark_task_as_completed()
            elif choice == 6:
                print("Thanks For Using Our System ")
                break
        else:
            print("Enter a valid Number!")


main()