#!/usr/bin/python3
"""
This script defines a recursive function
to query the Reddit API, parse the titles
of hot articles, and print a sorted count
of specified keywords (case-insensitive)
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursive function to query the Reddit API,
    parse titles, and print a sorted count of specified keywords
    """
    # Construct the URL to retrieve hot posts for the given subreddit
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
            # If no more posts, sort and print the word counts
            sorted_word_count = sorted(
                word_count.items(),
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_word_count:
                print("{}: {}".format(word, count))
        else:
            for post in posts:
                title = post["data"]["title"]
                title_words = title.lower().split()
                for word in word_list:
                    if word.lower() in title_words:
                        if word.lower() in word_count:
                            word_count[word.lower()] += 1
                        else:
                            word_count[word.lower()] = 1

            # Recursively call the function to get the next page of results
            return count_words(subreddit, word_list, after, word_count)
    else:

        return
