#!/usr/bin/python3

"""
This script fetches all employees' TODOs and exports them to
a JSON file in the required format.
"""

import json
import requests

if __name__ == "__main__":
    # API URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users
    users_response = requests.get(users_url)
    users = users_response.json()

    user_map = {user['id']: user['username'] for user in users}

    # Fetch all todos
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create result dictionary
    all_tasks = {}

    for task in todos:
        user_id = task['userId']
        task_data = {
            "username": user_map[user_id],
            "task": task['title'],
            "completed": task['completed']
        }

        # Append task to the user's task list
        if user_id not in all_tasks:
            all_tasks[user_id] = []
        all_tasks[user_id].append(task_data)

    # Write to JSON file
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)
