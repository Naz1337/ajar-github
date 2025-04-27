# todo_app.py - Collaborative To-Do List Application

# --- Data Storage ---
# Shared list to store tasks. Initially empty.
# This list will be passed to the functions that need it.
tasks = []

# --- Function Definitions ---

def add_task(task_list):
    """
    WORK UNIT 1 (Assigned to Person 1):
    - Prompt the user to enter a new task description.
    - Add the task string to the end of the provided 'task_list'.
    - Print a confirmation message indicating the task was added.
    """
    print("\n--- Add Task ---")
    # TODO: Person 1 implement this function
    print("Function 'add_task' needs implementation.")
    # Example:
    # task_description = input("Enter the task description: ")
    # if task_description: # Basic check if something was entered
    #     task_list.append(task_description)
    #     print(f"Task '{task_description}' added successfully.")
    # else:
    #     print("No task description entered.")
    pass # Remove this line once implemented


def view_tasks(task_list):
    """
    WORK UNIT 2 (Assigned to Person 2):
    - Check if the 'task_list' is empty.
    - If it's empty, print a message like "Your to-do list is empty!".
    - If it's not empty, print a numbered list of all tasks currently in 'task_list'.
      (e.g., "1. Buy groceries", "2. Walk the dog")
    """
    print("\n--- View Tasks ---")
    # TODO: Person 2 implement this function
    print("Function 'view_tasks' needs implementation.")
    # Example:
    # if not task_list:
    #     print("Your to-do list is empty!")
    # else:
    #     print("Current Tasks:")
    #     for index, task in enumerate(task_list):
    #         print(f"{index + 1}. {task}")
    pass # Remove this line once implemented


def remove_task(task_list):
    """
    WORK UNIT 3 (Assigned to Person 3):
    - First, display the current tasks using logic similar to view_tasks
      (or potentially call view_tasks if available and merged). This helps the user know which number to remove.
    - If the list is empty, print a message like "No tasks to remove." and return.
    - Prompt the user to enter the *number* of the task they want to remove.
    - Convert the input to an integer index (remembering lists are 0-indexed, so subtract 1).
    - Add error handling:
        - Check if the input is a valid number.
        - Check if the number is within the valid range of task indices (0 to len(task_list) - 1).
    - If the input is valid, remove the task at that index from 'task_list' using pop().
    - Print a confirmation message showing the removed task or an error message if input was invalid.
    """
    print("\n--- Remove Task ---")
    # TODO: Person 3 implement this function
    print("Function 'remove_task' needs implementation.")
    # Example (needs robust error handling):
    # if not task_list:
    #     print("No tasks to remove.")
    #     return
    #
    # print("Current Tasks:") # Display tasks first
    # for index, task in enumerate(task_list):
    #      print(f"{index + 1}. {task}")
    #
    # try:
    #     task_num_str = input(f"Enter the number of the task to remove (1-{len(task_list)}): ")
    #     task_index = int(task_num_str) - 1 # Convert to 0-based index
    #
    #     if 0 <= task_index < len(task_list):
    #         removed_task = task_list.pop(task_index)
    #         print(f"Task '{removed_task}' removed successfully.")
    #     else:
    #         print("Invalid task number. Please enter a number from the list.")
    # except ValueError:
    #     print("Invalid input. Please enter a number.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    pass # Remove this line once implemented


def main_menu(task_list):
    """
    WORK UNIT 4 (Assigned to Person 4):
    - Display a welcome message and the main menu options:
        1. Add Task
        2. View Tasks
        3. Remove Task
        4. Quit
    - Start a loop that continues until the user chooses to Quit (e.g., option '4').
    - Inside the loop:
        - Prompt the user to enter their choice (1-4).
        - Based on the choice:
            - If '1', call the 'add_task' function, passing 'task_list'.
            - If '2', call the 'view_tasks' function, passing 'task_list'.
            - If '3', call the 'remove_task' function, passing 'task_list'.
            - If '4', print a goodbye message and break the loop (or exit).
            - If the choice is invalid, print an error message.
    """
    print("\n--- Simple To-Do List Application ---")
    # TODO: Person 4 implement this function (basic structure provided)
    print("Function 'main_menu' needs implementation (main loop and calls).")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Call the function implemented by Person 1
            add_task(task_list)
        elif choice == '2':
            # Call the function implemented by Person 2
            view_tasks(task_list)
        elif choice == '3':
            # Call the function implemented by Person 3
            remove_task(task_list)
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break # Exit the while loop
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# --- Main Execution ---
if __name__ == "__main__":
    # This is the entry point of the script.
    # It initializes the task list (already done above as a global variable)
    # and starts the main menu loop by calling main_menu.
    print("Welcome to the Collaborative To-Do App!")
    # The main_menu function (Person 4's work) will handle the application flow.
    main_menu(tasks)
