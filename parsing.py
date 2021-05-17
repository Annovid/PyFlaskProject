"""
This file parsing site
"""

import requests as req
from bs4 import BeautifulSoup


BASE_URL = "https://www.kinopoisk.ru/s/type/film/list/1/find/"


def parsing(required):
    """
    this function call functions get_soup and get_films
    """
    soup = get_soup(BASE_URL + '/' + required + '/')
    films = get_films(soup)
    return films


def get_soup(url):
    """
    this function return soup
    """
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup


def get_films(soup):
    """
    this function make dictionary
    """
    items = soup.find_all("div", class_="element")
    films = []
    for item in items:
        def processing(name):
            return name.replace("\xa0", " ")
        films.append({
            'title': processing(item.find("p", class_="name").get_text()),
            'description': item.find("span", class_="gray").get_text(),
            'link': item.find("p", class_="name").find("a").get("data-url")
        })
    return films[:10]


if __name__ == "__main__":
    pass
