#! /usr/bin/env python3
#
################
#
# product_name.py
#
################
#

"""
Utility function to abbreviate the file names..
"""

import re
from csv_abbrev import read_csv


def modify_product_name(i: str, abbrev: list) -> str:
    n = i
    # Keep these two in order
    n = re.sub("Battenburg Lace", "BBL", n, flags=re.I)
    n = re.sub("Battenburg", "BB", n, flags=re.I)
    # End of Keep these two in order

    # Keep this section as is.  The order is important
    # Replacements are moved to the first of the name.
    # Except for the Freestanding in parentheses
    if n.find('(Freestanding)') >= 0:
        n = n.replace('(Freestanding)', '')
        n = 'FS ' + n
    if n.find('Freestanding') >= 0:
        n = n.replace('Freestanding', 'FS')
    if n.find('(In-the-Hoop') >= 0:
        n = n.replace('(In-the-Hoop)', '')
        n = 'ITH ' + n

    # Keep this in order
    n = re.sub("Crafty Cut Applique", "CCA", n, flags=re.I)
    n = re.sub("Crafty Cut", "CC", n, flags=re.I)
    n = re.sub("Vinyl Applique", "VA", n, flags=re.I)
    n = re.sub("Applique", "App", n, flags=re.I)
    # End of Keep these in order

    # Do the replacements from the abbreviations csv file.
    # Do these before the special cases.
    for abb in abbrev:
        n = re.sub(abb[0], abb[1], n, flags=re.I)

    # Special cases for prepositions, definite article, 'and' and '-'
    n = re.sub("\\W-\\W", " ", n, flags=re.I)
    n = re.sub("\\Wthe\\W", " ", n, flags=re.I)
    n = re.sub("\\Win\\W", " ", n, flags=re.I)
    n = re.sub("\\Wfor\\W", " ", n, flags=re.I)
    n = re.sub("\\Wwith\\W", " w ", n, flags=re.I)
    n = re.sub("\\Wand\\W", " & ", n, flags=re.I)

    # Make sure there are no leading or trailing white space
    n = n.strip()
    return n


if __name__ == "__main__":
    abbrev = read_csv("./el-replacement_names.csv")
    with open("test_string.txt", "r") as test_string:
        for i in test_string.readlines():
            i = i.strip()
            print(modify_product_name(i, abbrev))
