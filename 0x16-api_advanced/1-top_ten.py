#!/usr/bin/python3

"""
This Function Queries for the Titles of First 10 hot posts
Subreddit given as a command line arguement
"""
import requests


def top_ten(subreddit):
    """Returns Title of First 10 Hot Posts"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'This Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            post_title = post['data']['title']
            print(post_title)
    else:
        print("None")
