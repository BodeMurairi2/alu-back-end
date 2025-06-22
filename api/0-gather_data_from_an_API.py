#!/usr/bin/python3
# This module extracts a user's todo list based on their ID

if __name__ == "__main__":
    import requests
    import sys
    
    # Define API URL and parameters
    api_url = "https://jsonplaceholder.typicode.com/todos"
    employeeId = sys.argv[1]
    parameters = {
        'userId': employeeId
        }
    # Fetch data from API
    response = requests.get(api_url, params=parameters)
    if response.status_code == 200:
        todos = response.json()
        # Count completed tasks
        completed_tasks = [task for task in todos if task.get('completed')]
        count_done = len(completed_tasks)
        nbr_tasks = len(todos)

        # Display the report
        print(
            f"Employee {employeeId} is done with tasks "
            f"({count_done}/{nbr_tasks}):"
        )
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
    else:
        print(f"Failed to retrieve data: Status code {response.status_code}")
