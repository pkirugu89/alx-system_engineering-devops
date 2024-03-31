#!/usr/bin/python3
"""
Script that fetches TODO list progress for a given employee ID
and export the details to a json file.
"""


import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and export TODO list progress in JSON format.
    Args:
        employee_id (int): ID for a given employee.
    Return:
        Employee completed TODO list.
    """
    # URL to fetch employee data based on employee ID
    url = "https://jsonplaceholder.typicode.com/"
    user = "{}/users/{}".format(url, employee_id)
    # GET request to fetch employee data
    response = requests.get(user)
    # Extract JSON Response
    employee_info = response.json()

    # URL to fetch TODO list for the employee
    todo = "{}/todos?userId={}".format(url, employee_id)
    # GET request to fetch TODO list
    todo_response = requests.get(todo)
    # Extract JSON response with the TODO list
    todos = todo_response.json()

    # Extract employee name from employee info
    employee_name = employee_info['name']
    # Create a JSON file name based on employee id
    json_file = "{}.json".format(employee_id)
    # Prepare data for JSOn export
    data_export = {str(employee_id): []}
    for task in todos:
        data_export[str(employee_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })
    # Write task details to JSON file
    with open(json_file, 'w') as file_json:
        json.dump(data_export, file_json,)
    # print(f"Data exported to {json_file}")


if __name__ == "__main__":
    # Extract employee ID from the cmd arguments
    employee_id = int(sys.argv[1])
    # Call the function to fetch and export TODO list
    get_employee_todo_progress(employee_id)
