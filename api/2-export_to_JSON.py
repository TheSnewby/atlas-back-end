#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys
import urllib


if len(sys.argv) > 1:  # ensure script has an input
    employee_id = int(sys.argv[1])
    url_todos = 'https://jsonplaceholder.typicode.com/todos/'
    url_users = 'https://jsonplaceholder.typicode.com/users/'

    users = requests.get(url_users).json()  # get list of dicts of users
    for user in users:
        if user['id'] == employee_id:
            username = user["username"]  # establish name
            break
    todos = requests.get(url_todos).json()  # get list of dicts of todos

    data = []  # list of todos for json

    for todo in todos:
        if todo['userId'] == employee_id:  # add rows to csv
            new_row = {}
            new_row["task"] = todo['title']
            new_row['completed'] = todo['completed']
            new_row['username'] = username
            data.append(new_row)

    data_json = {}
    data_json['{}'.format(employee_id)] = data

    with open('{}.json'.format(employee_id), 'w', newline='') as f:
        f.write(json.dumps(data_json))
