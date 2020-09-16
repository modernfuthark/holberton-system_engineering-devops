#!/usr/bin/python3
""" 1-top_ten: Prints the top 10 hot posts of a /r/ """

import requests


def top_ten(subreddit):
    """ top_ten: Returns top 10 hot posts """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, headers={"User-Agent": "PlaceholderAgent"})
    if req.status_code == 200:  # Subreddit exists
        for i in range(0, 10):
            print(req.json()["data"]["children"][i]["data"]["title"])
