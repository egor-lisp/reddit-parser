

class Reddit_api():

    def __init__(self):
        pass

    def get_url_type(self, url):
        try:
            url_type = url.split('reddit.com/')[1].split('/')[0]
            if 'comments' in url:
                return 'post'
        except:
            return 'invalid_url'

        if url_type == 'r':
            return 'subreddit'
        elif url_type == 'user':
            return 'user'

    def get_user_info_url(self, username):
        url = f'https://www.reddit.com/user/{username}/about.json'
        # Параметры можно будет менять
        params = '?redditWebClient=desktop2x&app=desktop2x-client-production&gilding_detail=1&awarded_detail=1&raw_json=1'

        return url+params
