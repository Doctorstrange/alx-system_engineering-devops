#!/usr/bin/python3
"""Accessing todo lists of employees"""

import json
import requests
import sys

if __name__ == '__main__':
    empId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + empId

    response = requests.get(url)
    empuser = response.json().get('username')

    toUrl = url + "/todos"
    response = requests.get(toUrl)
    tasks = response.json()

    dic = {empId: []}
    for task in tasks:
        dic[empId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": empuser
        })
    with open('{}.json'.format(empId), 'w') as f:
        json.dump(dic, f)
