#! /usr/bin/env python3
#
################
#
# csv_abbrev.py
#
################
#

"""
Abbreviations to the file names are in a csv file.
Open, read and convert the data to a list of string lists.
"""

import csv
import os
from pathlib import Path
from dotenv import load_dotenv


def read_csv(f: str) -> list:
    a = []
    abbreviation_file = Path(f)
    with open(abbreviation_file) as cvsfile:
        abbreviations = csv.reader(cvsfile)
        a = list(abbreviations)
    return a


if __name__ == '__main__':
    load_dotenv()
    abbreviations = read_csv("./el-replacement-names.csv")
    for abbrev in abbreviations:
        print(f"{abbrev[0]}\t{abbrev[1]}")
    x = os.getenv("TESTING")
    print(f"TESTING={x}")
    if not x:
        print(f"TESTING={x}")
