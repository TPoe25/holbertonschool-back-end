#!/usr/bin/python3
"""
Gathers data fron APT and shows TODO list for employee ID
"""
from sys import argv
import json 
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()

    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    todos = response.json()

    user_dict = {}
    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')
        tasks = [{"username": username, "task": task.get('title'), "completed": task.get('completed')} for task in todos if task.get('userId') == user.get('id')]
        user_dict[user_id] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_dict, jsonfile)