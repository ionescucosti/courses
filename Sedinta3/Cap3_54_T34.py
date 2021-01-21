# Sedinta 3
# Tema 34
# Student data

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

'''
Se dau tuplurile de mai sus. Se cere:
- o baza de date cu dictionare si/sau liste cu toate datele
- lista cu numele si prenumele tuturor medicilor;
- lista cu medicii care au specialitatea pediatrie (toate datele)
- lista cu medicii care au specialitatile neurologie si psihiatrie 
    (nume, prenume, tip)?
- lista cu  medicii primari (nume si prenume)
- ce specialitate au medicii cu prenumele 'Mitrut' sau numele 'Cruceru'
    (nume, prenume, tip, specialitate)
'''

bd = {}
for x in range(1, 16):
    bd[x]=globals()['t{:d}'.format(x)]
    #print(bd[x])

numeprenume = []
for i in bd.values():
    numeprenume.append([i[0],i[1]])
    print('Nume: ',i[0],', Prenume: ',i[1])

pediatrie=[]
for i in bd.values():
    if str(i[3])=='pediatrie':
        pediatrie.append([i])
        print('Nume: ',i[0],', Prenume: ',i[1], ', Tip: ',i[2],' Speacialitate: ', i[3])

neurologiesipsihiatrie=[]
for i in bd.values():
    if str(i[3])=='neurologie' or str(i[3])=='psihiatrie':
        neurologiesipsihiatrie.append([i])
        print('Nume: ',i[0],', Prenume: ',i[1], ', Tip: ',i[2])

primari=[]
for i in bd.values():
    if str(i[2])=='primar':
        primari.append([i])
        print('Nume: ',i[0],', Prenume: ',i[1])

MitrutCruceru=[]
for i in bd.values():
    if str(i[1])=='Mitrut' or str(i[0])=='Cruceru':
        MitrutCruceru.append([i])
        print('Nume: ',i[0],', Prenume: ',i[1], ', Tip: ',i[2],' Speacialitate: ', i[3])