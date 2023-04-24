#!/usr/bin/python3
"""
This Script gets Dta from a URL &
Prints Titles An Employee has Written in CSV Format
and Exports to A CSV Formst
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]
    done_tasks = 0
    total_tasks = 0
    employee_titles = []

    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    """Gets Data from URL in Json Format"""
    user_dict = requests.get(user_url).json()

    """Gets the Name of Employee"""
    user_name = user_dict.get("username")

    """Gets The Emloyees To Do"""
    user_todo = requests.get("{}/todos".format(user_url))

    """Convert User To_Do tojson Format"""
    user_todo = user_todo.json()

    """Output FileName"""
    file_output = user_id + ".csv"

    with open(file_output, 'w') as csvfile:
        for item in user_todo:
            csvfile.write('"{}","{}","{}","{}"\n'.format(item.get('userId'),
                                                         user_name, item.get(
                                                             'completed'),
                                                         item.get('title')))
