#!/usr/bin/python3
"""
Export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Get user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Get tasks for the user
    tasks_response = requests.get(url, params={"userId": user_id})
    tasks_data = tasks_response.json()

    # Create a dictionary to store tasks
    user_tasks = {user_id: []}

    # Populate the dictionary with task information
    for task in tasks_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        user_tasks[user_id].append(task_info)

    # Save the data to a JSON file
    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(user_tasks, json_file)