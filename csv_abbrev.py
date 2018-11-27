#! /usr/bin/env python3
#
################
#
# csv_abbrev.py
#
################
#

"""
Tempory file to test modifiing the product name.
"""

import csv
from pathlib import Path


def read_csv() -> list:
    a = []
    abbreviation_file = Path("/home/greg/Dropbox/AAA/el-replacement-names.csv")
    abbreviations = csv.reader(open(abbreviation_file))
    for abb in abbreviations:
        a.append([abb[0], abb[1]])
    return a


if __name__ == '__main__':
    abbreviations = read_csv()
    for abbrev in abbreviations:
        print(f"name: {abbrev[0]}  a: {abbrev[1]}")
