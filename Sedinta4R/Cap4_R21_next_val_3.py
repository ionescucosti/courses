# 471
# Valoare viitoare
# PF 160716

# -------------------------------------------------------------------------------------------------------#
#  Scrie o functie care sa primeasca parametri de intrare suma unica investita, rata de dobanda fixa si #
#   numarul de ani si sa returneze valoarea viitoare a investitiei. Apeleaz-o                           #
# -------------------------------------------------------------------------------------------------------#

def dobinvfixa(suma, dobanda, ani):
    """Calculeaza suma viitoare returnata de o investitie curenta in suma unica"""  #
    s = suma
    d = dobanda/100
    for i in range(ani):
        s = s * (1 + d)
    s = '{:.2f}'.format(s)
    return 'Valoarea peste ' + str(i + 1) + ' ani este de: ' + str(s)


print(dobinvfixa(10000, 0.10, 10))

#sau
def investitie(suma, ratad, ani):
    '''Calculeaza valoarea viitoare a investitiei'''
    return suma * ((1 + ratad/100)**ani)

input('Apasa <enter> pentru a iesi.')
