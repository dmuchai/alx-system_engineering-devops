#!/usr/bin/python3
"""
This script fetches TODO list progress of a given employee
and exports the data to a JSON file..
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if not user_data or not todos_data:
        print("No data found for Employee ID:", employee_id)
        sys.exit(1)

    employee_name = user_data.get("username")

    total_tasks = len(todos_data)
    done_tasks = [task.get("title") for task in todos_data
                  if task.get("completed")]

    # Build JSON structure
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
            })

    json_data = {str(employee_id): tasks_list}

    with open("{}.json".format(employee_id), mode="w") as file:
        json.dump(json_data, file)
