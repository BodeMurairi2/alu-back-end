#!/usr/bin/python3
"""
This script exports all tasks for a given employee ID
to a JSON file in the required format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)

    username = user_response.json().get("username")

    # Get user's todos
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    tasks = todos_response.json()

    # Format JSON data
    user_tasks = []
    for task in tasks:
        user_tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    result = {employee_id: user_tasks}

    # Write to JSON file
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(result, json_file)
