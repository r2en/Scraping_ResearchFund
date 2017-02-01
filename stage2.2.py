#!/usr/bin/python
# -*- coding: utf-8 -*-
# Random output
import random
import requests
import bs4
import datetime#!/usr/bin/python

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
    num = len(sentence)
    
    for i in range(num):
        latest_sentence = sentence[i]
        index = latest_sentence[0].find('New')
        if index != -1:
            print latest_sentence[0],latest_sentence[1]

    #print str(sentence).decode('string-escape')

if __name__ == '__main__':
    getText()
