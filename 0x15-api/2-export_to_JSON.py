#!/usr/bin/python3
'''script that retrieves infromation about an employee using ID'''

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    usr_json = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            emp_id).json()
    emp_name = usr_json.get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         emp_id + '/todos').json()

    json_file = emp_id + '.json'
    first_dict = {}

    first_dict[emp_id] = []

    for item in todos:
        sec_dict = {}
        sec_dict["task"] = item.get("title")
        sec_dict["completed"] = item.get("completed")
        sec_dict["usernae"] = emp_name
        first_dict.get(emp_id).append(sec_dict)

    with open(json_file, 'w') as jsfile:
        json.dump(first_dict, jsfile)
