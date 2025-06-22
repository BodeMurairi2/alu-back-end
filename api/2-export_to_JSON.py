#!/usr/bin/python3
"""
This module extracts a user's todo list based on their ID
and displays their completed tasks using the JSONPlaceholder API.
"""

if __name__ == "__main__":
    import requests
    import sys
    import json

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Get user name
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = user_response.json().get('name')

    # Get todos
    response = requests.get(todos_url, params={'userId': employee_id})
    if response.status_code == 200:
        todos = response.json()
        filename = f'{employee_id}.json'
        # create an empty list to store tasks
        users_todos = []
        for task in todos:
            user_tasks = {
                "tasks": task['title'],
                "completed": task['completed'],
                "username": employee_name
                }
            users_todos.append(user_tasks)
        employee_tasks = {
            str(employee_id): users_todos
            }
        print(len(employee_tasks[str(employee_id)]))

#        with open(filename, 'w') as file:
#            json.dump(employee_tasks, file)

    else:
        print(f"Failed to retrieve todos for employee {employee_id}")
