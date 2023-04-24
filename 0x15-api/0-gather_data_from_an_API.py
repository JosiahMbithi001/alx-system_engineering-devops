#!/usr/bin/python3
"""
This Script gets Dta from a URL &
Prints Titles An Employee has Written
"""
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
    user_name = user_dict.get("name")

    """Gets The Emloyees To Do"""
    user_todo = requests.get(todo_url)

    user_todo = user_todo.json()

    for item in user_todo:
        if item.get("userId") == int(user_id):
            total_tasks += 1
            if item.get("completed") is True:
                done_tasks += 1
                employee_titles.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(user_name,
          done_tasks, total_tasks))

    for title in employee_titles:
        print("\t {}".format(title))
