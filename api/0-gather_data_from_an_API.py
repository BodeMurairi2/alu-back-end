#!/usr/bin/python3
# This module extracts user todo list based on ID

import requests

api_url = "https://jsonplaceholder.typicode.com/todos/"

parameter = {
    'userID': 1
}

response = requests.get(api_url, params=parameter)

if response.status_code == 200:
    response_data = response.json()

count_done = 0

# count the number of completed tasks
for completion in response_data:
    if completion['completed'] is True:
        count_done += 1

# number of tasks
nbr_tasks = len(response_data)

# Display the report
print(f"Patricia Leshler is done with tasks({count_done}/{nbr_tasks})")
for completed_tasks in response_data:
    if completed_tasks['completed'] is True:
        print(f'\t {completed_tasks['title']}')
