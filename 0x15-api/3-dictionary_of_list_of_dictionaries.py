#!/usr/bin/python3
'''script that retrieves infromation about an employee using ID'''

import json
import requests

if __name__ == "__main__":
    usr_json = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            emp_id).json()
    todo_file = 'todo_all_employees.json'
    first_dict = {}


    for item in usr_json:
        sec_dict = {}
        sec_dict["task"] = item.get("title")
        sec_dict["completed"] = item.get("completed")
        sec_dict["usernae"] = emp_name
        first_dict.get(emp_id).append(sec_dict)

    with open(json_file, 'w') as jsfile:
        json.dump(first_dict, jsfile)
