#!/usr/bin/python3
""" Gathers data from JSONPlaceholder and displays it """

from requests import get
from sys import argv

url_todos = "https://jsonplaceholder.typicode.com/todos?userId="
url_user = "https://jsonplaceholder.typicode.com/users/"


def GetData():
    """ Gets the data from a url """
    user = get(url_user + argv[1]).json()
    todos = get(url_todos + argv[1]).json()

    todos_total = len(todos)
    todos_done = 0
    results = []

    for i in todos:
        if i["completed"]:
            todos_done += 1
            results.append(i["title"])
    print("Employee {} is done with tasks({}/{})"
          .format(user.get("name"), todos_done, todos_total))
    for line in results:
        print("\t {}".format(line))


if __name__ == "__main__":
    GetData()
