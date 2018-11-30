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
    n = re.sub("\W-\W", " ", n, flags=re.I)
    n = re.sub("\Wthe\W", " ", n, flags=re.I)
    n = re.sub("\Wfor\W", " ", n, flags=re.I)
    n = re.sub("\Wwith\W", " w ", n, flags=re.I)
    n = re.sub("\Wand\W", " & ", n, flags=re.I)

    # Make sure there are no leading or trailing white space
    n = n.strip()
    return n


if __name__ == "__main__":
    names = [
            'Fall into Autumn Quilt Accent Adventure (Battenburg)',
            'Fall into Autumn Quilt (Battenburg Lace with Rayon)',
            'Fall into Autumn Quilt (Battenburg Lace)',
            'Exquisite Blue Jay Feather (Freestanding)',
            'Freestanding Daffodil in 3D (In-the-Hoop)',
            'Bell Flower (In-the-Hoop)',
            "Mum's the Word Flower Spray (Whitework)",
            'Autumn Elegance Medallion (Vintage)',
            'Brushed Lion (Thick Thread)',
            'Midnight Meowmance Shadowbox (Organza)',
            "Jolly Jack O' Lantern (Crafty Cut)",
            'Harvest Pumpkin (Embossed)',
            'Bountiful Harvest Bouquet (Vinyl Applique)',
            'Bountiful and Harvest Bouquet (Vinyl Applique)',
            'Homespun Merry Christmas (Puff FoaM)',
            'Autumn Leaves and Pumpkins with Please (Double Run)',
            'Autumn Leaves and Pumpkins with Please (Cardstock)',
            'Autumn Leaves and Pumpkins with Please (Redwork)',
            'Autumn Leaves and Pumpkins with Please (Embossed)',
            'Homespun Pine Bough and Ornaments',
            'Homespun Pine Bough Ornament and Ornaments',
            'This Border is safe',
            'Little girls and Butterflys',
            'Poinsettia is a flower',
            'Paint a Poinsettia with Watercolor',
            'Accent the Border with Squares',
            'Not-So-Spooky Bountiful Harvest Pumpkin in Topiary for Halloween',
            'A Square Accent in Etching (Goldwork)',
            'A Jacobean Enchanted Blossoming Medallion Top of the Line -',
            'Fantastic, Marvelous, Blooming Dinosaurs Lightening',
            'Southwestern (Trapunto) Delightful Monarch Dazzling Delicate',
            'An - Applique with (Crafty Cut Applique)',
            'Ballerina Bouquet Sunflower Schematic Balloon Impossible',
            'Hummingbird Snowflake Wonderland Monarch Dazzling Delicate',
            'Sunday Monday Tuesday Wednesday Thursday Friday Saturday',
            'Baroque Goldfinch Botanicals Kaleidoscope Ironwork Moroccan',
            'Quilting Nouveau Japanese Dragonfly Birdhouse Majestic American',
            'Exquisite Space - Space Lighthouse Starfish Seafood Adventure',
            'Patchwork Free-Flying Rainforest Madagascan Forget-Me-Not',
            'Dragonflies',
            'Heirloom Wintertide Snowman Reindeer Nutcracker Blizzard',
            'Farmhouse for Festive For Whatforis this On-the-Go Eggnog',
            ' Jingle Holiday Snowglobe',
            'Peppermint Chipmunk Gingerbread the Songbird the Chickadees',
            'This is a merry Merry Bear Cardinal',
            'whattheis this The For Goldwork Goldfish (Cutwork)',
            'whattheis this',
            'No changes'
            ]
    abbrev = read_csv()
    for i in names:
        print(modify_product_name(i, abbrev))
