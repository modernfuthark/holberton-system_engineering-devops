#!/usr/bin/python3
""" Gathers data from JSONPlaceholder and exports it """

from requests import get
from sys import argv
from json import dumps

url_todos = "https://jsonplaceholder.typicode.com/todos?userId="
url_user = "https://jsonplaceholder.typicode.com/users/"


def GetData():
    """ Gets the data from a url """
    user = get(url_user + argv[1]).json()
    todos = get(url_todos + argv[1]).json()

    tasks = []
    for i in todos:
        tasks.append({"task": i["title"], "completed": i["completed"],
                     "username": user["name"]})

    with open(str(user["id"]) + ".json", "w+") as f:
        f.write(dumps({"{}".format(user["id"]): tasks}))


if __name__ == "__main__":
    GetData()
