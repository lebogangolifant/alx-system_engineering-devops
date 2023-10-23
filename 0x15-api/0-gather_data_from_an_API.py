#!/usr/bin/python3
"""
Python script that, using a REST API retrieves
and displays information about an employee's TODO list progress.
"""

import requests
from sys import argv

# Check if the correct number of arguments is provided
if len(argv) != 2:
    print("Usage: python3 task_0.py <employee_id>")
    exit(1)

# Get the employee ID from the command line argument
employee_id = argv[1]

# Define the base API URL and the specific user and todo URLs
api_url = 'https://jsonplaceholder.typicode.com'
user_uri = f'{api_url}/users/{employee_id}'
todo_uri = f'{user_uri}/todos'

# Retrieve user data from the API
user_data = requests.get(user_uri).json()
employee_name = user_data.get('name')

# Retrieve the user's TODO list data from the API
todo_data = requests.get(todo_uri).json()
total_tasks = len(todo_data)
completed_tasks = sum(1 for task in todo_data if task["completed"])

# Display the employee's progress
progress_str = (
    f"Employee {employee_name} is done with tasks "
    f"({completed_tasks}/{total_tasks}):"
)
print(progress_str)

# Display the completed tasks
for task in todo_data:
    if task.get('completed'):
        print(f"\t{task.get('title')}")
