# Collaborative Command-Line To-Do List App

## Project Overview

This is a simple command-line To-Do list application written in Python. Its primary purpose is to serve as an exercise for learning and practicing collaborative development workflows using Git and GitHub.

The project is intentionally structured with distinct functions (`add_task`, `view_tasks`, `remove_task`, `main_menu`) that can be implemented independently by different collaborators.

## Features

* **Add Tasks:** Add new tasks to your to-do list.
* **View Tasks:** Display all current tasks in a numbered list.
* **Remove Tasks:** Remove specific tasks from the list by their number.
* **Command-Line Interface:** Interact with the application through simple text commands in your terminal.

## Getting Started

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    Replace `<repository_url>` with the actual URL of your GitHub repository and `<repository_directory>` with the name of the folder created by cloning.

2.  **Ensure Python is Installed:**
    This application requires Python 3.x. You can check your Python version by running:
    ```bash
    python --version
    # or
    python3 --version
    ```

## Running the Application

Once you have cloned the repository and have Python installed, navigate to the project directory in your terminal and run the script:

```bash
python todo_app.py
or if python points to Python 2 on your system:python3 todo_app.py
Follow the on-screen menu prompts to interact with the To-Do list.Collaboration Exercise GuideThis repository is designed for a 4-person collaboration exercise:Initial Setup:One person creates the GitHub repository and pushes the initial todo_app.py skeleton code.All collaborators are invited to the repository.Everyone clones the repository locally.Task Assignment:Person 1: Implement add_task function.Person 2: Implement view_tasks function.Person 3: Implement remove_task function.Person 4: Implement main_menu function (main application loop).Development Workflow (for each person):Create a Branch: Create a new branch for your feature (e.g., git checkout -b feature/add-task).Implement: Write the code for your assigned function.Commit: Commit your changes (git add todo_app.py, git commit -m "Implement add_task").Push: Push your branch to GitHub (git push origin feature/add-task).Pull Request (PR): Create a Pull Request on GitHub from your feature branch to the main branch.Review: Other team members review the PR, provide feedback, and approve.Merge: Once approved, merge the PR into the main branch.Update: Everyone should regularly pull the latest changes from the main branch (git checkout main, git pull origin main).Merge Conflicts: Be prepared to resolve merge conflicts if multiple people edit overlapping parts of the code.File Structure.
├── todo_app.py     # The
