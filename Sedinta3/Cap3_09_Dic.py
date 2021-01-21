# 309 Dictionare
# Dictionare
# PF - 27/05/2016

# Metode de creare a dictionarelor:

# 1. direct, prin elemente de tip cheie:valoare

d1 = {1: 'lu', 2: 'ma', 3: 'mi', 4: 'jo', 5: 'vi', 6: 'sa', 7: 'du'}

# 2. Prin dict() plus elemente de tip cheie = valoare:

d2 = dict(lu=1, ma=2, mi=3, jo=4, vi=5, sa=6, du=7)

# 3. Utilizand functia zip() si dict(), din doua liste cuprinzand cheile si valorile:

d3 = dict(zip([1, 2, 3, 4, 5, 6, 7],
              ['lu', 'ma', 'mi', 'jo', 'vi', 'sa', 'du']))

# 4. Utilizand tupluri cu cheile si valorile:

d4 = dict([(2, 'ma'), (1, 'lu'), (3, 'mi'), (4, 'jo'), (5, 'vi'), (6, 'sa'), (7, 'du')])

# 5. Utilizand dict() si elemente de tip cheie: valoare:

d5 = dict({1: 'lu', 2: 'ma', 3: 'mi', 4: 'jo', 5: 'vi', 6: 'sa', 7: 'du'})

if d1 == d3 == d4 == d5:
    print('\nAdevarat')
else:
    print('\nFals')

# 6. Putem utiliza si asa numita comprehensions method:
d6 = {x: x ** 3 for x in (1, 2, 3, 4)}
print(d6)

# Cum putem initializa un dictionar (gol):

d_100 = dict()
d_200 = {}

# Metode si functii aplicabile
dict1 = {1: 'Cal', 2: 'Caine', 3: 'Vaca', 4: 'Pisica'}
print(dict1)

dir(dict1)
dict1[5] = 'Oaie'  # Adauga noi elemente in dictionar
dict1[7] = 'Iepure'
print(dict1)

dict1.get(6, 'Nu exista elementul cu cheia')  # Returneaza valoarea corespunzatoare cheii primite sau a celei default

dict2 = dict1.copy()  # Creeaza o copie a dictionarului
print(dict2)

dict2.clear()  # Sterge toate elementele dictionarului
print(dict2)

dict1.update({11: 'Magar', 12: 'Capra', 7: 'Maimuta'})

print(dict1.items())  # Returneaza o lista cu tupluri cheie-valoare
dict1.keys()  # Returneaza o lista cu cheile
dict1.values()  # Returneaza o lista cu valorile

dict1.pop(1)  # Sterge elementul cu cheia respectiva si returneaza valoarea
print(dict1)

del dict1[5]  # Sterge elementul corespunzator cheii primite ca argument
print(dict1)

# Numaram elementele care apar intr-o lista sau intr-un text
s = '641761975865896158965813057980571249284932478346173124783289461' \
    '238789376183613766516754798765984764678464598783231437123197159475827159'
lista = []  # initializam lista (lista = list() face acelasi lucru)
lista.extend(s)  # extend va introduce fiecare cifra din sir ca element al listei
counts = {}  # initializare dictionar (counts = dict() face acelasi lucru)
print(type(counts))

for nr in lista:
    nr = int(nr)  # fiecare numar il transformam in intreg
    if nr not in counts:
        counts[nr] = 1  # daca nu e inca in dictionar il adaugam
    else:
        counts[nr] = counts[nr] + 1  # daca exista incrementam valoarea (mutabilitate)
print(counts)

# Metoda get + default versus if - exemplu
nr = 7
if nr in counts:  # vrem sa cautam daca exista cheia 7 si sa returnam valoarea, fara get
    x = counts[nr]
    print(x)
else:
    x = 0
    print(x)

print(counts.get(nr, 0))  # acelasi lucru, cu get (default 0, daca nu gaseste cheia nr)

# Split intr-un text si numaram elementele

counts = {}
text = 'Este ora zece si ne tine asta pana la ora unsprezece'
cuv = text.split()

print('Lista cuvinte:', cuv)

for item in cuv:
    counts[item] = counts.get(item, 0) + 1  # folosim get sa caute daca exista val. si o incrementeaza
print('Dictionar numar aparitii cuvinte:', counts)

# Elementele unui dictionar nu se pot sorta
dict3 = {'alfa': 10, 'beta': 20, 'gama': 30}
for key in dict3:
    print(key, dict3[key])
print(dict3.keys())
print(dict3.values())
print(dict3.items())

# Bucla cu doua variabile intr-un dictionar
dict3 = {'alfa': 10, 'beta': 20, 'gama': 30}
lista = []


for k, v in dict3.items():
    lista.append([k, v])

lista.sort()
print(lista)

# Construim un dictionar, pornind de la o lista, cu ajutorul functiei enumerate():

Unit_adm = dict()
for k, v in enumerate(['Municipiu', 'Oras', 'Comuna', 'Sat']):
    print(k + 1, v)
    Unit_adm[k + 1] = v
print(Unit_adm)

input('Apasa <enter> pentru a iesi.')
