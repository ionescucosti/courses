# 204 While
# Utilizarea buclei while
# PF - 06/10/2017 v3


# Exemplu while
x = 100
while x > 0:
    print(x, end = ';')
    x -= 15     # decrementam valoarea lui x, ca sa asiguram iesirea din bucla.
                # Daca omitem aceasta instructiune bucla devine infinita

# Conversie repetata lei in lire sterline (apelare succesiva pana la conditia de iesire din bucla).

curs = float(input('Introduceti cursul lei/GBP: '))

while True:
    lei = input('Introduceti suma: ')
    if lei.isdigit():
        lei = int(lei)
        print('Schimb efectuat. Ridicati suma de %.2f' % (lei / curs), 'GBP')
        continue
    else:
        print('Introduceti suma in format numar intreg!')

    terminat = input('Apasa "DONE" pt a termina, orice pentru a repeta conversia.')
    if terminat.upper() == 'DONE':
        break
print('Va multumim!')
