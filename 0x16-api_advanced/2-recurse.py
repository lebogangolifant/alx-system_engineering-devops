#!/usr/bin/python3
"""
This script defines a recursive function,
to query the Reddit API and accumulate
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to retrieve and accumulate
    the titles of all hot articles for a subreddit.
    """
    # Construct the API endpoint URL
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)

    # Get the next page of results
    if after:
        url += "&after={}".format(after)

    # Define custom headers to comply with Reddit's API guidelines
    headers = {"User-Agent": "my_bot/1.0"}

    # Send an HTTP GET request to the API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]

        if not posts:
            # If no more posts, return the accumulated hot_list
            return hot_list
        else:
            for post in posts:
                # Append titles to the hot_list
                hot_list.append(post["data"]["title"])

            # Recursively call the function to get the next page of results
            return recurse(subreddit, hot_list, after)
    else:

        return None
