'''
# todo
Simple to do application
Overview

In this project, you will build a functional To-Do List Application using Python from scratch. This assignment will help you strengthen your understanding of Python concepts such as syntax, data types, control structures, functions, and error handling, all while creating a practical, interactive command-line application.

Project

In VS Code, create a .py file and complete the following requirements:

User Interface (UI) and Storage Method
Build a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.
The tasks should be stored in a Python list
Core Features
Add tasks
View tasks
Delete tasks
Quit the application
User Interaction
Use input() to capture user selections and ensure proper input validation to handle invalid choices.
Error Handling
Implement error handling using try, except, else, and finally blocks to catch errors
Alert the user if they provide invalid input
Alert the user if there are no tasks to view
Alert the user if they try to delete a task that doesn't exist
Alert the user if they select an option on the main menu that doesn't exist
Code Organization
Organize your code into functions to improve clarity and maintainability. 
Use descriptive function names and add comments/docstrings where necessary.
Testing and Debugging
Thoroughly test your application, considering edge cases such as empty lists and invalid input.
Submission Guidelines:
Ensure the code is ready to run and that all functionality, such as loops, conditionals, and functions, works as expected when executed. The goal is to have fully tested and functional code.
Create a GitHub repository to host your project. Add, commit, and push your code to it
Create a README.md on the repository that gives information about your project and how to run/use it
Submit the repository link in Google Classroom.

'''
# Present choices 
def display_choice():
    """Displays the menu with available options."""
    print("\n===========================================")
    print("\n------------Welcome!!---------------")
    print("\n------ To-Do List Application ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit and Exit Application")
    print("\n===========================================")


def add_task(tasks):
    # Adds a new task to the to-do list.
    task = input("Enter the task to add: ")
    if task.strip():  # Ensures task is not empty.Both Leading and trailing whitespce
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("Error: Task cannot be empty.")


def view_tasks(tasks):
    # Displays the list of tasks."""
    if tasks:
        print("\n------- List of Tasks -----------------")
        # Loops through task and assigns a number to each task that was added
        for task_id, task in enumerate(tasks, 1): 
            print(f"{task_id}. {task}")
    else:
        print("----------No tasks to view. ---------")


def delete_task(tasks):
    # Deletes a task from  list.
    if not tasks:
        print("No tasks to delete.")
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully.")
        else:
            print("Error: Task number out of range.")
    except ValueError:
        print("Error: Invalid input, please enter the number of the task.")


def main():
    #  Main function of the application."""
    tasks = []  # Initialize empty List to store tasks
    while True:
        display_choice()
        try:
            choice = int(input("Choose an option/number: "))
            # this will execute the corresponding function chosen by the user
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                print("Exiting the application!")
                break
            else:
                print("Error: Invalid - Please choose a valid option/number.")
        except ValueError:
            print("Error: Invalid - Please enter a number between 1 and 4.")
        
# Standard way of calling main function 
if __name__ == "__main__":
    main()