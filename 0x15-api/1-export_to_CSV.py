#!/usr/bin/python3
"""
Python script that, using REST API retrieves and exports information
about an employee's TODO list progress in CSV format.
"""

import csv
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

    # Extract relevant data from the API responses
    user_id = employee_data.get("id")
    username = employee_data.get("username")
    tasks = []

    for task in todos_data:
        task_data = {
            "USER_ID": user_id,
            "USERNAME": username,
            "TASK_COMPLETED_STATUS": task.get("completed"),
            "TASK_TITLE": task.get("title"),
        }
        tasks.append(task_data)

    # Define the CSV header
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    # Export the data to a CSV file
    output_filename = f"{employee_id}.csv"

    with open(output_filename, "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=header,
                                    quoting=csv.QUOTE_ALL)
        csv_writer.writerows(tasks)

    print(f"User ID and Username: OK")
    print(f"Data exported to {output_filename}")
