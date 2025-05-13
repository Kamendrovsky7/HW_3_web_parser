# Импортируем необходимые библиотеки
import requests as rq
from bs4 import BeautifulSoup
from fake_headers import Headers
# from lxml import html



# Определяем ключевые слова для поиска
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
# Создание подменного юзер-агента
headers = Headers(browser='chrome', os='win').generate()
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
    preview_tag = article.find('div', class_=f"article-formatted-body article-formatted-body article-formatted-body_version-2").text
    # print(preview_tag)
    # Поиск по ключевым словам в превью 
    if any(keyword.lower() in preview_tag.lower() for keyword in KEYWORDS):
        print(f"{date} - {name} - {link}")
        

# Вывод нужных статей
print(f"{date} – {name} – {link}")
