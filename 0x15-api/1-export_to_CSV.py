#!/usr/bin/python3
"""
This script fetches TODO list progress of a given employee
and exports the data to a CSV file..
"""
import csv
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

    # Open a CSV file for writing
    with open("{}.csv".format(employee_id), mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write CSV header
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write data rows
        for task in todos_data:
            user_id = task.get("userId")
            username = employee_name
            completed = task.get("completed")
            title = task.get("title")
            writer.writerow([user_id, username, completed, title])
