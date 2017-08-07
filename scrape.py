#!/usr/bin/env python3
#

from bs4 import BeautifulSoup
import requests
import os
from shutil import rmtree

BASEDIR = './AAATemp/'

#
# Start at the http://www.emblibrary.com/EL/New.aspx
# or the user entered url.  Search for all product links.
# Then follow those links.  Search for the links within the span
# of class=sizeSpan
#
def findLinks(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    #
    # Find all the anchor tags that reference design details.
    # There may be different sizes for each design.  Follow each
    # size reference.
    #
    for link in soup.select('span.sizeSpan a'):
        href = link.get('href')
        params = href.split('=')  # params[2] is the productID
        designDetail(params[2], href)  # This function follows design reference

def designDetail(productID, url):
    # print(productID, url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    anchor = soup.select('a#ColorChangeLink')
    href = anchor[0].get('href')
    downloadPDF(productID, href)

def downloadPDF(productID, href):
    # print(productID, href)
    chunk_size = 2048
    payload = {}
    payload['productID'] = productID
    postData = {}
    postData = {'__EVENTTARGET': 'ctl00$MainContent$productRepeater$ctl00$MakePdfProduct'}
    url = 'http://www.emblibrary.com/EL/' + href
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    productName = soup.select('table.content-item.info-table.padded.no-border > tr td:nth-of-type(2)')[0].text.strip()
    print(productName, productID)
    # print(soup.prettify())
    hidden_tags = soup.findAll(attrs={"type" : "hidden"})
    # print(hidden_tags[0]['value'])
    for tag in hidden_tags:
        # print(tag['value'], tag['type'], tag['name'])
        postData[tag['name']] = tag['value']
    r = requests.post(url, params=payload, data=postData)
    dirPath = './AAATemp/' + productID + ' ' + productName + '/'
    os.makedirs(dirPath, exist_ok=True)
    filePath =  productID + ' ' + productName + '.pdf'
    with open(dirPath + filePath, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)

#
# Make sure the folder to store the PDF files is gone.
# The folder must be empty to begin or the PDF file will build.
#
def folderInitialize():
    rmtree(BASEDIR)

if __name__ == "__main__":
    folderInitialize()
    # findLinks('http://www.emblibrary.com/EL/New.aspx')
