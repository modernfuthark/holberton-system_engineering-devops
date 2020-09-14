#!/usr/bin/python3
""" Gathers data from JSONPlaceholder and exports it """

from requests import get
from sys import argv
from csv import writer, QUOTE_ALL

url_todos = "https://jsonplaceholder.typicode.com/todos?userId="
url_user = "https://jsonplaceholder.typicode.com/users/"


def GetData():
    """ Gets the data from a url """
    user = get(url_user + argv[1]).json()
    todos = get(url_todos + argv[1]).json()

    with open(str(user["id"]) + ".cvs", "w") as f:
        _writer = writer(f, delimiter=",", quotechar='"', quoting=QUOTE_ALL)
        for i in todos:
            _writer.writerow([user["id"], user["username"],
                             i["completed"], i["title"]])


if __name__ == "__main__":
    GetData()
