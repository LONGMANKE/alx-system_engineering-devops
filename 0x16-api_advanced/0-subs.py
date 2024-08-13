#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    # Set the URL and headers for the request
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'myAPI/0.0.1'}
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the request is successful (status code 200), parse the JSON
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        
        # If the status code is 301 (redirect) or any other, return 0
        return 0
    
    except Exception as e:
        # If there's any error, return 0
        return 0
