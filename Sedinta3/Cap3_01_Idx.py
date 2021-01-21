# 301 Indexarea sirurilor
# Indexare
# PF - 06/10/2017 v3


# Concatenare + indexare
sir = 'Tele' + 'cinemateca'             # concatenare stringuri
print(sir)
lit = sir[4]
print(lit)
x = 7
y = sir[x + 3]                          # index calculat cu o expresie
print(y)

# Bucla while intr-un sir - returneaza index - litera
index = 0                               # initializare variabila
while index < len(sir):
    litera = sir[index]                    # parsare
    print(index, '-', litera)
    index += 1                          # incrementare

# Bucla for intr-un sir - returneaza index - litera
index = 0
for i in sir:
    print(index, '-', i)
    index += 1

# Numararea aparitiilor unei litere
count = 0
for i in sir:
    if i == 'e':
        count += 1
print(count)


# Numara vocalele si ponderea in total
voc = 0
tot = 0
for i in sir:
    tot += 1
    if i in ('a', 'e', 'i', 'o', 'u'):
        voc += 1
print('Sunt', voc, 'vocale si', tot - voc, 'consoane.\
	Vocalele reprezinta: {0}'.format(voc / tot * 100), '%')

# Slicing
print(sir[0:4])  # incepe de la primul caracter, termina la al doilea argument fara sa-l includa

print(sir[4:8])  # incepe cu primul argument, termina la al doilea fara sa-l includa

print(sir[4:20])  # daca al doilea numar e mai mare decat len(string) se opreste la sfarsitul stringului

print(sir[:4])  # returneaza primele caractere fara sa includa argumentul final

print(sir[12:])  # returneaza toate caracterele incepand cu argumentul dinaintea ':'

print(sir[:])  # returneaza tot stringul

copy_sir = sir[:]  # facem o copie a stringului intr-o alta variabila

print(copy_sir)

print(sir is copy_sir)

# Inversam ordinea literelor intr-un sir
sir = input('Introduceti un sir: ')
sir_invers = ''
print('Sirul tau este', sir)

for var in sir:
    sir_invers = var + sir_invers

print(sir_invers)
print('Sirul tau se scrie invers: ', sir_invers)

input('Apasa <enter> pt a iesi.')



