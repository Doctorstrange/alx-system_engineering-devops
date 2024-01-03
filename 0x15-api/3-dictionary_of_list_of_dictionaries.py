#!/usr/bin/python3
"""Accessing todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    usrs = response.json()

    dic = {}
    for usr in usrs:
        usr_id = usr.get('id')
        usrname = usr.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dic[usr_id] = []
        for task in tasks:
            dic[usr_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": usrname
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dic, f)
