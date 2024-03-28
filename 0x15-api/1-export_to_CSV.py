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
    # URL Link that fetches employee data based on employee id
    e_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # GET request to fetch employee data
    response = requests.get(e_url)
    # Extract employee data in a JSON response
    employee_info = response.json()
    # Check if employee data exists for a given ID
    if "id" not in employee_info:
        print("Employee not found")
        return

    # URL link to fetch TODO list for the employee
    todo_url = f"\
            https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    # GET request to fetch TODO list
    todo_response = requests.get(todo_url)
    # Extract TODO list in a JSON response
    todos = todo_response.json()

    # Extract employee name from the employee data
    employee_name = employee_info['name']
    # Create CSV file name based on employee ID
    csv_fmt = f"{employee_id}.csv"
    # Write task info to CSV file
    with open(csv_fmt, mode='w', newline='') as csv_file:
        flnames = [
                'USER_ID',
                'USERNAME',
                'TASK_COMPLETED_STATUS',
                'TASK_TITLE'
        ]
        wr = csv.DictWriter(csv_file, fieldnames=flnames)
        wr.writeheader()
        for task in todos:
            wr.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })
    # print(f"Data exported to {csv_file}")


if __name__ == "__main__":
    # check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_csv.py <employee_id>")
        sys.exit(1)

    # Extract employee id from the cmd arguments
    employee_id = int(sys.argv[1])
    # Call the method to fetch and export TODO list
    export_employee_todo(employee_id)
