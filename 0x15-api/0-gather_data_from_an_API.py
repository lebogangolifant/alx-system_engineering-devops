#!/usr/bin/python3
"""
Python script that, using a REST API retrieves
and displays information about an employee's TODO list progress.
"""

import requests
import sys


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

    # Calculate the number of completed tasks and the total number of tasks
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    return employee_name, completed_tasks, total_tasks, todo_data


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 task_0.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)
    (employee_name, completed_tasks,
     total_tasks, todo_data) = get_employee_progress(employee_id)

    # Format and display the employee's progress
    progress_str = "Employee {} is done with tasks({}/{}):"
    print(progress_str.format(employee_name, completed_tasks, total_tasks))

    # Display completed tasks
    for task in todo_data:
        if task.get('completed'):
            print("\t" + task.get('title'))
