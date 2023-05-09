#!/usr/bin/python3

''' script to retrieve the number of subscribers'''

import requests


def number_of_subscribers(subreddit):
    '''function to return the number of subscribers on subreddit'''

    get_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {"User-Agent": 'My Agent'}
    response = requests.get(get_url, headers=header, allow_redirects=False)
    data = response.json()

    if response.status_code == 200:
        subscribers = data.get("data").get("subscribers")
        return subscribers
    else:
        return 0
