# 473
# Formatarea stringurilor
# PF 160719

# ------------------------------------------------------------------------------------------#
# Creati o aplicatie bancara, pentru incasari in contul clientilor						    #
# clientii n-ar fi incantati sa primeasca/plateasca o suma aproximativa generata de float,  #
# asa ca banca tine evidenta conturilor in subunitati monetare (bani -> 1 leu = 100 bani)   #
# asta inseamna ca putem utiliza numere intregi in tranzactii, iar cand dorim sa afisam     #
# impartim rezultatul suma / 100 					                                        #
# ------------------------------------------------------------------------------------------#

sold = 0

def bank():
    incaseaza = eval(input('Introduceti suma de incasat in bani - 1 leu = 100 bani: '))
    global sold
    sold += incaseaza
    print('Ati incasat {:.2f} lei'.format(incaseaza / 100))
    print('Soldul dv este de {:.2f}'.format(sold / 100))

bank()

input('Apasa <enter> pentru a iesi.')
