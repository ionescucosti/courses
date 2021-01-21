# 404 Lucrul cu fisiere
# Citire si scriere, extragere de informatii
# PF - 27/05/2016

# Deschiderea  fisierului. Citirea intregului text, toate liniile

text = open("guta.txt", "r")
x = text.read()  # citeste toate liniile intr-un sir de caractere
print(x)
text.close()

# Citeste doar caracterele dintr-o linie (readline)

text = open("c:/wt/guta.txt", "r")
print(text.readline())  # Prima linie
print(text.readline())  # A doua linie
print(text.readline())  # A treia linie

help(text)

# Citeste toate liniile si le adauga intr-o lista cate o linie pe element
text = open("c:\wt\guta.txt", "r")

linii = text.readlines()
print(linii)

# Bucla cu liniile unui text (Folosim lista de mai sus)

for linie in linii:
    linie = linie.rstrip()      # elimina liniile goale  ?!?!
    print(linie)
text.close()

count = 0
for linie in linii:
    linie = linie.rstrip()      # elimina spatiile goale  ?!?!
    count += 1
    if 'vorba' in linie:
        print(count)
        break

for linie in linii:
    if 'vorba' in linie.rstrip():
        print(linii.index(linie) + 1)       # linia
        print(linie.find('vorba'))              # caracterul
        print(linie.split().index('vorba')+1)       # cuvantul
#        break


# Cauta in text dupa pozitia caracterului, cu slicing, intr-un text
text = "Pretul zilei la pepeni este:    	1.2499"
pos = text.find(':')  # gaseste pozitia caracterului
pret = float(text[pos + 1:])  # returneaza ce este dupa caracterul gasit si-l transforma in numar
print(pret)

# Scrie intr-un fisiere nou creat
text = open("scrie.txt", "w")
text.write('Python si MySQL se inteleg de minune\nIn curand vom incerca \
    sa lucram cu\nbaze de date MySQL')
text.write('\nAstazi este o zi frumoasa')

text = open("scrie.txt", "r")
print(text.read())
text.close()

text = open("scrie.txt", "a+")
new_line = '\nInca o zi frumoasa!'
text.writelines(new_line)
text.write('Astazi este o zi mohorata!')

# Try / except - creaza un dictionar cu cuvintele din text si numarul de aparitii pentru fiecare

try:
    text = open('c:/wt/guta.txt')
except(IOError, FileNotFoundError) as e:
    print('Fisierul nu poate fi deschis:')
    print(e)

counts = dict()
for line in text:
    words = line.split()        # text linii split in cuvinte
    for word in words:
        if word not in counts:  # daca nu exista in dictionar il creaza
            counts[word] = 1
            print(counts[word], '-->', word)
        else:
            counts[word] += 1   # daca exista in dictionar aduna 1
            print(counts[word],'-->', word)
print(counts)

max(counts.values())

for k,v in counts.items():
    if v == 7:
        print (k)

#   Avem un fisier text care contine date despre medici. Extragem informatii si populam un dictionar
#   Datele vor fi in formatul [{'Nume': 'Popa', 'Prenume': 'Ion', 'Specialitate': 'orl', 'Tip': 'primar'},...]

fisier = open('medici.txt')
list = []   # initializam lista in care vom introduce dictionare cu seturi de valori pt fiecare medic
dict = {}   # initializam dictionarul care va introduce fiecare set de valori in lista

for line in fisier:
    line = line.rstrip()            # elimina spatiile dintre liniile returnate
    ls = line.split(',')            # creaza o lista cu cuvintele de pe o linie
    if ls[0] != 'Nume':             # nu vrem sa returneze si antetul din fisier
        dict['Nume'] = ls[0]
        dict['Prenume'] = ls[1]     # din aceasta lista populam un dictionar "temporar"
        dict['Tip'] = ls[2]
        dict['Specialitate'] = ls[3]
        list.append(dict)           # datele din dictionarul temporar sunt incarcate in lista
        dict = {}                   # dictionarul este reinitializat pentru urmatoarea iteratie (linie)

print(list)

# Avem o lista, care contine pentru fiecare medic un dictionar cu nume, prenume, tip si specialitate
# Putem extrage doar o parte din informatiile despre medici si sa le listam individual

medici = ['Nume', 'Prenume', 'Specialitate']  # stabilim ce informatii extragem din fiecare element al listei
for item in list:
    for key in medici:
        print(key, ': ', item[key])             # extragem informatia dorita
    print('Fullname:', item['Nume'] + ' ' + item['Prenume'] + '\n')

# Putem extrage doar informatiile care ne intereseza (ex: medici cu specialitatea cardiologie)

def med_spec(Spec):
    for item in list:
        if item['Specialitate'] == Spec:
            for key in medici:
                print(key, ': ', item[key])             # extragem informatia dorita
            print('*-------------------*-------------------*')

input('Apasa <enter> pentru a iesi.')


for elem in nume:
    if nume[0] == elem:
        pass
    else:
        print("""
        Nume : {0}
        Prenume : {1}
        Data nasterii: {2}
        """.format(elem.split()[0], elem.split()[1], elem.split()[2]))


