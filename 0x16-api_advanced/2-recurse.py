#!/usr/bin/python3
"""
Function that queries the Reddit API and returns a list
containing titles of all hot articles for a subreddit.
"""


import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    hot articles for a given subreddit.
    Args:
        subreddit (str): The name of subreddit.
        hot_list (list): List to store titles of hot articles.
        Default is an empty list.
    Returns:
        list or None: List containing titles of hot articles or
        None if subreddit is invalid.
    """
    if hot_list is None:
        # intialize hot_list if not provided
        hot_list = []
    # Intialize after variable used as pagination of all hot articles
    after = None
    # Base case: STop recursion when 'after' is 'STOP'
    if after == 'STOP':
        return hot_list

    # URL to get the top 10 posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # Define the custom User-Agent header
    header = {'User-Agent': 'MyBot/0.0.1'}
    # set the limit for number of posts per request
    params = {'limit': 100}
    # Send GET HTTP requests
    res = requests.get(url,
                       headers=header,
                       params=params,
                       allow_redirects=False)
    # Check if the request was successful
    if res.status_code == 200:
        # Extract post data from res
        data = res.json().get('data', {}).get('children', [])
        if data:
            # Iterate through each post
            for post in data:
                # Add title to the hot_list
                hot_list.append(post['data']['title'])
            # Check if there are more pages
            if 'after' in res.json().get('data', {}):
                after = res.json()['data']['after']
                # Recursively call with updated 'after' parameter
                return recurse(subreddit, hot_list, after)
            else:
                # Returns hot_list when all pages are processed
                return hot_list
        else:
            return None # if no posts are found
    else:
        # Return None if subreddit is invalid or failed request
        return None
