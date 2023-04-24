#!/usr/bin/python3
"""
This Script gets Data from a URL &
Prints Titles An Employee has Written in json Format
and Exports to A json File
"""
import csv
import json
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
    file_output = user_id + ".json"

    """Dictionary Containing Date"""
    my_dict = {}
    my_dict[user_id] = []

    for item in user_todo:
        in_dict = {}
        in_dict["task"] = item.get("title")
        in_dict["completed"] = item.get("completed")
        in_dict["username"] = user_name
        my_dict[user_id].append(in_dict)

        with open(file_output, 'w') as f:
            json.dump(my_dict, f)
