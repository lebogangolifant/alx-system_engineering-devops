#!/usr/bin/python3
"""
Python script that, using REST API retrieves and exports information
about an employee's TODO list progress in CSV format.
"""

import requests
import sys
import csv


def get_employee_progress(employee_id):
    # Define the API base URL
    api_url = 'https://jsonplaceholder.typicode.com'

    # Construct the URLs for user and TODO data
    user_uri = f'{api_url}/users/{employee_id}'
    todo_uri = f'{user_uri}/todos'

    # Fetch user data
    user_response = requests.get(user_uri)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch user's TODO tasks
    todo_response = requests.get(todo_uri)
    if todo_response.status_code != 200:
        print("Failed to fetch user's tasks")
        sys.exit(1)
    todo_data = todo_response.json()

    return employee_name, todo_data


def export_to_csv(employee_name, todo_data, employee_id):
    # Define the CSV file name
    csv_filename = f"{employee_id}.csv"

    # Open the CSV file for writing
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the CSV header
        writer.writeheader()

        # Write task data to the CSV file
        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 task_1.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)

    employee_name, todo_data = get_employee_progress(employee_id)

    # Export data to CSV file
    export_to_csv(employee_name, todo_data, employee_id)
    print(f"Data exported to {employee_id}.csv")
