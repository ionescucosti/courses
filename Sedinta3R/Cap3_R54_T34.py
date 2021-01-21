# R Tema 4
# Numara caracterele dintr-un string
#  PF 02/03/2015

'''
Se dau tuplurile de mai sus. Se cere:
- o baza de date cu dictionare si/sau liste cu toate datele
- lista cu numele si prenumele tuturor medicilor;
- lista cu medicii care au specialitatea pediatrie (toate datele)
- lista cu medicii care au specialitatile neurologie si psihiatrie 
    (nume, prenume, tip)
- lista cu  medicii primari (nume si prenume)
- ce specialitate au medicii cu prenumele 'Mitrut' sau numele 'Cruceru'
    (nume, prenume, tip, specialitate)
''' #

from datetime import datetime

time_start = datetime.now()

t1 = ('Bunica','Mihai-Daniel','primar','reumatologie')
t2 = ('Donca','Cornelia-Ana','primar','chirurgie')
t3 = ('Achiriloaie','Lorand-Levente','specialist','neurologie')
t4 = ('Papuc','Raducu-Liviu','primar','homeopatie')
t5 = ('Cucuiu','Nutu','primar','ortopedie')
t6 = ('Buia','Tache','specialist','ginecologie')
t7 = ('Dragomanu','Mitrut','specialist','ecografie')
t8 = ('Ticu','Simona','specialist','psihiatrie')
t9 = ('Ene','Adrian-Stefan','specialist','pediatrie')
t10 = ('Copae','Toma','primar','neurologie')
t11 = ('Hotoi','Dragos Alin','specialist','pediatrie')
t12 = ('Ceafalau','Vincenţiu Mihail','primar','pediatrie')
t13 = ('Briceag','Anca Stefana','primar','imagistica')
t14 = ('Condrea','Nutu','primar','fizioterapie')
t15 = ('Cruceru','Ioana-Loredana','primar','dermatologie')


# o baza de date cuprinzand o lista cu toate datele - cu o bucla for
bd = [globals() ['t{:d}'.format(x)]      for x in range ( 1, 16 ) ]
print(bd)

# sau manual:
bd = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15]

# o baza de date cuprinzand un dictionar cu toate datele
dd = {'t{:d}'.format(x) : globals()['t{:d}'.format(x)]  for x in  range ( 1, 16 )}
print(dd)

# sau

dd = {cheie+1: valoare for cheie, valoare in enumerate(bd)}

# o lista cu fullname
nume_prenume = []
for i in range(1, 16):
    elem = (globals()['t{:d}'.format(i)])
    nume_prenume.append(elem[0]+ ' ' + elem[1])
print(nume_prenume)
#sau
nu_pre = [(globals()['t{:d}'.format(i)])[0] +
          ' ' +
          (globals()['t{:d}'.format(i)])[1]
          for i in range(1, 16) ]
print(nu_pre)
#sau
npre = []
for i in bd:
    npre.append(i[0] + ' ' + i[1])
print(npre)



# medici pediatrie
medici_pediatrie = []
for i in bd:
    if i[3] == 'pediatrie':
        medici_pediatrie.append(i)
print(medici_pediatrie)

#sau

lmp = []
mp = {}

for i in bd:
    if i[3] == 'pediatrie':
        for elem in i:
            mp[i.index(elem) + 1] = elem
        lmp.append(mp)
        mp = {}

# lista cu medicii care au specialitatile neurologie si psihiatrie
lmnp = []
mnp = {}

for i in bd:
    if i[3] == 'neurologie' or 'psihiatrie':
        for elem in i:
            mnp[i.index(elem) + 1] = elem
        mnp.pop(4)
        lmnp.append(mnp)
        mnp = {}
print(lmnp)

#lista cu  medicii primari (nume si prenume)
medici_primari = []
mpr = {}

for i in bd:
    mpr[i.index(i[0]) + 1] = i[0]
    mpr[i.index(i[1]) + 1] = i[1]
    medici_primari.append(mpr)
    mpr = {}
print(medici_primari)

#ce specialitate au medicii cu prenumele 'Mitrut' sau numele 'Cruceru'
ldiv = []
div = {}

for i in bd:
    if i[1] == 'Mitrut' or i[0] == 'Cruceru':
        for elem in i:
            div[i.index(elem) + 1] = elem
        ldiv.append(div)
        div = {}
print(ldiv)

time_end = datetime.now()

print('Durata rularii:', time_end - time_start)

input('\n\nApasa <enter> pt a iesi.')
