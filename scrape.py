#!/usr/bin/env python3
#

from bs4 import BeautifulSoup
import requests
import signal
from utilities import folderInitialize, keyBoardInput, signal_handler, savePDF
from product_name import modify_product_name
from csv_abbrev import read_csv

def findLinks(url):
    """
    Start at the https://www.emblibrary.com/EL/New.aspx
    or the user entered url.  Search for all product links.
    Then follow those links.  Search for the links within the span
    of class=sizeSpan
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def designDetail(productID, url):
    """
    Scrape the design detail page.  It will have links to a color change page.
    From the color change page, there will be access to a link that will
    download a PDF file.
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    anchor = soup.select('a#ColorChangeLink')
    return anchor


def downloadPDF(productID, href, abbreviations: list):
    # productID is needed as a query parameter.
    payload = {}
    payload['productID'] = productID
    # Prepare the post data.  This will consist of a couple of hidden input
    # fields and a hard coded string generated by some javascript.
    postData = {}
    postData = {'__EVENTTARGET': 'ctl00$MainContent$productRepeater$ctl00$MakePdfProduct'}
    url = 'https://www.emblibrary.com/EL/' + href
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # The product name is used to form the folder and file name that
    # will store the downloaded color change PDF.
    xsel = 'table.content-item.info-table.padded.no-border > tr td:nth-of-type(2)'
    productName = soup.select(xsel)[0].text.strip()
    mod_name = modify_product_name(productName, abbreviations)
    print(f'{productID}-{mod_name}')
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
    savePDF(r, productID, mod_name)


if __name__ == "__main__":
    """
    Control the main loop.
    """
    signal.signal(signal.SIGINT, signal_handler)
    input_data = keyBoardInput()
    url = input_data[0]
    folder_name = input_data[1]
    if url is None:
        print("Problem entering date.")
    else:
        abbrevations = read_csv()
        print(f'{url}')
        folderInitialize(folder_name)
        # Return a BeautifulSoup object of the main page
        mainPage = findLinks(url)
        #
        # Find all the anchor tags that reference design details.
        # There may be different sizes for each design.  Follow each
        # size reference.
        #
        for link in mainPage.select('span.sizeSpan a'):
            detailPageLink = link.get('href')
            params = detailPageLink.split('=')  # params[2] is the productID
            productID = params[2]
            # This function follows the design reference
            colorChangeLink = designDetail(productID, detailPageLink)
            if not colorChangeLink:
                print(productID, "- Does not have a Color Change Link")
            else:
                designPageLink = colorChangeLink[0].get('href')
                downloadPDF(productID, designPageLink, abbrevations)
