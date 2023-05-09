#!/usr/bin/python3

"""
This Script Returns Number of subscribers of a
Given Subreddit passed as command Line Arg
"""
import requests


def number_of_subscribers(subreddit):
    """Method that returns No. of Subscribers"""
    headers = {'User-agent': 'This Agent'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
