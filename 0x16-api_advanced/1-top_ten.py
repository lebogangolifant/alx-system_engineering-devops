#!/usr/bin/python3
"""
This script defines a Python function that retrieves
and prints the titles of the first 10 hot posts
for a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Function to retrieve and print the titles
    of the first 10 hot posts for a subreddit.
    """
    # Construct the API endpoint URL
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Define custom headers to comply with Reddit's API guidelines
    headers = {"User-Agent": "my_bot/1.0"}

    # Send an HTTP GET request to the API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print("No hot posts found in this subreddit.")
        else:
            for post in posts:
                print(post["data"]["title"])
    else:
        print("None")
