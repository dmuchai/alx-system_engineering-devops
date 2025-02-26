#!/usr/bin/python3
"""
Recursive function to query the Reddit API and return a list containing the
titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all
    hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list, optional): List to store titles of hot posts.
        after (str, optional): The pagination parameter to get next results.

    Returns:
        list: List of hot article titles, or None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALX-Advanced-API-Client/1.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])
    for post in posts:
        hot_list.append(post.get('data', {}).get('title', None))

    after = data.get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
