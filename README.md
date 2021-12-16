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

