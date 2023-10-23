#!/usr/bin/env python3
"""
Python script that, using REST API retrieves all employees data,
create a dictionary to store all tasks for each user
and export it to a JSON file.
"""

import json
import requests


def main():
    # Retrieve data for all employees from JSONPlaceholder API
    user_data = get_user_data()
    todo_data = get_todo_data()

    if user_data is None or todo_data is None:
        print("Failed to retrieve data. Exiting.")
        return

    # Create a dictionary to store tasks for each user
    all_tasks = {}

    # Organize tasks by user and add them to the all_tasks dictionary
    for todo in todo_data:
        user_id = todo["userId"]
        if user_id not in all_tasks:
            all_tasks[user_id] = []
        task = {
            "username": user_data[user_id]["username"],
            "task": todo["title"],
            "completed": todo["completed"]
        }
        all_tasks[user_id].append(task)

    # Write the all_tasks dictionary to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)


def get_user_data():
    # Retrieve user data from JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve user data.")
        return None

    user_data = {}
    for user in response.json():
        user_data[user["id"]] = {
            "username": user["username"]
        }
    return user_data


def get_todo_data():
    # Retrieve TODO data from JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve TODO data.")
        return None

    return response.json()


if __name__ == "__main__":
    main()
