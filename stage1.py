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

    textHTML = string.select('a')
    sentence = []

    for x in textHTML:
        text = x.getText().strip()
        sentence.append(text)

    for phrase in sentence:
        index = phrase.find('New')
        if index != -1:
            print phrase

if __name__ == '__main__':
    getText()

