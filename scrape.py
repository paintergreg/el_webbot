#!/usr/bin/env python3
#

from bs4 import BeautifulSoup
import requests
import os

#
# Start at the http://www.emblibrary.com/EL/New.aspx
# or the user entered url.  Search for all product links.
# Then follow those links.  Search for the links within the span
# of class=sizeSpan
#
def findLinks(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.select('span.sizeSpan a'):
        href = link.get('href')
        params = href.split('=')  # params[2] is the productID
        # print(params[2])
        # print(href)
        designDetail(params[2], href)
        # print(type(href))
        # if(type(href) is str):
        #     if href.find('ProductID') != -1:
        #         print(link.get('href'))

def designDetail(productID, url):
    print(productID, url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    anchor = soup.select('a#ColorChangeLink')
    href = anchor[0].get('href')
    findParams(productID, href)

def findParams(productID, href):
    print(productID, href)
    chunk_size = 2048
    payload = {}
    payload['productID'] = productID
    postData = {}
    postData = {'__EVENTTARGET': 'ctl00$MainContent$productRepeater$ctl00$MakePdfProduct'}
    url = 'http://www.emblibrary.com/EL/' + href
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    hidden_tags = soup.findAll(attrs={"type" : "hidden"})
    print(hidden_tags[0]['value'])
    for tag in hidden_tags:
        print(tag['value'], tag['type'], tag['name'])
        postData[tag['name']] = tag['value']
    r = requests.post(url, params=payload, data=postData)
    print(r.url)
    filePath = './AAATemp/' + productID + '.pdf'
    with open(filePath, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)


if __name__ == "__main__":
    findLinks('http://www.emblibrary.com/EL/New.aspx')
    # findParams()
