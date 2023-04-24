#!/usr/bin/python3
'''script that retrieves infromation about an employee using ID'''

import json
import requests

if __name__ == "__main__":
    usr_url = 'https://jsonplaceholder.typicode.com/users/'
    usr_json = requests.get(usr_url).json()
    todo_file = 'todo_all_employees.json'
    first_dict = {}

    for item in usr_json:
        emp_name = item.get("username")
        emp_id = str(item.get("id"))
        emp_data = requests.get("{}{}/todos".format(usr_url, emp_id)).json()
        first_dict[emp_id] = []
        for element in emp_data:
            sec_dict = {}
            sec_dict["task"] = element.get("title")
            sec_dict["completed"] = element.get("completed")
            sec_dict["username"] = emp_name
            first_dict[emp_id].append(sec_dict)

    with open(todo_file, 'w') as data_file:
        json.dump(first_dict, data_file)
