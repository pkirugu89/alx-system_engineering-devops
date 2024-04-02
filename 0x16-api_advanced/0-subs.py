#!/usr/bin/python3
"""
This script defines a function that gets the subscriber numbers for subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API to get number of subscriber for a given subreddit.
    Args:
        subreddit (str): The name of subreddit.
    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    # URL for the subreddit's details
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Define custom User-Agent header
    header = {'User-Agent': 'MyBot/0.0.1'}
    # Send GET request
    response = requests.get(url, headers=header)
    # Check if the request was successful
    if response.status_code == 200:
        # Extract data from JSON response
        data = response.json().get('data')
        if data:
            # Return the subscribers numbers if available
            return data.get('subscribers', 0)
        # Return 0 if the subreddit is invalid or failed request.
        return 0
