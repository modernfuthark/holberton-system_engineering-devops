#!/usr/bin/python3
""" Gathers data from JSONPlaceholder and displays it """

from requests import get
from sys import argv

url_todos = "https://jsonplaceholder.typicode.com/todos/"
url_user = "https://jsonplaceholder.typicode.com/users/"


def GetData():
    """ Gets the data from a url """
    # if len(argv) < 2:
    #    print("No ID given")
    #    return

    user = get(url_user + argv[1]).json()
    todos = get(url_todos).json()

    todos_total = 0
    todos_done = 0
    results = []

    for i in todos:
        if i["userId"] == user.get("id"):
            todos_total += 1
            if i["completed"]:
                todos_done += 1
                results.append(i["title"])
    print("Employee {} is done with tasks({}/{})"
          .format(user.get("name"), todos_done, todos_total))
    for line in results:
        print("\t {}".format(line))


if __name__ == "__main__":
    GetData()
