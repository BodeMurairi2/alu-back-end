#!/usr/bin/python3
"""
This script fetches a user's TODO list and exports it to a CSV file
in the exact format expected by the ALX checker: no header, quoted fields.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)

    username = user_response.json().get('username')

    # Fetch todos
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url, params={'userId': employee_id})
    if todos_response.status_code != 200:
        print(f"Failed to retrieve todos for employee {employee_id}")
        sys.exit(1)

    tasks = todos_response.json()

    # Write to CSV (NO HEADER, FIELDS QUOTED)
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = [
            'USER_ID',
            'USERNAME',
            'TASK_COMPLETED_STATUS',
            'TASK_TITLE'
        ]
        writer = csv.DictWriter(csvfile,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL
                                )

        for task in tasks:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })
