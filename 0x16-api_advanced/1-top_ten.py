#!/usr/bin/python3

''' script to retrieve the top ten  posts listed for a given subreddit.'''

import requests


def top_ten(subreddit):
    '''returns the titles of the first 10 hot posts listed for  subreddit.'''

    get_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {"User-Agent": 'My Agent'}
    response = requests.get(get_url, headers=header, allow_redirects=False)
    data = response.json()

    if response.status_code == 200:
        hot_posts = data.get("data").get("children")
        if hot_posts:
            titles = []
            for post in hot_posts:
                result = post.get("data").get("title")
                titles.append(result)
            print('\n'.join(titles))
    else:
        print(None)
