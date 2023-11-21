#!/usr/bin/python3
"""
Gathers data fron APT and shows TODO list for employee ID
"""
from sys import argv
import requests

if __name__ == '__main__':
    # Checks if number of args is provided
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)
        
    employee_id = argv[1]
    base_url = "http://jsonplaceholder.typicode.com"
    
    # User Info
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("username")
    
    # User's TODO list
    todo_response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    todo_data = todo_response.json()
    
    # Calculate the TODO progress
    total_tasks =  len(todo_data)
    completed_tasks = sum(task.get("completed") for task in todo_data)
    
    # Shows the list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task.get("completed"):
            print(f"\t{task.get('title')}")