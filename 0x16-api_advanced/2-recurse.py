#!/usr/bin/python3
""" 2-recurse: Gets the top 10 hot posts but recursive """

import requests


def recurse(subreddit, hot_list=[], aft=""):
    """ recurse: Recursive, using the 'after' json """

    if aft is None:
        return []
    elif len(aft) == 0:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}"\
              .format(subreddit, aft)

    req = requests.get(url, allow_redirects=False,
                       headers={"User-Agent": "PlaceholderAgent"})
    if req.status_code == 200:
        if req.json()["data"]["children"]:
            for v in req.json()["data"]["children"]:
                hot_list.append(v["data"]["title"])
    else:
        return None

    return(hot_list + recurse(subreddit, [], req.json()["data"]["after"]))
