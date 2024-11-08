#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys
import urllib


if len(sys.argv) > 1:
    employee_id = int(sys.argv[1])
    url_todos = 'https://jsonplaceholder.typicode.com/todos/'
    url_users = 'https://jsonplaceholder.typicode.com/users/'

    users = requests.get(url_users).json()
    for user in users:
        if user['id'] == employee_id:
            employee_name = user["name"]
            break
    # print("Employee Name: {}".format(employee_name))
    todos = requests.get(url_todos).json()
    todo_count = 0
    todo_success_count = 0
    todo_list = []
    for todo in todos:
        # print("TODO: {}".format(todo))
        if todo['userId'] == employee_id:
            # print("TODO: {}".format(todo))
            if todo['completed']:
                todo_list.append(todo["title"])
                todo_success_count += 1
            todo_count += 1
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          todo_success_count,
                                                          todo_count))
    for todo in todo_list:
        print("\t {}".format(todo))
