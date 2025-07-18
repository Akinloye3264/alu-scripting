#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid or does not exist, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:subreddit.hot:v1.0 (by /u/alustudent)'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        results = response.json().get("data", {}).get("children", [])
        if not results:
            print(None)
            return

        for post in results:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)


