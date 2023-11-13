
# https://en.wikipedia.org/wiki/Programmer 


# Example program below to get some understanding: 
# import requests
# from bs4 import BeautifulSoup

# def get_page(url):
#     response = requests.get(url)

#     soup = BeautifulSoup(response.content, 'html.parser')

#     tag = soup.find_all("a")

#     for t in tag:
#         url2 = t.get("href")
#         print(url2)

# get_page(input("What URL would you like to scrape? "))




# Main program:
# This program is going to grab different URL's for us.

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

# We are going to use the "set" class right here. This will identify all of the individual URL's for us. 
# If we visit multiple URL's, this class will help us to differentiate between these.
# Basically, we want it to classify each URL "one time".
visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except: 
        print(f"Request failed {url}.")
        return 
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_all('a') # 'a' for anchor-tag
        urls = []
        for tag in a_tag:
            href = tag.get("href")    # href for hyperlink
            if href is not None and href != "":
                urls.append(href)

        # moving on let's delete the duplicates, and add the key words in the for loop

        for urls2 in urls: 
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)
                if keyword in url_join: 
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass


url = input("Enter the URL you want to scrape: ")
keyword = input("Enter the keyword to search for in the URL provided: ")
spider_urls(url, keyword)

# https://www.yahoo.com