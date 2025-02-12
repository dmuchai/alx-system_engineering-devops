#!/usr/bin/python3
"""
Fetches all employees' TODO list data from a REST API
and exports it to a JSON file.
"""

import json
import requests


if __name__ == "__main__":
    # Define API URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch data from the API
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Create a dictionary to store all tasks per user
    all_tasks = {}

    # Organize tasks under their respective users
    for user in users:
        user_id = str(user["id"])
        username = user["username"]
        all_tasks[user_id] = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos if task["userId"] == user["id"]
        ]

    # Write data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)
