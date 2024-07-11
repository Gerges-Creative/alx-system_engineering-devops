#!/usr/bin/python3
"""
0-subs.py queries to https://www.reddit.com/dev/api/
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    domain = 'https://www.reddit.com'
    path = f'/r/{subreddit}/about.json'
    url = f'{domain}{path}'
    headers = {
        'User-Agent': 'my-app/0.0.1',
        'over18': 'yes'
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
        response.raise_for_status() #Raises HTTPError for bad responses (4xx and 5xx)

        data = response.json().get('data')
        if data:
            subscribers = data.get('subscribers')
            return subscribers
        else:
            return 'No Data Found'

    except requests.exceptions.RequestException as e:
        return f'Error: {e}'
