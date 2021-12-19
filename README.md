# Мини-документация по использованию парсера в коде

## Объекты
### User
Параметры:
  1) url (str) = ссылка на пользователя
  2) username (str) = имя пользователя
  3) logo_url (str) = ссылка на аватарку
  4) description (str) = описание аккаунта
  5) comment_karma (int) = карма коментов
  6) link_karma (int) = карма ссылок
  7) total_karma (int) = общая карма
  8) created_date (str) = время создания акка
  9) is_email_verif (bool) = потвержден ли емейл (True/False)
  10) list posts (list) = список объектов Post

### Subreddit (Group)
  1) url (str) = ссылка на сабреддит
  2) name (str) = название сабреддита
  3) logo_url (str) = ссылка на аватарку
  4) description (str) = описание сабреддита
  5) created_date (str) = дата создани сабреддита
  6) subs_count (int) = число участников
  7) active_subs (int) = число участников онлайн
  8) rules (str) = Правила сабреддита

### Post
  1) url (str) = ссылка на пост
  2) title (str) = название поста
  3) author (User) = объект User, только без постов
  4) created_date (str) = дата поста
  5) flair (list) = список тегов
  6) text (str) = текст поста
  7) picture (str) = ссылка на картинку поста
  8) upvotes (int) = кол-во апвотов
  9) upvote_ratio (float) = соотношение апвотов (Значение от 0 до 1)
  10) comments_count (int) = число коментов

## Использование в коде
### Функция retrieve_url(url)
Параметры:
  1) url = ссылка на пользователя, пост, или сабреддит
 
### Возвращаемое значение:
Функция возвращает питоновский dict вида
```
{
    "request_type": "post/subreddit/user/invalid_url",
    "content": {
        <Тут информация>
    },
}

```

## Примеры в коде
```
from reddit.reddit_parser import Reddit_parser

reddit = Reddit_parser()

info = reddit.retrieve_url('https://www.reddit.com/r/pics/comments/rgyuh5/after_30_years_of_mortgage_payments_i_paid_it_off/')
print(info)
{
  'request_type': 'post',
  'content': {
    'url': 'https://www.reddit.com/r/pics/comments/rgyuh5/after_30_years_of_mortgage_payments_i_paid_it_off/',
    'title': 'After 30 years of mortgage payments. I paid it off today. It’s all ours',
    'author': {
      'url': 'https://www.reddit.com/user/Latter-Statement-463',
      'username': 'Latter-Statement-463',
      'logo_url': 'https://styles.redditmedia.com/t5_485iy8/styles/profileIcon_snoo6477886c-4c03-4be8-b2ad-9c8e367ea0ac-headshot-f.png',
      'description': '',
      'comment_karma': 27842,
      'link_karma': 8484,
      'total_karma': 44780,
      'created_date': 1617893702.0,
      'is_email_verif': True
    },
    'created_date': 1639574086000,
    'flair': [
      
    ],
    'text': '',
    'picture': 'https://i.redd.it/lzjti8o0ip581.jpg',
    'upvotes': 145464,
    'upvote_ratio': 0.78,
    'comments_count': 5720
  }
}


```
