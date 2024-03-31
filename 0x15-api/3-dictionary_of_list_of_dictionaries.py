#!/usr/bin/python3
"""
Script that exports all TODO list for employees in JSON format
"""


import json
import requests
import sys


if __name__ == "__main__":
    # Fetch all user data from the API link
    url = "https://jsonplaceholder.typicode.com"
    users_link = "{}/users".format(url)
    u_response = requests.get(users_link)
    user_info = u_response.json()

    # Initilaize a dict to store all users tasks
    all_tasks = {}

    # Iterate over each user and fetch their tasks.
    for user in user_info:
        uid = str(user['id'])
        uname = user['username']

        # Fetch tasks data for the current user
        tasks_link = "{}/todos?userId={}".format(url, uid)
        t_response = requests.get(tasks_link)
        task_info = t_response.json()

        # Intialize a list to store current user tasks
        user_tasks = []

        # Iterate over each task of the current user
        for task in task_info:
            t_dict = {
                    'username': uname,
                    'task': task['title'],
                    'completed': task['completed']
                    }
            user_tasks.append(t_dict)

        # Add to the task list for the current user to the dict
        all_tasks[uid] = user_tasks

    # Write all tasks info to a JSON file
    with open('todo_all_employee.json', 'w') as json_file:
        json.dump(all_tasks, json_file)
