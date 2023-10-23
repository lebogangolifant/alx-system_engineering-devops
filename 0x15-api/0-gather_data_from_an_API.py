#!/usr/bin/python3
"""
Python script that, using a REST API retrieves
and displays information about an employee's TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Get the employee ID from the command-line arguments
    employee_id = int(argv[1])  # Convert to integer

    # Construct the URLs for employee information and tasks
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"{employee_url}/todos"

    # Fetch the employee's information and tasks from the API
    employee_data = requests.get(employee_url).json()
    todos_data = requests.get(todos_url).json()

    # Extract the employee's name, completed tasks, and total tasks
    employee_name = employee_data.get("name")
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)

    # Prepare and print the progress message
    progress_message = (
        f"Employee {employee_name} is done with tasks("
        f"{len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        progress_message += f"\n\t {task.get('title')}"
    print(progress_message)
