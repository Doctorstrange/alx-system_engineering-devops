#!/usr/bin/python3
"""returns the number of subscribers """

from requests import get


def number_of_subscribers(subreddit):
    """returns the number of subscribers (not active users, total subscribers)
    for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 120.0.6099.216'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    thejson = response.json()

    try:
        return thejson.get('data').get('subscribers')

    except Exception:
        return 0