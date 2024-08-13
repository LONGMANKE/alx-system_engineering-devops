import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    # Define the API endpoint with the subreddit
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set headers, including a custom User-Agent to avoid being blocked
    headers = {"User-Agent": "Custom"}
    
    # Define the parameters to limit the number of posts to 10
    params = {"limit": 10}
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the posts from the response JSON
        posts = response.json().get("data", {}).get("children", [])
        
        # Print the title of each post
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        # If the request failed, print None
        print(None)
