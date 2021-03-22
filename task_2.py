import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


def get_animals():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    page = requests.get(url).text
    animals = {}
    while True:
        soup = BeautifulSoup(page, 'html.parser')
        names = soup.find('div', class_='mw-category-group').find_all('a')
        for name in names:
            if re.match('[а-яА-Я]', name.text[0]):
                if name.text[0] not in animals:
                    animals[name.text[0]] = []
                animals[name.text[0]].append(name.text)
        links = soup.find('div', id='mw-pages').find_all('a')
        page = None
        for a in links:
            if a.text == 'Следующая страница':
                url = urljoin('https://ru.wikipedia.org/', a.get('href'))
                page = requests.get(url).text
        if page == None:
            break
    list_keys = list(animals.keys())
    list_keys.sort()
    for i in list_keys:
        print(i, ': ', len(animals[i]))

