#!/usr/bin/python3
"""
Python script, using REST API retrieves and exports information
about an employee's TODO list progress to a JSON file
"""

import requests
import sys
import json


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


def export_to_json(employee_name, todo_data, employee_id):
    # Create a dictionary for JSON export
    json_data = {str(employee_id): []}

    # Populate the JSON data with tasks
    for task in todo_data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        }
        json_data[str(employee_id)].append(task_dict)

    # Define the JSON file name
    json_filename = f"{employee_id}.json"

    # Export data to JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {employee_id}.json")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 task_2.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)

    employee_name, todo_data = get_employee_progress(employee_id)

    # Export data to JSON file
    export_to_json(employee_name, todo_data, employee_id)
