#!/usr/bin/python3
""" queries the Reddit API """
import requests


def recurse(subreddit, after=None, hot_list=None):
    """queries the Reddit API recursively."""
    if hot_list is None:
        hot_list = []

    user_agent = {'User-Agent': 'chrome-browser'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    token_param = {'after': after}

    results = requests.get(url, params=token_param,
                           headers=user_agent, allow_redirects=False)

    if results.status_code == 200:
        after_token = results.json().get("data").get("after")
        if after_token is not None:
            recurse(subreddit, after_token, hot_list)

        titles = results.json().get("data").get("children")
        for title_ in titles:
            hot_list.append(title_.get("data").get("title"))

        return hot_list
    else:
        return None
