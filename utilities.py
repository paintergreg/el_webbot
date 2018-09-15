#!/usr/bin/env python3
#
import re
import os
import sys
from shutil import rmtree
from datetime import datetime

defaultURL = "https://www.emblibrary.com/EL/New.aspx"


def folderInitialize(folder_name):
    """
    Make sure the folder to store the PDF files is empty.
    The folder must be empty to begin or the PDF files will build.
    """
    BASEDIR = os.path.join(folder_name)
    if os.path.exists(BASEDIR):
        rmtree(BASEDIR)  # if new_folder exists remove it and all children
    os.makedirs(BASEDIR)  # Create an empty new_folder folder.


def savePDF(r, productID, productName, folder_name):
    """
    Save the PDF in a folder named with the productID and productName.
    Make the file name the productID, productName and '.pdf' extension
    """
    dirPath = os.path.join('.', folder_name, productID + ' ' + productName)
    os.makedirs(dirPath, exist_ok=True)
    filePath = f'{productID} {productName}.pdf'
    chunk_size = 2048
    with open(os.path.join(dirPath, filePath), 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)


def signal_handler(sig, frame):
    """
    Exit the application gracefully if CTRL-C was entered.
    """
    print('\nApplication interrupted...')
    sys.exit(0)


def keyBoardInput():
    """
    User input to select the week to download.  User enters DD-MM-YY or
    and empty string.  Embrodiery Library accepts the date at MMDDYY.
    """
    url = defaultURL
    i = input(
        "Enter Date as: DD-MM-YY or DD/MM/YY or DDMMYY or Return for today: ")
    if i != "":
        now = validDate(i)
        if now is not None:
            date = now.strftime("%m%d%y")
            url += "?date=" + date
        else:
            return None
    return((url, now.strftime("%Y-%m-%d")))


def validDate(datestring):
    """
    Validate the user entered a string that can be converted to a
    valid date.
    """
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
            print(now.strftime("%Y-%m-%d"))
            return now
    except ValueError:
        print("DateError")
    return None
