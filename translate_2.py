# -*- coding: utf8 -*-

import requests
import urllib

from bs4 import BeautifulSoup

word = "%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94"
url = 'https://translate.google.com/#ko/en/%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94'
print (url)
source_code = requests.get(url)
html = source_code.text
soup = BeautifulSoup(html, 'lxml')

data = []
# result = soup.find_all('span', id="result_box")
result = soup.find_all('span')

print (result)
# result = soup.find_all()