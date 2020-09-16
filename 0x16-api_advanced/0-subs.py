#!/usr/bin/python3
""" 0-subs: returns the number of subscribers of a given subreddit """

import requests


def number_of_subscribers(subreddit):
    """ number_of_subscribers: Returns # of subs of a /r/ """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={"User-Agent": "PlaceholderAgent"})
    if req.status_code == 200:
        return (req.json()["data"]["subscribers"])
    return (0)
