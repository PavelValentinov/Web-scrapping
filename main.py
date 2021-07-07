import requests
from bs4 import BeautifulSoup

# получаем свой ip
# response = requests.get('https://2ip.ru')
# if not response.ok:
#     raise RuntimeError('сайт не доступен')
#
# text = response.text
#
# soup = BeautifulSoup(text, features='html.parser')
# print(soup.find('div', id='d_clip_button').text.strip())
DESIRED_HUBS = {'Как'}
KEYWORDS = ['проекта', 'Как']

response = requests.get('https://habr.com/ru/all')
if not response.ok:
    raise RuntimeError('сайт не доступен')

text = response.text

soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
# print(articles)
for article in articles:
    # hubs = {h.text.strip() for h in article.find_all('a', class_='hub-link')}
    # if hubs & DESIRED_HUBS:
    #     a = article.find('a', class_='post__title_link')
    #     print(a.attrs.get('href'))
    hubs = []
    for h in article.find_all():
        hubs.append(h.text.strip())
    # print(hubs)

    for word in KEYWORDS:
        # full_hubs = ' '.join(hubs)
        for h in hubs:
            if word in h.split():
                time = article.find(class_='post__time')
                title = article.find(class_='post__title')
                href = article.find('a', class_='post__title_link')
                # print('слово', h.split(), 'есть')
                print(time.text, title.text, href.attrs.get('href'), '\n')


# print(len(articles))