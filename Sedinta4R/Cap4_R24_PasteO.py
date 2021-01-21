# 424
# Exercitii IF - Pastele Ortodox
# PF 160720

# ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#
# Creati un program care sa returneze ziua sarbatoarii Pastelui Ortodox intre 1900 -2099             #
# Aplicand algoritmul lui Gauss pentru calculul datei Pastelui pentru anul N, avem urmatorii pasi:   #
# 1. a = N mod 19       2. b = N mod 4      3. c = N mod 7      4. d = (19 a + 15) mod 30            #                          #
# 5. e = (2 b + 4 c + 6 d + 6) mod 7        6. ziua = d + e + 4   (Aprilie)  . 						 #
# ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#

def PasteO(year):
    if year in range(1900, 2100):
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 15) % 30                  # aici difera de cel catolic 15 in loc de 24
        e = (2 * b + 4 * c + 6 * d + 6) % 7     # aici difera de cel catolic 6 in loc de 5
        ziua = 4 + d + e                        # aici difera de cel catolic 4 in loc de 22
        luna = 'Aprilie'
        if ziua > 30:
            ziua = ziua - 30
            luna = 'May'
        print('Pastele este in data de', ziua, luna + '.')
    else:
        print('Anul nu este in intervalul dorit.')

PasteO(2023)

input('Apasa <enter> pentru a iesi.')
