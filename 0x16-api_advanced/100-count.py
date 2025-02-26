#!/usr/bin/python3
"""
Module to recursively query the Reddit API, parse hot article titles,
and count occurrences of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses hot article titles,
    and counts occurrences of given keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of keywords to count.
        after (str): The parameter for pagination (default: None).
        word_count (dict): Dictionary to store word frequencies.

    Returns:
        None: Prints the sorted word count or nothing if invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALX-Advanced-API-Client/1.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
                )
        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        titles = [post['data']['title'].lower().split() for post in posts]

        # Flatten the list of words from titles
        words = [word.strip('.,!?-_') for title in titles for word in title]

        # Initialize or update word_count dictionary
        if not word_count:
            word_count = {word.lower(): 0 for word in word_list}

        for word in words:
            if word in word_count:
                word_count[word] += 1

        after = data.get('data', {}).get('after')
        if after:
            return count_words(subreddit, word_list, after, word_count)

        # Sorting: by count (descending), then by word (ascending)
        sorted_words = sorted(
            [(word, count) for word, count in word_count.items() if count > 0],
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_words:
            print(f"{word}: {count}")

    except requests.exceptions.RequestException:
        return
