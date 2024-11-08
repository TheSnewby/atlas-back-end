#!/usr/bin/python3
"""Export to CSV"""
import csv
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

    # header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    data = []  # list of rows for csv

    for todo in todos:
        if todo['userId'] == employee_id:  # add rows to csv
            new_row = [str(employee_id), username,
                       str(todo['completed']), todo['title']]
            data.append(new_row)

    with open('{}.csv'.format(employee_id), 'w', newline='') as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(data)
