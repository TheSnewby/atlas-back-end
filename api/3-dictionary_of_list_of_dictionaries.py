#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests
import urllib


url_todos = 'https://jsonplaceholder.typicode.com/todos/'
url_users = 'https://jsonplaceholder.typicode.com/users/'

users = requests.get(url_users).json()  # get list of dicts of users
userlist = []
for user in users:
    userlist.append(user['username'])
todos = requests.get(url_todos).json()  # get list of dicts of todos

user_data = []  # list of todos for current user
current_id = 0
data_json = {}
task_list = {}

for todo in todos:  # cycles through all todos and commits user_data
    if (current_id + 1) != todo["userId"]:
        data_json[str(current_id + 1)] = user_data  # commit userdata
        current_id = todo["userId"] - 1  # set new current id
        task_list = {}  # reset vars
        user_data = []
    task_list['username'] = userlist[current_id]
    task_list["task"] = todo['title']
    task_list['completed'] = todo['completed']
    user_data.append(task_list)
data_json[str(current_id + 1)] = user_data  # commits last user data

with open('todo_all_employees.json', 'w', newline='') as f:
    f.write(json.dumps(data_json))
