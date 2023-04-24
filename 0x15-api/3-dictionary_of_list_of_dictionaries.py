#!/usr/bin/python3
"""
This Script Displays all records of Employees
i.e userId, Username, Task, Comletion Status
and gets the Output to todo_all_dicitonaries.json
"""
import json
import requests

if __name__ == '__main__':

    user_url = "https://jsonplaceholder.typicode.com/users/"
    user_dict = requests.get(user_url).json()
    file_output = "todo_all_employess.json"
    my_dict = {}

    for item in user_dict:
        user_id = str(item.get("id"))
        user_name = item.get("username")
        user_data = requests.get("{}{}/todos".format(user_url, user_id))
        user_data = user_data.json()
        my_dict[user_id] = []
        for elem in user_data:
            in_dict = {}
            in_dict["username"] = user_name
            in_dict["task"] = elem.get("title")
            in_dict["completed"] = elem.get("completed")
            my_dict[user_id].append(in_dict)

    with open(file_output, 'w') as f:
        json.dump(my_dict, f)
