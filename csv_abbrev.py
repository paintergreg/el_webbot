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
Open, read and convert the data to a list of sring lists.
"""

import csv
from pathlib import Path


def read_csv() -> list:
    a = []
    abbreviation_file = Path("/home/greg/Dropbox/AAA/el-replacement-names.csv")
    with open(abbreviation_file) as cvsfile:
        abbreviations = csv.reader(cvsfile)
        a = list(abbreviations)
    return a


if __name__ == '__main__':
    abbreviations = read_csv()
    for abbrev in abbreviations:
        print(f"{abbrev[0]}\t{abbrev[1]}")
