#!/usr/bin/python3
"""
Gathers data fron APT and shows TODO list for employee ID
"""

import requests
from sys import argv

if __name__ == '__main__':
    # Checks if number of args is provided
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    base_url = "http://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]
        total_tasks = len(todos_data)

        print("Employee {} is done with tasks({}/{}):".format(
            user_data['name'], len(completed_tasks), total_tasks))

        for task in completed_tasks:
            print("\t {}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))