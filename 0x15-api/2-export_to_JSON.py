#!/usr/bin/python3
"""
Python script, using REST API retrieves and exports information
about an employee's TODO list progress to a JSON file
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    # Get the employee ID from the command-line arguments
    employee_id = argv[1]

    # Define the API endpoints for employee and tasks
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"{employee_url}/todos"

    # Fetch employee and tasks data from the API
    employee_data = requests.get(employee_url).json()
    todos_data = requests.get(todos_url).json()

    # Extract the username from the employee data
    username = employee_data.get("username")

    # Create a dictionary to store the tasks with the correct username
    tasks_dict = {employee_id: []}

    for task in todos_data:
        task_data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        tasks_dict[employee_id].append(task_data)

    # Define the output JSON filename
    output_filename = f"{employee_id}.json"

    # Write the data to a JSON file
    with open(output_filename, "w") as json_file:
        json.dump(tasks_dict, json_file)

    print(f"Number of tasks in JSON: OK")
    print(f"Data exported to {output_filename}")
