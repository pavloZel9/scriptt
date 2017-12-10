#Павел Зелинский pavlozel9@gmail.com
#Python 3.6
#BeautifulSoup 4.4

import validators
import urllib
import urllib.request
import requests
import socket
from bs4 import BeautifulSoup
import sys

arg1=sys.argv[1]
e=arg1
flag=0

if not validators.url(e):
    print ("неверный url-формат")
else:
    try:
        response = requests.get(e)
        flag=1
    except requests.exceptions.ConnectionError:
        print('Поиск dns не удался')
       
#если такой сайт существует то парсим его
if flag==1:
    url = e
    response = requests.get(url)
    page = str(BeautifulSoup(response.content, "html.parser"))
    def getURL(page):
        start_link = page.find("a href")
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1: end_quote]
        return url, end_quote
  
    print ("Найденние почтовие адресса и URL ссылки на сайте- "+e)
    print ()
    while True:
        url, n = getURL(page)
        page = page[n:]
        if url and url[:6]=="mailto" :
            print (url[7:])
        if url and url[:5]=="https" :
            print (url)  
        if url and url[:4]=="http" :
            print (url) 


