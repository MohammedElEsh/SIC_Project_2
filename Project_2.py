from Project_2_classes import *


def main():
    while True:
        print("******************** Welcome to Task Manager system ********************\n"
              "[1] Add task\n"
              "[2] Delete a task\n"
              "[3] Show list of tasks\n"
              "[4] Update deadline date\n"
              "[5] Mark task as completed\n"
              "[6] Update task priority\n"
              "[7] Filter tasks by status\n"
              "[8] Search task by title\n"
              "[9] Add notes to a task\n"
              "[10] Display task statistics\n"
              "[11] Quit")
        while True:
            try:
                choice = int(input("Please enter your choice "))
            except ValueError:
                print("Enter a valid value!")
            else:
                break
        if choice in range(1, 12):
            if choice == 1:
                TaskManager.add_task()
                print("The task has been added successfully.")
            elif choice == 2:
                TaskManager.delete_task()
                print("The task has been deleted successfully.")
            elif choice == 3:
                TaskManager.view_tasks()
                print("Tasks have been displayed successfully.")
            elif choice == 4:
                TaskManager.update_deadline_date()
                print("The deadline date has been updated successfully.")
            elif choice == 5:
                TaskManager.mark_task_as_completed()
                print("The task has been marked as completed successfully.")
            elif choice == 6:
                TaskManager.update_priority()
                print("The task priority has been updated successfully.")
            elif choice == 7:
                TaskManager.filter_tasks_by_status()
                print("Tasks have been filtered by status successfully.")
            elif choice == 8:
                TaskManager.search_task_by_title()
                print("Task search by title completed successfully.")
            elif choice == 9:
                TaskManager.add_notes()
                print("Notes have been added to the task successfully.")
            elif choice == 10:
                TaskManager.task_statistics()
                print("Task statistics have been displayed successfully.")
            elif choice == 11:
                print("Thanks For Using Our System ")
                break
        else:
            print("Enter a valid Number!")


main()