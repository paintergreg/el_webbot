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

    if n.find('(Applique)') >= 0:
        n = n.replace('(Applique)', '(App)')

    if n.find('(Vinyl Applique)') >= 0:
        n = n.replace('(Vinyl Applique)', '(VA)')

    if n.find('Christmas') >= 0:
        n = n.replace('Christmas', 'Xmas')

    if n.find('(Whitework)') >= 0:
        n = n.replace('(Whitework)', '(WW)')

    if n.find('(Vintage)') >= 0:
        n = n.replace('(Vintage)', '(V)')

    if n.find(' and ') >= 0:
        n = n.replace(' and ', ' & ')

    if n.find('(Crafty Cut)') >= 0:
        n = n.replace('(Crafty Cut)', '(CC)')

    if n.find('(Organza)') >= 0:
        n = n.replace('(Organza)', '(O)')

    if n.find('(Puff Foam)') >= 0:
        n = n.replace('(Puff Foam)', '(PF)')

    if n.find('(Thick Thread)') >= 0:
        n = n.replace('(Thick Thread)', '(TT)')

    if n.find('(Cardstock)') >= 0:
        n = n.replace('(Cardstock)', '(CS)')

    if n.find('(Redwork)') >= 0:
        n = n.replace('(Redwork)', '(RW)')

    if n.find('(Embossed)') >= 0:
        n = n.replace('(Embossed)', '(EM)')

    if n.find('(Double Run)') >= 0:
        n = n.replace('(Double Run)', '(DR)')

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
            'No changes'
            ]
    for i in names:
        print(modify_product_name(i))
