#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    # API endpoint to get the hot posts of a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Custom User-Agent to prevent being blocked by Reddit's API
    headers = {"User-Agent": "python:top_ten:v1.0.0 (by /u/yourusername)"}
    
    # Parameters to limit the number of posts returned to 10
    params = {"limit": 10}
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the list of posts
        posts = response.json().get("data", {}).get("children", [])
        
        # Print the title of each post
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        # If the subreddit is not valid, print None
        print(None)

# Example usage: replace 'programming' with your desired subreddit
top_ten('programming')
top_ten('this_is_a_fake_subreddit')

