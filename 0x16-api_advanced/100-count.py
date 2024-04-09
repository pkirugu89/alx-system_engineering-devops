#!/usr/bin/python3
"""
The module defines a recursive function that counts the occurences
of word in hot articles.
"""


import requests


def count_words(subreddit, word_list):
    """
    Queries the Reddit API and counts the keywords occurences in
    the hot articles.
    Args:
        subreddit (str): the name of subreddit.
        word_list (str): list of keyword occurences.
    Returns:
        None
    """
    # Initialize word_count list to store word counts
    word_counts = {}
    # Call the helper function
    recurse(subreddit, word_list, word_counts)
    # Helper function that prints word counts.
    print_word_counts(word_counts)


def recurse(subreddit, word_list, word_counts=None, after=None):
    """
    Recursive function to query the Reddit API and count keyword occurences.
    Args:
        subreddit (str): name of the subreddit.
        word_list (list): List of keywords to count occurrences.
        word_counts (dict): Dict to store word counts. Default is None.
        after (str): Parameter used for pagination. Default is None.
    Return:
        None
    """
    if word_counts is None:
        # Initialize word_counts if not provided
        word_counts = {}

    if after is None:
        # Construct the URL for the first page
        rlink = "https://www.reddit.com"
        url = "{}/r/{}/hot.json".format(rlink, subreddit)
    else:
        # Construct the URL for subsequent pages
        url = "{}/r/{}/hot.json?after={}".format(rlink, subreddit, after)
    # Define custom User-Agent header
    headers = {'User-Agent': 'MyBot/0.0.1'}
    # Limit for number of posts per request
    params = {'limit', 100}
    # GET http request
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    # Check if the res was successfull.
    if res.status_code == 200:
        # Extract post data
        data = res.json().get('data', {}).get('children', [])
        if data:
            # Iterate through each post
            for pst in data:
                # Convert title to lowercase for case-sensitive matching
                title = post['data']['title'].lower()
                # Loop through each word in word_list
                for word in word_list:
                    # Check if word is present in title (with space padding)
                    if '{}' in '{}'.format(word.lower(), title):
                        word_counts[word.lower()] = \
                                word_counts.get(word.lower(), 0) + 1
                # Check if there're more pages
                if 'after' in res.json().get('data', {}):
                    # Get the 'after' token for pagination
                    after = res.json()['data']['after']
                    # call method with updated 'after' parameter & word_counts
                    recurse(subreddit, word_list, word_counts, after)
    else:
        # Return None if subreddit is invalid
        return
    # Stop recursion when there're no more pages to fetch
    if after is None:
        return


def print_word_counts(word_counts):
    """
    Function to print the sorted given keyword counts
    Args:
        word_counts (dict): Dict counting word counts.
    Returns:
        int: word count.
    """
    # Sort word_counts by count (descending) and
    # word (ascending) alphabetically
    wcs = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    # print the word counts
    for word, count in wcs:
        print('{}:{}'.format(word, count))
