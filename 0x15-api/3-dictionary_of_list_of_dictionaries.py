#!/usr/bin/python3
""" Gathers data from JSONPlaceholder and exports it """

from requests import get
from json import dumps

url_todos = "https://jsonplaceholder.typicode.com/todos?userId="
url_user = "https://jsonplaceholder.typicode.com/users/"


def GetData():
    """ Gets the data from a url """
    listdict = {}

    for uid in range(1, 11):
        user = get(url_user + str(uid)).json()
        todos = get(url_todos + str(uid)).json()

        tasks = []
        for i in todos:
            tasks.append({
                          "task": i["title"],
                          "completed": i["completed"],
                          "username": user["username"]
            })
        listdict["{}".format(user["id"])] = tasks

    with open("todo_all_employees.json", "w+") as f:
        f.write(dumps(listdict))


if __name__ == "__main__":
    GetData()
