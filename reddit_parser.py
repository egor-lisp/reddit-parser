import requests, pickle
from reddit_api import Reddit_api
from utils import Utils


class User():

    def __init__(self):
        self.url = ''
        self.username = ''
        self.logo_url = ''
        self.description = ''
        self.comment_karma = 0
        self.link_karma = 0
        self.total_karma = 0
        self.created_date = ''
        self.is_email_verif = False

class Subreddit():

    def __init__(self):
        self.url = ''
        self.name = ''
        self.logo_url = ''
        self.description = ''
        self.created_date = ''
        self.subs_count = 0
        self.active_subs = 0
        self.rules = ''

class Post():

    def __init__(self):
        self.url = ''
        self.title = ''
        self.author = {}
        self.created_date = ''
        self.flair = []
        self.text = ''
        self.picture = None
        self.upvotes = 0
        self.upvote_ratio = 0
        self.comments_count = 0


class Reddit_parser():

    def __init__(self):
        self.api = Reddit_api()
        session = requests.Session()
        session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
        with open('cookies/session', 'rb') as f:
            session.cookies.update(pickle.load(f))
            f.close()
        self.session = session
        self.utils = Utils()

    def dict_from_class(self, class_):
        data = class_.__dict__
        return data

    def get_user_info(self, username):
        # Получаем json от реддита
        info_url = self.api.get_user_info_url(username)
        response = self.session.get(info_url)
        json = response.json()

        user = User()

        info = json['data']
        subreddit = json['data']['subreddit']

        user.username = username
        user.url = 'https://www.reddit.com/user/'+username

        user.description = subreddit['description']

        user.logo_url = info['icon_img']
        user.comment_karma = info['comment_karma']
        user.link_karma = info['link_karma']
        user.total_karma = info['total_karma']
        user.created_date = info['created_utc']
        user.is_email_verif = info['has_verified_email']

        return self.dict_from_class(user)

    def get_user_posts(username, max_couunt=10):
        pass

    def get_subreddit_info(self, url):
        response = self.session.get(url)
        raw_data = self.utils.extract_data(response.text)

        # Информация о сабреддите
        subreddits = raw_data['subreddits']

        # Получаем ключ
        about = subreddits['about']
        first_key = next(iter(about))

        # Вкладкии с информацией
        about = about[first_key]
        model = subreddits['models'][first_key]
        rules = subreddits['rules'][first_key]

        subreddit = Subreddit()

        subreddit.url = url
        subreddit.name = url.split('r/')[1]

        # Парсинг вкладки about
        subreddit.description = about['publicDescription']
        subreddit.created_date = about['created']
        subreddit.subs_count = about['subscribers']
        subreddit.active_subs = about['accountsActive']

        # Парсинг вкладки model
        subreddit.logo_url = model['communityIcon']

        # Парсинг вкладки rules
        rules_list = rules['rules']
        rules_string = ''
        for rule in rules_list:
            rules_string += rule['shortName'] + ' '
        subreddit.rules = rules_string

        return self.dict_from_class(subreddit)

    def get_post_info(self, url):
        # Получаем выдачу реддита
        response = self.session.get(url)
        raw_data = self.utils.extract_data(response.text)

        # Берем нужный раздел из выдачи
        posts = raw_data['posts']['models']
        first_key = next(iter(posts))
        data = posts[first_key]

        post = Post()

        post.url = data['permalink']
        post.title = data['title']
        try:
            post.text = self.utils.extract_post_text(data['media']['richtextContent'])
        # Значит в посте нет текста
        except KeyError:
            post.text = ''
        # Собираем инфу об авторе
        username = data['author']
        post.author = self.get_user_info(username)

        # Остальна инфа
        post.picture = data['media']['content']
        post.created_date = data['created']
        post.flair = self.utils.extract_flair(data['flair'])
        post.comments_count = data['numComments']
        post.upvotes = data['score']
        post.upvote_ratio = data['upvoteRatio']

        return self.dict_from_class(post)

    def retrieve_url(self, url):
        url_type = self.api.get_url_type(url)
        data = {'request_type': url_type}

        if url_type == 'invalid_url':
            data['content'] = {}

        elif url_type == 'user':
            username = url.split('reddit.com/user/')[1].replace('/', '')
            data['content'] = self.get_user_info(username)

        elif url_type == 'subreddit':
            data['content'] = self.get_subreddit_info(url)

        elif url_type == 'post':
            data['content'] = self.get_post_info(url)

        return data
