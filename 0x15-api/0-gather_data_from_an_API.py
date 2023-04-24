#!/usr/bin/python3
'''script that retrieves infromation about an employee using ID'''

import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    usr_json = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            emp_id).json()
    emp_name = usr_json.get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    total_todo = 0
    completed_titles = []
    num_complete = 0

    for todo in todos:
        if todo.get("userId") == int(emp_id):
            total_todo += 1
            if todo.get("completed") is True:
                num_complete += 1
                completed_titles.append(todo.get("title"))
    print('Employee {} is done with tasks({}/{}):'.format(
        emp_name, num_complete, total_todo))
    for title in completed_titles:
        print('\t {}'.format(title))
