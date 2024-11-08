#!/usr/bin/python3
"""Gather data from an API"""
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
            employee_name = user["name"]  # establish name
            break
    todos = requests.get(url_todos).json()  # get list of dicts of todos

    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    data = [header]  # list of rows for csv

    for todo in todos:
        if todo['userId'] == employee_id:
            data.append([str(employee_id),  # add rows to csv
                         employee_name,
                         todo['completed'],
                         todo['title']])

    with open('USER_ID.csv', 'wb') as f:  # create file and write csv
        writer = csv.writer(f)
        writer.writerows(data)
