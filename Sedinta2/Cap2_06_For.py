# 206 for & while / else
# Utilizarea buclelor cu else
# PF - 06/10/2017 v3

# for cu else - blocul de sub else va fi executat dupa finalul buclei

for i in range(1, 5):
    print([i, i ** 2, i ** 3, i ** 4])
else:
    print('!... si ELSE')

# for cu else - blocul de sub else NU va fi executat daca bucla nu ajunge la final

for i in range(1, 5):
    if i == 3:
        break
    print([i, i ** 2, i ** 3, i ** 4])
else:
    print('!... si ELSE')

# for cu else - blocul de sub else va fi sau nu executat in functie de situatie

n = 5

for i in range(1, n+1):
    print([i, i ** 2, i ** 3, i ** 4])
    if i % 7 == 0:
        print('Divizibil cu 7')
        break
else:
    print('Nu e divizibil cu 7')

# for cu else - blocul de sub else va fi executat chiar daca bucla nu ruleaza niciodata

for i in '':
    print(i)
else:
    print('!... si ELSE')

# while cu else - blocul de sub else va fi executat chiar daca bucla nu ruleaza niciodata

while False:
    print('Nimic')
else:
    print('AltCeva')

# while cu else - blocul de sub else NU va fi executat daca bucla nu ajunge la final

while True:
    print('Corect')
    if True:
        break
else:
    print('AltCeva')

input('\n\nApasa <enter> pt a iesi.')
