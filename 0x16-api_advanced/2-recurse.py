#!/usr/bin/python3

"""
This Script Returns A List containing Titles
of All Hot Articles of A Given Subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns A List of All Hot Titles"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
        subreddit, after)
    headers = {'User-Agent': 'This Agent'}
    posts = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        posts = posts.json()['data']
        after = posts['after']
        posts = posts['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)
