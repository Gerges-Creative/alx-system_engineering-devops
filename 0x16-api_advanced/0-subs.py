#!/usr/bin/python3
"""
0-subs.py queries to https://www.reddit.com/dev/api/
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    domain = f'https://www.reddit.com'
    path = f'/r/{subreddit}/about.json'
    url = f'{domain}{path}'
    headers = {
        'User-Agent': 'MyRedditApp/0.1 by DealerOdd6515'
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
        # Raises HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()

        data = response.json().get('data')
        if data:
            subscribers = data.get('subscribers')
            return subscribers
        else:
            return 0

    except requests.exceptions.RequestException as e:
        return 0
