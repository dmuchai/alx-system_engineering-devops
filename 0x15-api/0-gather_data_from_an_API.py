#!/usr/bin/python3
"""
This script fetches and displays TODO list progress of a given employee
using a REST API.
"""

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

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = [task.get("title") for task in todos_data
                  if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task))
