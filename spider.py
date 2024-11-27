import requests 
from bs4 import BeautifulSoup
import re
from selenium import webdriver

# base url's
root_url = "https://www.kupujemprodajem.com/muzicki-instrumenti/gitarska-oprema-efekti-i-pedale//grupa/22/726"
pojacala_delovi_url = "https://www.kupujemprodajem.com/muzicki-instrumenti/gitarska-pojacala-delovi/grupa/22/998"
gitare_elektricne_url = "https://www.kupujemprodajem.com/muzicki-instrumenti/gitare-elektricne/grupa/22/325"

# main dict
all_data = []

# scrape single page and load next
def scrape_and_get_next_page(root_url, m):
    page_url = f"{root_url}/{m}"
    driver = webdriver.Chrome()
    driver.get(page_url)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    text = re.compile('AdItem_name')
    cena = re.compile('AdItem_price')

    print(f"{m}")
    articles = soup.find_all('article') 
    for article in articles:
        article_titles = article.find("div", class_= text)
        article_price = article.find("div", class_=cena)
        if article_titles: 
            title = article_titles.get_text()
            price = article_price.get_text()
            all_data.append({"Title": title, "Cena": price})
        else: 
            print("element not found")

# scrape loop for n pages
m = 0
for i in range(10):
    m += 1
    scrape_and_get_next_page(root_url, m)

# print data
for item in all_data: 
    print(f"{item}")