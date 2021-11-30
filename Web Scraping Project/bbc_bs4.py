from os import closerange
import requests
import time
from bs4 import BeautifulSoup
import re

exec(open('bbc_url.py').read())

t_date = time.strftime("%Y%m%d")
filename = str(t_date)+"_url"
filename_title = filename+"_title"
work_book = str(t_date)+"_bbc_article_bs4"

file = open(filename+'.txt','r')
file_t = open(filename_title+'.txt','r')
file_final = open(work_book+'.txt', 'w')

#url_list holds all the scraped urls from the home page
url_list = []
#title_list holds all the scraped title strings from the home page
title_list = []
#art_tag_list holds all the scraped article from the respective url page
art_tag_list = []

#for loop for url list creation from the file
for line in file:
    stripped_line = line.strip()
    url_list.append(stripped_line)

#for loop for url_title list creation from the file
c = 0
for line in file_t:
    stripped_line = line.strip()
    if c%2 != 0:
        title_list.append(stripped_line)
    else:
        pass
    c+=1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

num = 0
for row in range(len(url_list)):
    num+=1
    file_final.write(str(num)+".\n")
    file_final.write(title_list[row]+"\n")
    file_final.write(url_list[row]+"\n")
    f = requests.get(url_list[row],headers=headers)
    soup = BeautifulSoup(f.content, 'lxml')
    for tag in soup.find_all(re.compile("^art")):
        #print(tag)
        art_tag_list.append(tag)
    for i in range(len(art_tag_list)):
        file_final.write(str(art_tag_list[i])+"\n")
    file_final.write("\n\t                                       ******************************************************************************************\n\t                                       ******************************************************************************************\n\n")

# print(len(art_tag_list))

file_final.write("End of Scraping")
file_final.close()

