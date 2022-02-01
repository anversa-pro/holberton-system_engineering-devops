#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    user_i = sys.argv[1]
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(user_i))
    todo_s = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_s = todo_s.json()

    todoUser = {}
    taskList = []

    for task in todo_s:
        if task.get('userId') == int(user_i):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": usr.json().get('username')}
            taskList.append(taskDict)
    todoUser[user_i] = taskList

    filename = user_i + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
