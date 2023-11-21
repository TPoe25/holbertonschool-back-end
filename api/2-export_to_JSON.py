#!/usr/bin/python3
"""
Using what still doesn't work in task 0...
Extend your Python script to export data in the JSON format
"""
import json
import requests
import sys


def export_to_json(user_id):
    """Export employee progress to JSON"""
    url = "https://jsonplaceholder.typicode.com"
    empl_url = f"{url}/users/{user_id}"
    todo_url = f"{url}/todos"

    empl_data = requests.get(empl_url).json()
    todo_data = requests.get(todo_url, params={"userId": user_id}).json()

    empl_name = empl_data.get("name")
    user_name = empl_data.get("username")
    completed_tasks = [t["title"] for t in todo_data if t["completed"]]
    num_done = len(completed_tasks)
    num_total = len(todo_data)

    user_todo_list = []
    for task in todo_data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user_name
        }
        user_todo_list.append(task_dict)

    user_todo_dict = {f"{user_id}": user_todo_list}

    with open(f"{user_id}.json", "w") as f:
        json.dump(user_todo_dict, f)

    print("Employee {} is done with tasks({}/{}):"
          .format(empl_name, num_done, num_total))
    for todo in completed_tasks:
        print(f"\t {todo}")


if __name__ == "__main__":
    # Check the number of args
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Gets the user ID from command-line args
    user_id = int(sys.argv[1])

    # Calls export function
    export_to_json(user_id)