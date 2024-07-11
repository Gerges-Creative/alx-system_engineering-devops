#!/usr/bin/python3
"""Module to query Reddit API for the number of subscribers in a subreddit."""

import requests


def number_of_subscribers(subreddit):

    """Queries the Reddit API and returns the number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("Error: Received status code {}".format(response.status_code))
        return 0

    try:
        data = response.json().get("data")
        if data:
            return data.get("subscribers", 0)
        else:
            print("Error: 'data' field is missing in the response.")
            return 0
    except ValueError:
        print("Error: Unable to parse JSON response.")
        return 0
