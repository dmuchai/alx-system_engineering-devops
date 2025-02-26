#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit. If the subreddit is invalid, prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'ALX-Advanced-API-Client/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        print(post.get('data', {}).get('title', None))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
