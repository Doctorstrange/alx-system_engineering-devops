#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts """

from requests import get


def top_ten(subreddit):
    """ queries the Reddit API and prints the
    titles of the first 10 hot posts
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google-Chrome'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent, params={'limit': 10})
        response.raise_for_status()

        if response.status_code == 200:
            result = response.json().get('data', {}).get('children', [])

            return [obj.get('data', {}).get('title', '') for obj in result]
        else:
            print(f"Failed to retrieve data. HTTP status code:
                  {response.status_code}")

    except requests.RequestException as e:
        print(f"Error during request: {e}")

    return []
