from typing import Mapping
import requests
import time
import re
from bs4 import BeautifulSoup

#This code extract the particular day's article links

url = 'https://www.bbc.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

f = requests.get(url, headers=headers)
soup = BeautifulSoup(f.content, 'lxml')

article_url = soup.find_all('a',{'class':'media__link'})

n = 0
art_url = []
art_title = []
for anchor in article_url:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    if re.search(r"https://www.bbc.com", str(anchor)):
        art_url.append(anchor['href'])
        art_title.append(anchor.string)
    else:
        urls = 'https://www.bbc.com' + anchor['href']
        art_url.append(urls)
        art_title.append(anchor.string)
    n += 1

t_date = time.strftime("%Y%m%d")
filename = str(t_date)+"_url"
file = open(filename+'.txt', 'w')
for i in art_url:
    file.write(i)
    file.write('\n')

file.close()

file_title = open(filename+'_title'+'.txt', 'w')
for i in art_title:
    file_title.write(i)
    file_title.write('\n')

file_title.close()