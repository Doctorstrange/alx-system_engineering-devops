#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts """

from requests import get


def top_ten(subreddit):
    """ queries the Reddit API and prints the
    titles of the first 10 hot posts
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {'User-Agent': 'CustomUserAgent'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=headers, allow_redirects=False, params={'limit': 10})
    injson = response.json()

    try:
        result = injson.get('data').get('children')

        for obj in result:
            print(obj.get('data').get('title'))

    except Exception:
        print("None")
