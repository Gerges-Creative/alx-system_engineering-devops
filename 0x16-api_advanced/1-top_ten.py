#!/usr/bin/python3
"""
queries to https://www.reddit.com/dev/api/
"""
import requests


def top_ten(subreddit):
    """
    returns the top ten hot posts for subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {
        'user-agent': 'Gerges_Z',
        'over18': 'yes'
    }
    response = requests.get(
        url,
        headers=header,
        allow_redirects=False
    )
    code = response.status_code
    if code >= 300:
        print('None')
    else:
        data = response.json().get('data')
        children = data.get('children')
        for child in range(10):
            hot_post = children[child].get('data')
            title = hot_post.get('title')
            print('{}'.format(title))
