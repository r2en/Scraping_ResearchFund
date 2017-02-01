#!/usr/bin/python
# -*- coding: utf-8 -*-
# Random output
import random
import requests
import bs4
import datetime
import os.path
import re
from twitterTokens import tokens
import tweepy

r = re.compile("(.*)( )")

url = 'http://www.rcp.keio.ac.jp/ora/'
#print ('Scraping URL : '+url) 

res = requests.get(url)
string = bs4.BeautifulSoup(res.text.encode(res.encoding), "html.parser")

num = 0
 
def getText():

    parseURL = string.select("a[href*='jukunai']")
    sentence = []

    for text,url in zip(parseURL,parseURL):
        tmp=[]
        tmp.append(text.getText().encode('utf-8').strip())
        tmp.append("http://www.rcp.keio.ac.jp/ora/"+url.get('href'))
        sentence.append(tmp)
    global num
    num = len(sentence)
    return sentence

def getMenu():
    latest_sentence = []
    # New fund
    sentence = getText()
    for i in range(num):
        latest_sentence = sentence[i]
        index = latest_sentence[0].find('New')
        if index != -1:
            count = 0
            f = open('write.txt','r')
            len_num = sum(1 for line in 'write.txt')
            while len_num >= 0:
                line1 = f.readline()
                line2 = line1.strip()
                m = r.match(line2)
                if m != None:
                    if m.group(1) == latest_sentence[0]:
                        count += 1
                        #print line2
                len_num -= 1
            if count == 0:
                #tweet processing
                f.close()
                #return [latest_sentence[0],latest_sentence[1]]
                tweet_text = latest_sentence[0]
                tweet_url = latest_sentence[1]
                return [tweet_text,tweet_url]

def reWrite():
# remove old file and write new file
    os.remove('write.txt')
    sentence = getText()
    for i in range(num):
        latest_sentence = sentence[i]
        index = latest_sentence[0].find('New')
        if index != -1:
            w = open('write.txt','a')
            w.write(latest_sentence[0])
            w.write(' ')
            w.write(latest_sentence[1])
            w.write('\n')
            w.close()

    #print str(sentence).decode('string-escape')

def tweetMenu():
    text,url = getMenu()
    print "tweetMenu"
    # set tokens
    CONSUMER_KEY = tokens['consumer_key']
    CONSUMER_SECRET = tokens['consumer_secret']
    ACCESS_TOKEN = tokens['access_token']
    ACCESS_TOKEN_SECRET = tokens['access_token_secret']
    # auth process
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    # send tweet
    api.update_status(unicode(text,'utf-8') + url)

if __name__ == '__main__':
    getText()
    getMenu()
    tweetMenu()
    reWrite()
