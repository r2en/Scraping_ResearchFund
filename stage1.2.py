#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import requests
import bs4
import datetime
import re

url = 'http://www.rcp.keio.ac.jp/ora/'
print ('Scraping URL : '+url) 

res = requests.get(url)
string = bs4.BeautifulSoup(res.text.encode(res.encoding), "html.parser")

def getText():

    parseURL = string.select("a[href*='jukunai']")
    sentence = []

    for text,url in zip(parseURL,parseURL):
        tmp=[]
        tmp.append(text.getText().encode('utf-8').strip())
        tmp.append("http://www.rcp.keio.ac.jp/ora/"+url.get('href'))
        sentence.append(tmp)

    print str(sentence).decode('string-escape')

if __name__ == '__main__':
    getText()