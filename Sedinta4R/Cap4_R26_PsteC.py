# 426
# Exercitii IF -Pastele Catolic
# PF 160720

# ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#
# Creati un program care sa returneze ziua in care are (a avut) loc sarbatoarea Pastelui Catolic intre 1900 -2099    #
# a = year%19, b = year%4, c = year%7, d = (19a + 24)%30, e = (2b + 4c + 6d + 5)%7                                   #
# data Pastelui este 22 Martie + d + e. Atentie, in anii 1954,1981, 2049, 2076 este cu o saptamana mai devreme       #
# ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#

def PasteC(year):
    if year in range(1900, 2100):
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        data = 22 + d + e
        luna = 'Martie'
        if year in (1954, 1981, 2049, 2076):
            data = data - 7
        if data > 61:
            data = data - 61
            luna = 'May'
        elif data > 31:
            data = data - 31
            luna = 'Aprilie'
        print('Pastele este in data de', data, luna + '.')
    else:
        print('Anul nu este in intervalul dorit.')


PasteC(2011)

input('Apasa <enter> pentru a iesi.')
