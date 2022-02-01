#!/usr/bin/python3
"""Export data to json format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    usr = requests.get("https://jsonplaceholder.typicode.com/users")
    usr = usr.json()
    todo_s = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_s = todo_s.json()
    todo_A = {}

    for user in usr:
        taskList = []
        for task in todo_s:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todo_A[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_A, f)
