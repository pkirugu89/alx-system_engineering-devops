#!/usr/bin/python3
"""
Script that fetches TODP list progess for a given employee ID
and exports the data in csv format.
"""

import csv
import requests
import sys


def export_employee_todo(employee_id):
    """
    Fetches and exports TODO list for a employee ID in csv format
    Args:
        employee_id (int): The ID of the employee.
    Returns:
        Employee completed tasks in csv.
    """
    # API URL
    url = "https://jsonplaceholder.typicode.com/"
    # URL Link that fetches employee data based on employee id
    e_url = "{}/users/{}".format(url, employee_id)
    # GET request to fetch employee data
    response = requests.get(e_url)
    # Extract employee data in a JSON response
    employee_info = response.json()
    # Check if employee data exists for a given ID
    if "id" not in employee_info:
        print("Employee not found")
        return

    # URL link to fetch TODO list for the employee
    todo_url = "{}/todos?userId={}".format(url, employee_id)
    # GET request to fetch TODO list
    todo_response = requests.get(todo_url)
    # Extract TODO list in a JSON response
    todos = todo_response.json()

    # Extract employee name from the employee data
    employee_name = employee_info['name']
    # Create CSV file name based on employee ID
    csv_fmt = "{}.csv".format(employee_id)
    # Write task info to CSV file
    with open(csv_fmt, mode='w', newline='') as csv_file:
        for task in todos:
            csv_file.write(
                    '"{}","{}","{}","{}"\n'.format(
                        employee_id,
                        employee_name,
                        task.get('completed'),
                        task.get('title')
                    )
            )


if __name__ == "__main__":
    # Extract employee id from the cmd arguments
    employee_id = int(sys.argv[1])
    # Call the method to fetch and export TODO list
    export_employee_todo(employee_id)
