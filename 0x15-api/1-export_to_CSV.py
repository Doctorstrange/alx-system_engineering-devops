#!/usr/bin/python3
"""Accessing todo lists of employees"""

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
    with open('{}.csv'.format(empId), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(empId, empuser, task.get('completed'),
                            task.get('title')))
