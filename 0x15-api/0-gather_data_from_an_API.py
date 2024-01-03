#!/usr/bin/python3
"""Accessing todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    empId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + empId

    response = requests.get(url)
    empName = response.json().get('name')

    toUrl = url + "/todos"
    response = requests.get(toUrl)
    tasks = response.json()
    count = 0
    done_count = []

    for task in tasks:
        if task.get('completed'):
            done_count.append(task)
            count += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empName, count, len(tasks)))

    for task in done_count:
        print("\t {}".format(task.get('title')))
