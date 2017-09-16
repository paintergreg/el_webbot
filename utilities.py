#!/usr/bin/env python3
#
import re
import os
import sys
from shutil import rmtree
import signal
from datetime import datetime

defaultURL = "http://www.emblibrary.com/EL/New.aspx"
BASEDIR = os.path.join('AAATemp')

#####################################################################
#
# Make sure the folder to store the PDF files is empty.
# The folder must be empty to begin or the PDF files will build.
#
def folderInitialize():
    if os.path.exists(BASEDIR):
        rmtree(BASEDIR)  # if BASEDIR exists remove it and all children
    os.makedirs(BASEDIR) # Create an empty BASEDIR folder.

#####################################################################
# Save the PDF in a folder named with the productID and productName.
# Make the file name the productID, productName and '.pdf' extension
#
def savePDF(r, productID, productName):
    dirPath = os.path.join('.', BASEDIR, productID + ' ' + productName)
    os.makedirs(dirPath, exist_ok=True)
    filePath =  productID + ' ' + productName + '.pdf'
    chunk_size = 2048
    with open(os.path.join(dirPath, filePath), 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)

#####################################################################
#
# Exit the application gracefully if CTRL-C was entered.
#
def signal_handler(signal, frame):
    print('\nApplication interrupted...')
    sys.exit(0)

#####################################################################
#
# User input to select the week to download.  User enters DD-MM-YY or
# and empty string.  Embrodiery Library accepts the date at MMDDYY.
#
def keyBoardInput():
    url = defaultURL
    i = input("Enter Date as: DD-MM-YY or DD/MM/YY or DDMMYY or Return for today: ")
    if i != "":
        date = validDate(i)
        if date is not None:
            url += "?date=" + date
        else:
            return None
    return(url)

#####################################################################
# Validate the user entered a string that can be converted to a
# valid date.
#
def validDate(datestring):
    regex = re.compile(r"""
                (\d{1,2})[/-]?
                (\d{1,2})[/-]?
                (\d{2,4})
                """, re.VERBOSE)
    mat = regex.search(datestring)

    try:
        if mat is not None:
            now = datetime(*(map(int, mat.groups()[-1::-1])))
            print(now)
            return now.strftime("%m%d%y")
    except ValueError:
        print("DateError")
    return None
