# This program is going to grab different URL's for us. 
# https://en.wikipedia.org/wiki/Programmer 

import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    tag = soup.find_all("a")

    for t in tag:
        url2 = t.get("href")
        print(url2)

get_page(input("What URL would you like to scrape? "))
