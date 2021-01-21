# 421
# Valoare viitoare
# PF 160716

#-------------------------------------------------------------------------------------------------------#
#  Scrie o functie care sa primeasca parametri de intrare suma unica investita, rata de dobanda fixa si #
#   numarul de ani si sa returneze valoarea viitoare a investitiei. Apeleaz-o suma*(1+i)**ani                          #
#-------------------------------------------------------------------------------------------------------#

def suma(x, d, a):
    return x * d * a

print(suma(100, 2.5, 10))

input ( 'Apasa <enter> pentru a iesi.' )
