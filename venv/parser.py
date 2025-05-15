# Импортируем необходимые библиотеки
import requests as rq
from bs4 import BeautifulSoup
from fake_headers import Headers
# from lxml import html



# Определяем ключевые слова для поиска
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
# Создание подменного юзер-агента
headers = Headers(browser='firefox', os='win').generate()
# Жертва парсинга
url = "https://habr.com/ru/articles/"
# Отпрвка гет запроса
response = rq.get(url, headers=headers)
# Парсинг текста
soup = BeautifulSoup(response.text, 'html.parser')

# Поиск всех элементов статей на странице
articles = soup.find_all(class_="tm-articles-list__item")

# Цикл для поиска в элементах
for article in articles:
    # Поиск названия
    name_tag = article.find('h2')     
    if name_tag:
        name = name_tag.text.strip('') 
    else: 
        name = 'Name not defined'
    # print(name)
    # Поиск ссылки
    link_tag = name_tag.find('a')
    link = "https://habr.com" + link_tag["href"]
#   print(link)
    # Поиск даты
    date_tag = article.find('time')
    date = date_tag['title']
#   print(date)
    # Работа с превью статьи для поиска ключевых слов
    preview_tag = article.find('div', class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    # print(preview_tag)
    if preview_tag:
        try:
                preview_text = preview_tag.text.strip('')
        except AttributeError:
            preview_text = 'Text not found'
    else:
        preview_text = "Can't get the data"
    # Поиск по ключевым словам в превью 
    for keyword in KEYWORDS:
        if keyword.lower() in preview_text.lower():
            print(f"{date} - {name} - {link}")
        else:
            pass
        

# Вывод нужных статей
print(f"{date} - {name} - {link}")
