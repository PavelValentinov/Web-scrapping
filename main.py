import requests
from bs4 import BeautifulSoup

KEYWORDS = ['проекта', 'Как']

response = requests.get('https://habr.com/ru/all')
if not response.ok:
    raise RuntimeError('сайт не доступен')

text = response.text

soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = []
    for h in article.find_all():
        hubs.append(h.text.strip())

    for word in KEYWORDS:
        for h in hubs:
            if word in h.split():
                time = article.find(class_='post__time')
                title = article.find(class_='post__title')
                href = article.find('a', class_='post__title_link')
                # print('слово', h.split(), 'есть')
                print(time.text, title.text, href.attrs.get('href'), '\n')