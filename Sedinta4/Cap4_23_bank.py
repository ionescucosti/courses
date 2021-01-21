# 423
# Formatarea stringurilor
# PF 160719

# ------------------------------------------------------------------------------------------#
# Creati o aplicatie bancara, pentru incasari in contul clientilor						    #
# clientii n-ar fi incantati sa primeasca/plateasca o suma aproximativa generata de float,  #
# asa ca banca tine evidenta conturilor in subunitati monetare (bani -> 1 leu = 100 bani)   #
# asta inseamna ca putem utiliza numere intregi in tranzactii, iar cand dorim sa afisam     #
# impartim rezultatul suma / 100 					                                        #
# ------------------------------------------------------------------------------------------#

cont = 0

def incaseaza(n):
    global cont
    cont += n
    print('Suma depusa: ',n,'\nSold: ', cont,'\n')

def plateste(n):
    global cont
    cont -= n
    print('Suma retrasa: ',n,'\nSold: ', cont,'\n')

incaseaza(100)
plateste(5)


