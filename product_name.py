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
    if n.find('Battenburg Lace') >= 0:
        n = n.replace('Battenburg Lace', 'BBL')
    elif n.find('Battenburg') >= 0:
        n = n.replace('Battenburg', 'BBL')

    if n.find('(Freestanding)') >= 0:
        n = n.replace('(Freestanding)', '')
        n = 'FS ' + n
    if n.find('Freestanding') >= 0:
        n = n.replace('Freestanding', 'FS')
    if n.find('(In-the-Hoop') >= 0:
        n = n.replace('(In-the-Hoop)', '')
        n = 'ITH ' + n

    if n.find(' with ') >= 0:
        n = n.replace(' with ', ' w ')

    # Keep this in order
    if n.find('Crafty Cut Applique') >= 0:
        n = n.replace('Crafty Cut Applique', 'CCA')

    if n.find('Crafty Cut') >= 0:
        n = n.replace('Crafty Cut', 'CC')

    if n.find('Vinyl Applique') >= 0:
        n = n.replace('Vinyl Applique', 'VA')

    if n.find('Applique') >= 0:
        n = n.replace('Applique', 'App')
    # End of Keep these in order

    if n.find('Christmas') >= 0:
        n = n.replace('Christmas', 'Xmas')

    if n.find('Whitework') >= 0:
        n = n.replace('Whitework', 'WW')

    if n.find('Vintage') >= 0:
        n = n.replace('Vintage', 'V')

    if n.find(' and ') >= 0:
        n = n.replace(' and ', ' & ')

    if n.find('Organza') >= 0:
        n = n.replace('Organza', 'O')

    if n.find('Puff Foam') >= 0:
        n = n.replace('Puff Foam', 'PF')

    if n.find('Thick Thread') >= 0:
        n = n.replace('Thick Thread', 'TT')

    if n.find('Cardstock') >= 0:
        n = n.replace('Cardstock', 'CS')

    if n.find('Redwork') >= 0:
        n = n.replace('Redwork', 'RW')

    if n.find('Embossed') >= 0:
        n = n.replace('Embossed', 'EM')

    if n.find('Double Run') >= 0:
        n = n.replace('Double Run', 'DR')

    if n.find('Ornament') >= 0:
        n = n.replace('Ornament', 'Ornie')

    if n.find('Border') >= 0:
        n = n.replace('Border', 'Brdr')

    if n.find('Butterfly') >= 0:
        n = n.replace('Butterfly', 'Btrfly')

    if n.find('Poinsettia') >= 0:
        n = n.replace('Poinsettia', 'Pnseta')

    if n.find('Watercolor') >= 0:
        n = n.replace('Watercolor', 'Wtrclr')

    if n.find('Square') >= 0:
        n = n.replace('Square', 'Sq')

    if n.find('Accent') >= 0:
        n = n.replace('Accent', 'Acnt')

    if n.find('Etching') >= 0:
        n = n.replace('Etching', 'Etch')

    if n.find('Goldwork') >= 0:
        n = n.replace('Goldwork', 'GW')

    if n.find('Halloween') >= 0:
        n = n.replace('Halloween', 'Halwen')

    if n.find('Not-So-Spooky') >= 0:
        n = n.replace('Not-So-Spooky', 'Not Spooky')

    if n.find('Bountiful') >= 0:
        n = n.replace('Bountiful', 'Bntfl')

    if n.find('Pumpkin') >= 0:
        n = n.replace('Pumpkin', 'Pmpkn')

    if n.find('Harvest') >= 0:
        n = n.replace('Harvest', 'Hvst')

    if n.find('Autumn') >= 0:
        n = n.replace('Autumn', 'Atmn')

    if n.find('Topiary') >= 0:
        n = n.replace('Topiary', 'Tpry')

    if n.find('Jacobean') >= 0:
        n = n.replace('Jacobean', 'Jbean')

    if n.find('Enchanted') >= 0:
        n = n.replace('Enchanted', 'Echnt')

    if n.find('Blossoming') >= 0:
        n = n.replace('Blossoming', 'Blosm')

    if n.find('Medallion') >= 0:
        n = n.replace('Medallion', 'Mdln')

    if n.find('Woodland') >= 0:
        n = n.replace('Woodland', 'Wlnd')

    if n.find('Fantastic') >= 0:
        n = n.replace('Fantastic', 'Fntstc')

    if n.find('Marvelous') >= 0:
        n = n.replace('Marvelous', 'Mrvls')

    if n.find('Top of the Line -') >= 0:
        n = n.replace('Top of the Line -', 'TOL')

    if n.find('Blooming') >= 0:
        n = n.replace('Blooming', 'Blmg')

    if n.find('Dinosaurs') >= 0:
        n = n.replace('Dinosaurs', 'Dnsrs')

    if n.find('Lightening') >= 0:
        n = n.replace('Lightening', 'Lghtng')

    if n.find('Trapunto') >= 0:
        n = n.replace('Trapunto', 'Tpnto')

    if n.find('Southwestern') >= 0:
        n = n.replace('Southwestern', 'Swtrn')

    if n.find('Delightful') >= 0:
        n = n.replace('Delightful', 'Dltfl')

    if n.find('Ballerina') >= 0:
        n = n.replace('Ballerina', 'Blnra')

    if n.find('Bouquet') >= 0:
        n = n.replace('Bouquet', 'Bqt')

    if n.find('Sunflower') >= 0:
        n = n.replace('Sunflower', 'Snflwr')

    if n.find('Schematic') >= 0:
        n = n.replace('Schematic', 'Scmtc')

    if n.find('Balloon') >= 0:
        n = n.replace('Balloon', 'Baln')

    if n.find('Impossible') >= 0:
        n = n.replace('Impossible', 'Impsbl')

    if n.find('Hummingbird') >= 0:
        n = n.replace('Hummingbird', 'Hmgbrd')

    if n.find('Snowflake') >= 0:
        n = n.replace('Snowflake', 'Snflk')

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

    if n.find('Gingerbread') >= 0:
        n = n.replace('Gingerbread', 'Gngbrd')

    if n.find('Songbird') >= 0:
        n = n.replace('Songbird', 'Sngbrd')

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
            'Homespun Merry Christmas',
            'Autumn Leaves and Pumpkins with Please',
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
