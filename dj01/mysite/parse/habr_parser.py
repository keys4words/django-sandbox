import requests, time
from bs4 import BeautifulSoup


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
           'accept': '*/*'}
BASIC_URL = 'https://habr.com/ru/search/?q=django#h'



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    articles_lst = list()
    time.sleep(2)
    articles_html = soup.find_all('li', class_='content-list__item content-list__item_post shortcuts_item')
    for article in articles_html:
        article_dct = dict()
        title = article.find('h2', class_='post__title').a
        article_dct['title'] = title.text
        article_dct['url'] = ''
        url = article.find('a', class_='btn btn_x-large btn_outline_blue post__habracut-btn')
        if url:
            article_dct['url'] = url.get('href').replace('#habracut', '')
        articles_lst.append(article_dct)
    return articles_lst


def parse(URL):
    html = requests.get(URL, headers=HEADERS)
    if html.status_code == 200:
        print(get_content(html.text))
    else:
        print('Error')


def save_to_db(res):
    pass
parse(BASIC_URL)



