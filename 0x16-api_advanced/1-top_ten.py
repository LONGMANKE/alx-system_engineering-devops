#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10}

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Handle invalid subreddit (404 Not Found)
    if response.status_code == 404:
        print("None")
        return

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json().get("data", {}).get("children", [])
        # Loop through each post and print its title
        for post in results:
            print(post.get("data", {}).get("title"))
    else:
        print("None")
