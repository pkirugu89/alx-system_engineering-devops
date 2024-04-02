#!/usr/bin/python3
"""
Function that prints the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
    Queries and print the first 10 hot posts listed for a given subreddit.
    Args:
        subreddit (str): The name of subreddit.
    Return:
        First 10 hot posts for a given subreddit.
    """
    # URL for getting the hot posts of the subreddit
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    # Define the User-Agent header
    header = {'User-Agent': 'MyBot/0.0.1'}
    # Send HTTP GET request
    res = requests.get(url, headers=header)
    # Check if the requests was successful
    if res.status_code == 200:
        # Extract data from JSON response
        data = res.json().get('data')
        if data:
            # Get the list of posts
            child = data.get('children')
            # Iterate through each post
            for post in child:
                # Print the post title
                print(post.get('data').get('title'))
        else:
            # Print None if subreddit is invalid or request failed.
            print("None")
