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
    path = '/r/{}/about.json'.format(subreddit)
    url = '{}{}'.format(domain, path)
    header = {
        'user-agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)',
        'over18': 'yes'
    }
    response = requests.get(
        url,
        headers=header,
        allow_redirects=False
    )
    code = response.status_code
    if code >= 300:
        return 0
    data = response.json().get('data')
    subscribers = data.get('subscribers')
    return subscribers
