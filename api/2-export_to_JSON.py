#!/usr/bin/python3
"""
Gathers data fron APT and shows TODO list for employee ID
"""
from sys import argv
import requests
import json

if __name__ == '__main__':
    # Checks number of args provided
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    base_url = "http://jsonplaceholder.typicode.com"

    # Users info
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("username")

    # User's TODO list
    todo_response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    todo_data = todo_response.json()

    # Prepares the data in JSON layout
    json_data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name,
            }
            for task in todo_data
        ]
    }

    # Write data to JSON file
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)