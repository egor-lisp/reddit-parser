# Мини документация и примеры по парсеру реддит

## Объекты
### User
  str url = ссылка на пользователя
  str username = имя пользователя
  str logo_url = ссылка на аватарку
  str description = описание аккаунта
  int comment_karma = карма коментов
  int link_karma = карма ссылок
  int total_karma = общая карма
  str created_date = время создания акка
  bool is_email_verif = потвержден ли емейл
  list posts = список объектов Post

### Subreddit (Group)
  str url = '<ссылка на сабреддит>'
  str name = '<название сабреддита>'
  str logo_url = 'ссылка на аватарку'
  str description = '<описание сабреддита>'
  str created_date = '<дата создани сабреддита>'
  int subs_count = <число участников>
  int active_subs = <число участников онлайн>
  str rules = '<Правила сабреддита>'
  
### Post
  str url = 'Ссылка на пост'
  str title = 'Название поста'
  User author = <Объект User, только без постов>
  str created_date = 'Дата поста'
  list flair = <Список тегов>
  str text = 'Текст поста'
  str picture = 'Ссылка на картинку поста'
  int upvotes = <Кол-во апвотов>
  float upvote_ratio = <соотношение апвотов>
  int comments_count = <число коментов>
