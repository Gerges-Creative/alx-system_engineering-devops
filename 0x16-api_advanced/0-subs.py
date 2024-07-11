#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    # Define the URL for the subreddit info
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Set a custom User-Agent to avoid being blocked by Reddit
    headers = {"User-Agent": "My-User-Agent"}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json().get("data")
        # Return the number of subscribers
        return data.get("subscribers", 0)
    else:
        # If the request was not successful, return 0
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit = "learnpython"
    print("Number of subscribers:", number_of_subscribers(subreddit))