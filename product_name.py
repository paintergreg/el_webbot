#! /usr/bin/env python3
#
################
#
# product_name.py
#
################
#

"""
Tempory file to test modifiing the product name.
"""

import re


def modify_product_name(i):
    n = i
    n = re.sub("Battenburg Lace", "BBL", n, flags=re.I)
    n = re.sub("Battenburg", "BBL", n, flags=re.I)

    if n.find('(Freestanding)') >= 0:
        n = n.replace('(Freestanding)', '')
        n = 'FS ' + n
    if n.find('Freestanding') >= 0:
        n = n.replace('Freestanding', 'FS')
    if n.find('(In-the-Hoop') >= 0:
        n = n.replace('(In-the-Hoop)', '')
        n = 'ITH ' + n

    n = re.sub("\Wwith\W", " w ", n, flags=re.I)
    n = re.sub("\Wand\W", " & ", n, flags=re.I)

    # Keep this in order
    n = re.sub("Crafty Cut Applique", "CCA", n, flags=re.I)
    n = re.sub("Crafty Cut", "CC", n, flags=re.I)
    n = re.sub("Vinyl Applique", "VA", n, flags=re.I)
    n = re.sub("Applique", "App", n, flags=re.I)
    # End of Keep these in order

    n = re.sub("Christmas", "Xmas", n, flags=re.I)
    n = re.sub("Whitework", "WW", n, flags=re.I)
    n = re.sub("Vintage", "V", n, flags=re.I)
    n = re.sub("Organza", "O", n, flags=re.I)

    n = re.sub("Puff Foam", "PF", n, flags=re.I)
    n = re.sub("Thick Thread", "TT", n, flags=re.I)
    n = re.sub("Cardstock", "CS", n, flags=re.I)
    n = re.sub("Redwork", "RW", n, flags=re.I)

    n = re.sub("Embossed", "EM", n, flags=re.I)
    n = re.sub("Double Run", "DR", n, flags=re.I)
    n = re.sub("Ornament", "Ornie", n, flags=re.I)
    n = re.sub("Border", "Brdr", n, flags=re.I)

    n = re.sub("Butterfly", "Btrfly", n, flags=re.I)
    n = re.sub("Poinsettia", "Pnseta", n, flags=re.I)
    n = re.sub("Watercolor", "Wtrclr", n, flags=re.I)
    n = re.sub("Square", "Sq", n, flags=re.I)

    n = re.sub('Accent', 'Acnt', n, flags=re.I)
    n = re.sub('Etching', 'Etch', n, flags=re.I)
    n = re.sub('Goldwork', 'GW', n, flags=re.I)
    n = re.sub('Halloween', 'Halwen', n, flags=re.I)

    n = re.sub('Not-So-Spooky', 'Not Spooky', n, flags=re.I)
    n = re.sub('Bountiful', 'Bntfl', n, flags=re.I)
    n = re.sub('Pumpkin', 'Pmpkn', n, flags=re.I)
    n = re.sub('Harvest', 'Hvst', n, flags=re.I)

    n = re.sub('Autumn', 'Atmn', n, flags=re.I)
    n = re.sub('Topiary', 'Tpry', n, flags=re.I)
    n = re.sub('Jacobean', 'Jbean', n, flags=re.I)
    n = re.sub('Enchanted', 'Echnt', n, flags=re.I)

    n = re.sub('Blossoming', 'Blosm', n, flags=re.I)
    n = re.sub('Medallion', 'Mdln', n, flags=re.I)
    n = re.sub('Woodland', 'Wlnd', n, flags=re.I)
    n = re.sub('Fantastic', 'Fntstc', n, flags=re.I)

    n = re.sub('Marvelous', 'Mrvls', n, flags=re.I)
    n = re.sub('Top of the Line -', 'TOL', n, flags=re.I)
    n = re.sub('Blooming', 'Blmg', n, flags=re.I)
    n = re.sub('Dinosaurs', 'Dnsrs', n, flags=re.I)

    n = re.sub('Lightening', 'Lghtng', n, flags=re.I)
    n = re.sub('Trapunto', 'Tpnto', n, flags=re.I)
    n = re.sub('Southwestern', 'Swtrn', n, flags=re.I)
    n = re.sub('Delightful', 'Dltfl', n, flags=re.I)

    n = re.sub('Ballerina', 'Blnra', n, flags=re.I)
    n = re.sub('Bouquet', 'Bqt', n, flags=re.I)
    n = re.sub('Sunflower', 'Snflwr', n, flags=re.I)
    n = re.sub('Schematic', 'Scmtc', n, flags=re.I)

    n = re.sub('Balloon', 'Baln', n, flags=re.I)
    n = re.sub('Impossible', 'Impsbl', n, flags=re.I)
    n = re.sub('Hummingbird', 'Hmgbrd', n, flags=re.I)
    n = re.sub('Snowflake', 'Snflk', n, flags=re.I)

    if n.find('Wonderland') >= 0:
        n = n.replace('Wonderland', 'Wdrlnd')

    if n.find('Monarch') >= 0:
        n = n.replace('Monarch', 'Mnrh')

    if n.find('Dazzling') >= 0:
        n = n.replace('Dazzling', 'Dzlng')

    if n.find('Delicate') >= 0:
        n = n.replace('Delicate', 'Dlcte')

    if n.find('Monday') >= 0:
        n = n.replace('Monday', 'Mon')

    if n.find('Tuesday') >= 0:
        n = n.replace('Tuesday', 'Tue')

    if n.find('Wednesday') >= 0:
        n = n.replace('Wednesday', 'Wed')

    if n.find('Thursday') >= 0:
        n = n.replace('Thursday', 'Thu')

    if n.find('Friday') >= 0:
        n = n.replace('Friday', 'Fri')

    if n.find('Saturday') >= 0:
        n = n.replace('Saturday', 'Sat')

    if n.find('Sunday') >= 0:
        n = n.replace('Sunday', 'Sun')

    if n.find('Baroque') >= 0:
        n = n.replace('Baroque', 'Brqe')

    if n.find('Goldfinch') >= 0:
        n = n.replace('Goldfinch', 'Gldfnh')

    if n.find('Botanicals') >= 0:
        n = n.replace('Botanicals', 'Btncls')

    if n.find('Goldfish') >= 0:
        n = n.replace('Goldfish', 'Gldfsh')

    if n.find('Kaleidoscope') >= 0:
        n = n.replace('Kaleidoscope', 'Kldscpe')

    if n.find('Ironwork') >= 0:
        n = n.replace('Ironwork', 'Irnwrk')

    if n.find('Moroccan') >= 0:
        n = n.replace('Moroccan', 'Mrcn')

    if n.find('Quilting') >= 0:
        n = n.replace('Quilting', 'Qltng')

    if n.find('Nouveau') >= 0:
        n = n.replace('Nouveau', 'Nvu')

    if n.find('Japanese') >= 0:
        n = n.replace('Japanese', 'Jpnse')

    if n.find('Dragonfly') >= 0:
        n = n.replace('Dragonfly', 'Drgfl')

    if n.find('Birdhouse') >= 0:
        n = n.replace('Birdhouse', 'Brdhs')

    if n.find('Majestic') >= 0:
        n = n.replace('Majestic', 'Mjstc')

    if n.find('American') >= 0:
        n = n.replace('American', 'Amrcn')

    if n.find('Exquisite') >= 0:
        n = n.replace('Exquisite', 'Exqst')

    if n.find('Lighthouse') >= 0:
        n = n.replace('Lighthouse', 'Lthse')

    if n.find('Starfish') >= 0:
        n = n.replace('Starfish', 'Strfs')

    if n.find('Seafood') >= 0:
        n = n.replace('Seafood', 'Sefd')

    if n.find('Adventure') >= 0:
        n = n.replace('Adventure', 'Advntr')

    if n.find('Patchwork') >= 0:
        n = n.replace('Patchwork', 'Ptwrk')

    if n.find('Free-Flying') >= 0:
        n = n.replace('Free-Flying', 'FF')

    if n.find('Rainforest') >= 0:
        n = n.replace('Rainforest', 'Rnfrst')

    if n.find('Madagascan') >= 0:
        n = n.replace('Madagascan', 'Mdgscn')

    if n.find('Forget-Me-Not') >= 0:
        n = n.replace('Forget-Me-Not', 'FMN')

    if n.find('Dragonflies') >= 0:
        n = n.replace('Dragonflies', 'Drgnfls')

    if n.find(' - ') >= 0:
        n = n.replace(' - ', ' ')

    if n.find('Heirloom') >= 0:
        n = n.replace('Heirloom', 'Hrlm')

    if n.find('Wintertide') >= 0:
        n = n.replace('Wintertide', 'Wntrtd')

    if n.find('Snowman') >= 0:
        n = n.replace('Snowman', 'Snwmn')

    if n.find('Reindeer') >= 0:
        n = n.replace('Reindeer', 'Rndr')

    if n.find('Nutcracker') >= 0:
        n = n.replace('Nutcracker', 'Ntcrkr')

    if n.find('Blizzard') >= 0:
        n = n.replace('Blizzard', 'Blzrd')

    if n.find('Farmhouse') >= 0:
        n = n.replace('Farmhouse', 'Frmhse')

    if n.find('Festive') >= 0:
        n = n.replace('Festive', 'Fstv')

    if n.find('On-the-Go') >= 0:
        n = n.replace('On-the-Go', 'OtG')

    if n.find('Eggnog') >= 0:
        n = n.replace('Eggnog', 'Egng')

    if n.find('Jingle') >= 0:
        n = n.replace('Jingle', 'Jngl')

    if n.find('Holiday') >= 0:
        n = n.replace('Holiday', 'Hldy')

    if n.find('Snowglobe') >= 0:
        n = n.replace('Snowglobe', 'Snwglb')

    if n.find('Peppermint') >= 0:
        n = n.replace('Peppermint', 'Ppmt')

    if n.find('Chipmunk') >= 0:
        n = n.replace('Chipmunk', 'Cpmk')

    # if n.find('Gingerbread') >= 0:
    #     n = n.replace('Gingerbread', 'Gngbrd')
    n = re.sub("\WGingerbread\W", " Gngbrd ", n, flags=re.I)

    # if n.find('Songbird') >= 0:
    #     n = n.replace('Songbird', 'Sngbrd')
    n = re.sub("\WSongbird\W", " Sngbrd ", n, flags=re.I)

    # if n.find('Chickadees') >= 0:
    #     n = n.replace('Chickadees', 'Chkds')
    n = re.sub("\WChickadees\W", " Chkds ", n, flags=re.I)

    # if n.lower().find(' the ') >= 0:
    #     n = n.lower().replace(' the ', ' ')

    n = re.sub("\WThe\W", " ", n, flags=re.I)
    n = re.sub("\Wfor\W", " ", n, flags=re.I)
    # if n.find(' For ') >= 0:
    #     n = n.replace(' For ', ' ')

    n = n.strip()
    return n


if __name__ == "__main__":
    names = [
            'Fall into Autumn Quilt (Battenburg)',
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
            'An Applique with (Crafty Cut Applique)',
            'Ballerina Bouquet Sunflower Schematic Balloon Impossible',
            'Hummingbird Snowflake Wonderland'
            'Sunday Monday Tuesday Wednesday Thursday Friday Saturday',
            'Baroque Goldfinch Botanicals Kaleidoscope Ironwork Moroccan',
            'Quilting Nouveau Japanese Dragonfly Birdhouse Majestic American',
            'Exquisite Space - Space Lighthouse Starfish Seafood Adventure',
            'Patchwork Free-Flying Rainforest Madagascan Forget-Me-Not',
            'Dragonflies',
            'Heirloom Wintertide Snowman Reindeer Nutcracker Blizzard',
            'Farmhouse for Festive For Whatforis this On-the-Go Eggnog Jingle Holiday Snowglobe',
            'Peppermint Chipmunk Gingerbread the Songbird the Chickadees The For ',
            'whattheis this',
            'No changes'
            ]
    for i in names:
        print(modify_product_name(i))
