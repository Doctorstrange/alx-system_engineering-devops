#!/usr/bin/python3
""" parses the title of all hot articles"""

import json
import requests


def count_words(subreddit, parse_values, after=None, tally=None):
    """parses the title of all hot articles"""

    if tally is None:
        tally = [0] * len(parse_values)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(parse_values)):
                    if parse_values[i].lower() == word.lower():
                        tally[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(parse_values)):
                for j in range(i + 1, len(parse_values)):
                    if parse_values[i].lower() == parse_values[j].lower():
                        save.append(j)
                        tally[i] += tally[j]

            for i in range(len(parse_values)):
                for j in range(i, len(parse_values)):
                    if (tally[j] > tally[i] or
                            (parse_values[i] > parse_values[j] and
                             tally[j] == tally[i])):
                        aux = tally[i]
                        tally[i] = tally[j]
                        tally[j] = aux
                        aux = parse_values[i]
                        parse_values[i] = parse_values[j]
                        parse_values[j] = aux

            for i in range(len(parse_values)):
                if (tally[i] > 0) and i not in save:
                    print("{}: {}".format(parse_values[i].lower(), tally[i]))
        else:
            count_words(subreddit, parse_values, after, tally)
