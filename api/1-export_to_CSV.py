#!/usr/bin/python3
"""
This module extracts data extends from file1
and save data to a csv file
"""

if __name__ == "__main__":
    import requests
    import sys
    import csv

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
        with open(f'{employee_id}.csv', 'w', newline='') as file:
            fieldnames = ['employee Id',
                          'employee name',
                          'Task Completed Status',
                          'Task Title'
                          ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            for tasks in todos:
                writer.writerow({
                    'employee Id': tasks['userId'],
                    'employee name': employee_name,
                    'Task Completed Status': tasks['completed'],
                    'Task Title': tasks['title']
                }
                )
    else:
        print(f"Failed to retrieve todos for employee {employee_id}")
