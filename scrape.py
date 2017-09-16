#!/usr/bin/env python3
#

from bs4 import BeautifulSoup
import requests
import os
import signal
from utilities import folderInitialize, keyBoardInput, signal_handler, savePDF


#####################################################################
#
# Start at the http://www.emblibrary.com/EL/New.aspx
# or the user entered url.  Search for all product links.
# Then follow those links.  Search for the links within the span
# of class=sizeSpan
#
def findLinks(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

#####################################################################
#
# Scrape the design detail page.  It will have links to a color change page.
# From the color change page, there will be access to a link that will
# download a PDF file.
#
def designDetail(productID, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    anchor = soup.select('a#ColorChangeLink')
    return anchor

#####################################################################
#
#
#
def downloadPDF(productID, href):
    # productID is needed as a query parameter.
    payload = {}
    payload['productID'] = productID
    # Prepare the post data.  This will consist of a couple of hidden input
    # fields and a hard coded string generated by some javascript.
    postData = {}
    postData = {'__EVENTTARGET': 'ctl00$MainContent$productRepeater$ctl00$MakePdfProduct'}
    url = 'http://www.emblibrary.com/EL/' + href
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # The product name is used to form the folder and file name that
    # will store the downloaded color change PDF.
    productName = soup.select('table.content-item.info-table.padded.no-border > tr td:nth-of-type(2)')[0].text.strip()
    print(productID, productName, sep='-')
    # Select the hidden tags from the DOM. Add the hidden values to
    # the post data within a dictionary.
    hidden_tags = soup.select('input[type=hidden]')
    for tag in hidden_tags:
        postData[tag['name']] = tag['value']
    # Request the PDF.
    r = requests.post(url, params=payload, data=postData)
    # PDF is downloaded.  Save in a folder named with the productID
    # and productName.  Make the file name the productID, productName and
    # '.pdf' extension
    savePDF(r, productID, productName)

#####################################################################
# Control the main loop.
#
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    url = keyBoardInput()
    if url is None:
        print("Problem entering date.")
    else:
        print(url)
        folderInitialize()
        mainPage = findLinks(url)  # Return a BeautifulSoup object of the main page
        #
        # Find all the anchor tags that reference design details.
        # There may be different sizes for each design.  Follow each
        # size reference.
        #
        for link in mainPage.select('span.sizeSpan a'):
            detailPageLink = link.get('href')
            params = detailPageLink.split('=')  # params[2] is the productID
            productID = params[2]
            colorChangeLink = designDetail(productID, detailPageLink)  # This function follows design reference
            if not colorChangeLink:
                print(productID, "- Does not have a Color Change Link")
            else:
                designPageLink = colorChangeLink[0].get('href')
                downloadPDF(productID, designPageLink)
