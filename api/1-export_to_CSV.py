#!/usr/bin/python3
"""
Gathers data fron APT and shows TODO list for employee ID
"""
from sys import argv
import requests
import csv


if __name__ == '__main__':
    # Checks if number of args is provided
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <employee_id>")
        exit(1)

    employee_id = argv[1]
    base_url = "http://jsonplaceholder.typicode.com"

    # User Info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("username")

    # User's TODO listß
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    #create CSV and wrtie data
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            csv_writer.writerow([employee_id, employee_name, str(task.get("completed")), task.get("title")])

    print(f"CSV file '{csv_file_name}' has been created.")
