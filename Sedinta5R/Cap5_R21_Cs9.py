# 571 Clase
# Clase
# PF - 10/08/2016

'''
Importati functia datetime din modulul datetime. Instructiune scrisa deja (vezi mai jos)

Creati o clasa 'Stoc' care va avea:
  - o metoda constructor cu
        denumire produs
        categoria
        unitatea de masura default 'Buc'
        sold default 0
        initializati trei dictionare, cu cheie comuna (numerica), pentru data op.,
    intrari si iesiri din stoc, care vor fi atribuite fiecarei instante

  - o metoda intrari cu
        cantitatea,
        data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )
        testati daca exista chei in dictionarul cu data op. Daca exista stabileste cheia curenta
    ca fiind maximul cheilor existente plus 1, altfel va fi egala cu 1
        introduce in dict intrari cheie si cant
        introduce in dict data cheie si data op
        actualizeaza soldul

  - o metoda iesiri, similara cu precedenta. Diferente: populam dict iesiri

  - o metoda fisa produsului cu urmatoarele specificatii:
        Sa printeze 'Fisa produsului "denumire_produs"' (sa stim si noi a cui e fisa)
        Sa printeze ' Nrc ', '  Data  ', ' Intrare', ' Iesire' pentru toate tranzactiile produsului
        Sa printeze stocul actual al produsului
        pentru avansati - aliniati coloanele

Creati trei instante (produse). Pentru 2 din ele efectuati cate 4-5 operatiuni (intrari, iesiri)

Apelati metoda fisa produsului pentru cele 2 produse
''' #

from datetime import datetime

class Stoc:
    """Tine stocul unui depozit"""

    def __init__(self, prod, categ, um='Buc', sold=0):
        self.prod = prod			# parametri cu valori default ii lasam la sfarsitul listei
        self.categ = categ  		# fiecare instanta va fi creata obligatoriu cu primii trei param.
        self.sold = sold			# al patrulea e optional, soldul va fi zero
        self.um = um
        self.i = {}					# fiecare instanta va avea trei dictionare intrari, iesiri, data
        self.e = {}					# pentru mentinerea corelatiilor cheia operatiunii va fi unica
        self.d = {}

    def intr(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.data = data
        self.cant = cant
        self.sold += self.cant          # recalculam soldul dupa fiecare tranzactie
        if self.d.keys():               # dictionarul data are toate cheile (fiecare tranzactie are data)
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.i[cheie] = self.cant       # introducem valorile in dictionarele de intrari si data
        self.d[cheie] = self.data

    def iesi(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        #   datetime.strftime(datetime.now(), '%Y%m%d') in Python 3.5
        self.data = data
        self.cant = cant
        self.sold -= self.cant
        if self.d.keys():
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.e[cheie] = self.cant       # similar, introducem datele in dictionarele iesiri si data
        self.d[cheie] = self.data

    def fisap(self):

        print('Fisa produsului ' + self.prod + ': ' + self.um)
        print(40 * '-')
        print(' Nrc ', '  Data ', 'Intrari', 'Iesiri')
        print(40 * '-')
        for v in self.d.keys():
            if v in self.i.keys():
                print(str(v).rjust(5), self.d[v], str(self.i[v]).rjust(6), str(0).rjust(6))
            else:
                print(str(v).rjust(5), self.d[v], str(0).rjust(6), str(self.e[v]).rjust(6))
        print(40 * '-')
        print('Stoc actual:      ' + str(self.sold).rjust(10))
        print(40 * '-' + '\n')


fragute = Stoc('fragute', 'fructe', 'kg')       # cream instantele clasei
lapte = Stoc('lapte', 'lactate', 'litru')
ceasuri = Stoc('ceasuri', 'ceasuri')

fragute.sold                    # ATRIBUTE
fragute.prod
fragute.intr(100)
fragute.iesi(73)
fragute.intr(100)
fragute.iesi(85)
fragute.intr(100)
fragute.iesi(101)

fragute.d                       # dictinareele produsului cu informatii specializate
fragute.i
fragute.e

fragute.sold
fragute.categ
fragute.prod
fragute.um

fragute.fisap()

lapte.intr(1500)
lapte.iesi(975)
lapte.intr(1200)
lapte.iesi(1490)
lapte.intr(1000)
lapte.iesi(1200)

lapte.fisap()

l = [fragute, lapte, ceasuri]

for i in l:
    i.fisap()