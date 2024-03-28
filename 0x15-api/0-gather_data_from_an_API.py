#!/usr/bin/python3
"""
Fetches TODO list progress for
a given employee ID using REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display TODO list progress for a given employee ID.
    Args:
        employee_id (int): ID for a given employee.
    Returns:
        status of TODO list.
    """
    # Link to the employee data from typicode website
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # Link to the todo list for each employee id
    todo_url = f"\
            https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    # GET request to fetch Employeee details
    response = requests.get(url)
    # Extract JSON response from the above GET request
    employee_info = response.json()
    # Check if the employee id exists
    if "id" not in employee_info:
        print("Employee not found")
        return

    # GET request to fetch TODO task details.
    response_todo = requests.get(todo_url)
    # Extract JSON response from the above GET request
    todos = response_todo.json()

    # Get completed tasks from the TODO list
    done_tasks = [todo for todo in todos if todo['completed']]
    # The total count for all tasks in the TODO list
    all_tasks = len(todos)
    # The count of completed tasks from the TODO list
    num_done_tasks = len(done_tasks)
    # Extract the employee name from the employee data
    employee_name = employee_info['name']

    # Display TODO list progress in specified format
    print(f"Employee {employee_name} is done with tasks\
            ({all_tasks}/{num_done_tasks}):")
    # Print titles of the completed tasks
    for task in todos:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    # Check if the correct argument number is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    # Extract employee ID from the arguments
    employee_id = int(sys.argv[1])
    # Call the function to display TODO list progress
    get_employee_todo_progress(employee_id)
