#!/usr/bin/python3

'''Return a list of the titles of all hot articles for a subreddit '''

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of the titles of all hot articles for a subreddit
    """
    get_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Agent'}
    params_limit = {'limit': 100}
    if after:
        params_limit['after'] = after
    response = requests.get(get_url, headers=header, params=params_limit,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        posts = data.get('children')
        for post in posts:
            hot_list.append(post['data']['title'])
        if not data['after']:
            return hot_list
        else:
            return recurse(subreddit, hot_list, data['after'])
    else:
        print(None)
