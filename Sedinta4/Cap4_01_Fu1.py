# 401 Functii
# Functii
# PF - 27/05/2016

# O functie fara bloc de instructiuni
def nimic():
    pass

nimic()

# Numele functiei


		# ...si nu le veti mai putea utiliza pana la restart
def len():  		    # nu folositi nume de functii builtin. Operatiunea va putea modifica acele functii
    print(100)
# Atentie la rescriere unei functii cu acelasi nume

def aria(a, b):
    """Calculeaza aria dreptunghiului"""  		# Doc stringul se identeaza fata de prima linie
    return a * b  					# la fel si blocul de instructiuni

print(aria(7, 5.2))

def aria(raza):  								# rescriem functia
    """Calculeaza aria cercului"""
    return 3.14159 * raza ** 2

print(aria(7, 5.2))  							# daca incercam s-o apelam asa cum o stiam
print(aria(5))  								# apelarea actuala

aria.__doc__

# NU dati un nume identic cu al unei variabile globale

var_glob = 50

def var_glob():
    print('Daca schimbam valoarea variabilei globale cu acelasi nume functia nu va mai fi rulata')

var_glob()  							# e OK, functia este executata
var_glob = 100  						# schimbam valoarea variabilei
var_glob()  							# NU mai functioneaza dupa ce am modificat valoarea variabilei

# Parametrii functiei

def test():  # Functie fara parametri
    print('Test')

test()

def test_parametri(nume, varsta):
    if type(nume) is str and type(int(varsta)) is int:
        print(nume, 'are', varsta, 'ani!')
    else:
        print('Parametrii incorecti!')

test_parametri('Maria', 34)  		# apelare corecta a functiei
test_parametri(34, 'Maria')  		# parametrii inversati, tipuri de date diferite
test_parametri('Maria')  			# numar incorect de parametrii


# Fara return

def aduna(p1, p2):
    print(p1 + p2)

x = aduna(5, 7)  		# nu stocheaza rezultatul intors de functie. Nu este o atribuire de valoare
x += 100  # testare

# Cu return. Return poate fi urmat de o expresie. Rezultatul va fi printat automat
# fara sa mai fie nevoie de o variabila suplimentara

def aduna(p1, p2):
    return p1 + p2

x = aduna(5, 7)
x += 100
print(x)

# Atentie la o functie care are print in rezultat

def salut(nume):
    print('Hello', nume)

print(salut('Vasile'))  			# Apelare cu print rezultat denaturat
salut('Ioana')  					# Apelare doar cu nume functie rezultat corect

# Parametri pozitionali	-  daca gresim ordinea sau tipul de date -> eroare

listaa = {}  # dict cu data angajarii
listav = {}  # dict cu varsta

def salariat(nume, varsta, an_ang):
    """Populeaza doua dictionare cu datele angajatilor, nume-varsta, nume-anul angajarii"""
    try:
        if type(nume) is str:        # daca nume nu e string --> except. Daca e strig cu numere--> else
            if 18 <= varsta <= 100:                 # varsta in afara intervalului --> mesaj
                if an_ang in range(1950, 2018):     # daca anul ang nu e in interval --> mesaj
                    listaa[nume] = an_ang
                    listav[nume] = varsta
                else:
                    print('Anul angajarii incorect!')
            else:
                print('Varsta incorecta!')
        else:
            print('Nume incorect!')
    except TypeError as e:
        print(e)
        print('Nume .... incorect!')

salariat('Paul', 25, 2001)                  # corect
salariat('George', 21, 2011)                # corect
salariat('22', 'Marin', 2011)               # parametri inversati, nume incorect
salariat(22, 'Marin', 2011)                 # nume incorect
salariat('Marin', 2011, 22)                 # parametri inversati, varsta incorecta

print(listaa)
print(listav)

# parametrii cu valori standard

personal = dict()

def angajat(nume='Georgel', anul_ang=2017):
    """Completeaza datele angajatilor in 'personal' """
    personal[nume] = anul_ang

angajat('Mitica', 2001)
angajat('Corina')
angajat()
angajat(2005)                           # numele va fi considera ca fiind 2005, anul default 2017
angajat(nume='Micsunica', anul_ang=2009)
angajat(anul_ang=2011)                  # Numele va fi default 'Nume'
angajat(nume='Ion')                   # anul va fi cel default 2017
angajat(anul_ang=2002, nume='Constanta')    # nu conteaza ordinea, daca atribuim valori tururor p v s
print(personal)

# Incapsulare / return

def calculeaza(a, b, c):
    d = (a + b) * c         # d este variabila locala, nu este vizibila in afara functiei
    return d                # la fel si parametrii a, b, c

calculeaza(1, 2, 3)
print(d)                    # NU sunt vizibili in afara functiei
print(a, b, c)

# Variabila globala / variabila locala

x = 10  # variabila globala

def test(numar):
    if numar < 25:
        x = 25  # variabila locala
        return x

print(test(x))  # functia apeleaza var globala si transmite rezultatul variabilei locale cu acelasi nume
print(x)        # variabila globala nu-si modifica valoarea

# Variabila globala - modificare
def test_global(numar):
    global x  # declaram variabila globala x
    # print(x)
    x = numar + 1
    return x

test_global(30)

print(x)

# alt exemplu

glo = 100  # definim o var globala

def test_glo():  # scriem o functie care foloseste variabila globala
    print(glo)

test_glo()

def test_loc():     # scriem o functie care foloseste o var locala cu nume identic cu al celei globale
    glo = 5         # variabila locala are prioritate fata de cea globala, daca n-a fost definita global
    print(glo)


test_loc()

print(glo)          # valoarea var globale ramane neschimbata

input('Apasa <enter> pentru a iesi.')


def numere(*argv):
    maxi = argv[0]
    mini = argv[0]
    for var in argv:
        if var > maxi:
            maxi = var

        if var < mini:
            mini = var
    return maxi, mini
listan = [15, 35, 78, 9, 658]

numere(*listan)
