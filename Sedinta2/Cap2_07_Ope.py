# 207 Operatori
# Utilizarea operatorilor
# PF - 06/10/2017 v3

# Operatori de comparare

if 'Am un cos plin' >= 'Am un cos gol':     # comparatia efectiva la primul caracter diferit
    print('E mai bine sa fie plin')
else:
    print('E mai bine sa fie gol')


if 'mere' == 'pere':
    print('Premiul Nobel')
else:
    print('Mai fa cercetari')


if 'zece' <=  100:          # genereaza o eroare, nu putem compara tipuri diferite
    print('Chiar asa?')


# Operatori Boolean

if True:                # nu ajunge niciodata pe ramura else
    print('Soare')
else:
    print('Nor')

# sau

if 5:                   # nu ajunge niciodata pe ramura else
    print('Soare')
else:
    print('Nor')




input('\n\nApasa <enter> pt a iesi.')
