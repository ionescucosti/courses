# 505 Clase
# Clase
# PF - 27/05/2016

# 01 putem crea o clasa fara continut in blocul de instructiuni (empty):
#----------------------------------------------------------------------#

class ClasaMea:         # denumire preferabil cu litera mare
    pass

obiect1 = ClasaMea()  	# obiect, instantiere
obiect2 = ClasaMea()
print(obiect1)
obiect2  				# returneaza adresa obiectului in memorie


# 02  Atribute:
#------------#

class MyList:
    """Clasa creaza o lista cu categ de animale si numarul maxim pentru fiecare categ"""

    def __init__(self, max):        # la crearea oricarei instante (categorie) va trebui sa specificam
        self.max_elem = max         # numarul maxim de animale ale acesteia.
        self.animale = []           # De asemenea, se va initializa lista cu animalele instantei

    def adauga(self, elem):         # metoda de adaugare animal intr-o categorie (instanta)
        self.animale.append(elem)
        if len(self.animale) > self.max_elem:
            self.animale.pop(0)     # daca numarul este depasit il va sterge pe primul din lista

    def listeaza(self):             # metoda pentru listarea animalelor dintr-o categorie (instanta)
        return self.animale

domestice = MyList(4)               # cream instante
salbatice = MyList(2)

domestice.adauga("Caine")           # utilizam metoda adauga
domestice.adauga("Pisica")
domestice.adauga("Cal")
domestice.adauga("Oaie")

print(domestice.listeaza())

domestice.adauga("Capra")

salbatice.adauga("Tigru")
salbatice.adauga("Ghepard")
salbatice.adauga("Leu")
salbatice.adauga("Linx")

print(domestice.listeaza())            # listam utilizand metoda listeaza
print(salbatice.listeaza())

domestice.animale.append('caine')    # atentie, putem utiliza si metode specifice altor tipuri utilizate (lista)
domestice.adauga('Vaca')

# 03 Clasa persoana - metode speciale
#------------------------------------#

class Persoane:
    """Persoane, nume si varsta. Metoda de returnare a acestor informatii"""  # Doc string

    def __init__(self, name, age):      # metoda construtor, metoda privata
        self.name = name             # este apelata automat la crearea unei instante
        self.age = age            # ofera posibilitatea initializarii unor atribute la  crearea instantei

    def __str__(self):                  # metoda speciala pentru printarea starii obiectului
        """Afiseaza starea obiectului"""
        return "Persoana: ({0}, {1})".format(self.name, self.age)

    def __del__(self):                  # metoda de stergere a instantei
        print('Stergerea a fost efectuata.')

George = Persoane("George", 32)

print(George)             # print apeleaza automat metoda __str__, nu se apeleeaza ca metodele obisnuite

del George                # metoda __del__ se apeleza diferit de metodele obisnuite


# 04 Clasa cu parametri default
#-----------------------------#

class Test:
    """Clasa cu parametri default"""

    def __init__(self, a=10, b=20):
        if type(a) == int and type(b) == int:
            print(a + b)
        else:
            print('Parametrii incorecti')


Ob1 = Test()            # la creare va prelua parametrii default

Ob2 = Test(5, 7)        # putem sa dam alti parametri

Ob3 = Test(b = 50)

print(Ob1)

dir(Ob1)

Ob1.__dict__

# 05 Clasa cu variabila statica
#-----------------------------#

class test:
    '''doc'''
    x = 10                              # Putem crea o clasa cu variabile statice (detalii cap urmator)
    l = []                              # Acestea pot fi tipurile invatate
    d = {}                              # Sunt accesibile fiecarei instante si clasei

    def __init__(self, nume):           # La instantiere va trebui sa introducem parametrul nume
        self.nume = nume
        self.x = test.x                 # Pentru a atribui instantelor variabilele de clasa
        self.d = test.d                 # setam in acest mod self.variabila = NumeClasa.variabila
        self.l = test.l
        if self.d.keys():                       # o modalitate de populare lista si dictionar cu
            cheie = max(self.d.keys()) + 1      # numele introduse pentru fiecare instanta
            print(cheie)
        else:
            cheie = 1
            print('else')
        self.l.append(self.nume)
        self.d[cheie] = self.nume


obj_1 = test('Vasile')
obj_2 = test('George')
obj_3 = test('Camelia')

test.l
obj_1.d
obj_2.l

test.x

obj_1.x = 100

obj_1.x
test.x =25
obj_2.x

obj_4 = test('Corina')
obj_4.x


class test2:
    y = 20

    def __init__(self):
        self.y = test2.y

    def __str__(self):
        return str(self.y)

obj_5 = test2

obj_5.y

print(obj_5.y)