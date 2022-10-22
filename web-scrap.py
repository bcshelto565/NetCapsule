from bs4 import BeautifulSoup
import requests
import re
from lxml import etree
# from selenium import webdriver

url = "https://web.archive.org/web/20220922100932/https://en.wikipedia.org/wiki/University_of_North_Texas"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
# stringed_page = etree.HTML(str(soup))

stringed_page = str(soup)
print(stringed_page)