#!/usr/bin/python3
"""
This script defines a function that queries the Reddit API,
to retrieve the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Function to retrieve the number of subscribers for a subreddit."""
    # Construct the API endpoint URL
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Define custom headers to comply with Reddit's API guidelines
    headers = {"User-Agent": "my_bot/1.0"}

    # Send an HTTP GET request to the API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = response.json()
        # Extract the number of subscribers from the response
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
