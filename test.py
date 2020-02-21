#! /usr/bin/env python3
#
################
#
# test.py
#
################
#

"""
docstring goes here.  be sure to write a good one ;)
"""

import unittest
import os
from csv_abbrev import read_csv
from product_name import modify_product_name
from utilities import folderInitialize
from shutil import rmtree


class AllTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        if os.path.exists("AAATemp/TempFolder"):
            rmtree("AAATemp/TempFolder")

    def test_read_csv_file(self):
        abbreviations = read_csv("./el-replacement-names.csv")
        self.assertNotIn(["Adundant", "Abndt"], abbreviations)
        self.assertIn(["Admiral", "Admrl"], abbreviations)
        self.assertIn(["Accent", "Acnt"], abbreviations)
        self.assertIn(["Wednesday", "Wed"], abbreviations)
        self.assertIn(["Honey", "Hny"], abbreviations)

    def test_abbreviate_strings(self):
        abbrev = read_csv("./el-replacement-names.csv")
        with open("test_string.txt", "r") as test_string:
            for i in test_string.readlines():
                i = i.strip()
                if i == "Fall into Autumn Quilt Accent Adventure (Battenburg)":
                    self.assertEqual(
                        "Fall into Atmn Qlt Acnt Advntr BB",
                        modify_product_name(i, abbrev),
                    )
                if i == "No changes":
                    self.assertEqual(
                        "No changes", modify_product_name(i, abbrev)
                    )
                if i == "Exquisite Blue Jay Feather (Freestanding)":
                    self.assertEqual(
                        "FS Exqst Blue Jay Feather",
                        modify_product_name(i, abbrev),
                    )
                # print(i + "\n" + modify_product_name(i, abbrev))

    def test_folderInitialize(self):
        BaseDir = folderInitialize("TempFolder")
        self.assertEqual(os.path.exists(BaseDir), 1)


if __name__ == "__main__":
    unittest.main()
