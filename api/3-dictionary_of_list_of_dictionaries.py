#!/usr/bin/python3
""" Export data in the JSON format."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    response_users = requests.get(users_url)
    response_todos = requests.get(todos_url)

    if response_users.status_code != 200 or response_todos.status_code != 200:
        print("Error: Unable to fetch data from JSONPlaceholder API")
    else:
        users = response_users.json()
        todos = response_todos.json()

        todo_all_employees = {}

        for user in users:
            user_id = str(user.get("id"))
            username = user.get("username")

            user_todos = [
                {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
                for todo in todos
                if todo.get("userId") == user.get("id")
            ]

            todo_all_employees[user_id] = user_todos

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(todo_all_employees, json_file)
