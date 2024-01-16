#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts """

from requests import get


def top_ten(subreddit):
    """ queries the Reddit API and prints the
    titles of the first 10 hot posts
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 120.0.6099.216'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params={'limit': 10})
    injson = response.json()

    try:
        result = injson.get('data').get('children')

        for obj in result:
            print(obj.get('data').get('title'))

    except Exception:
        print("None")
