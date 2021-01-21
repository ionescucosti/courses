# 571 Clase
# Clase
# PF - v 21/09/2017

'''
Rescrieti aplicatia de la Exercitiul 521 astfel:
    In loc de trei dictionare folositi doar un dictionar, care la valori va avea
    informatiile fiecarei tranzactii astfel
        Ex:  ds = {1: {'d':'20170101', 'i':100, 'e' : 0}, 2: {'20170103', 0, 29} }

  - o metoda intrari cu
        - cantitatea,
        - data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )
        - testati daca exista chei in dictionarul cu data op. Daca exista stabileste cheia curenta
        ca fiind maximul cheilor existente plus 1, altfel va fi egala cu 1
        - introduce in dict datele operatiunii (va introduce zero la iesiri)
        - actualizeaza soldul

  - o metoda iesiri, similara cu precedenta. Diferente: (va introduce zero la intrari)

  - o metoda fisa produsului cu urmatoarele specificatii:
        - Sa printeze 'Fisa produsului "denumire_produs"' (sa stim si noi a cui e fisa)
        - Sa printeze ' Nrc ', '  Data  ', ' Intrare', ' Iesire' pentru toate tranzactiile produsului
        - Sa printeze stocul actual al produsului
        - pentru avansati - aliniati coloanele

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
        self.sd = {}                # dictionar cu cheie numerica, valoare tip dictionar

    def intr(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.data = data
        self.cant = cant
        self.sold += self.cant          # recalculam soldul dupa fiecare tranzactie
        if self.sd.keys():               # dictionarul data are toate cheile (fiecare tranzactie are data)
            cheie = max(self.sd.keys()) + 1
        else:
            cheie = 1

        self.sd[cheie] = {'d': self.data, 'i': self.cant, 'e' : 0}
        # self.sd[cheie] = [self.data, self.cant, 0] daca verem lista in loc de dictonar

    def iesi(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.data = data
        self.cant = cant
        self.sold -= self.cant
        if self.sd.keys():
            cheie = max(self.sd.keys()) + 1
        else:
            cheie = 1

        self.sd[cheie] = {'d': self.data, 'i': 0, 'e': self.cant}

    def fisap(self):
        print('*-*' * 10)
        print('Fisa produsului {0} ({1})'.format(self.prod, self.um))
        print('*-*' * 10)
        print(' Nrc ', '  Data ', 'Intrari', 'Iesiri')
        print('*-*' * 10)
        for k in self.sd.keys():
            print(str(k).rjust(5),
                  self.sd[k]['d'],
                  str(self.sd[k]['i']).rjust(6),
                  str(self.sd[k]['e']).rjust(6))
        print('*-*' * 10)
        print('Stoc actual:              {0}'.format(str(self.sold)))
        print('*-*' * 10 +'\n')


fragute = Stoc('fragute', 'fructe', 'kg')       # cream instantele clasei
lapte = Stoc('lapte', 'lactate', 'litri')
ceasuri = Stoc('ceasuri', 'ceasuri')

fragute.sold                    # ATRIBUTE
fragute.intr(100)
fragute.iesi(73)
fragute.intr(100)
fragute.iesi(85)
fragute.intr(100)
fragute.iesi(101)

fragute.sd            # dictionarele produsului cu informatii i/e

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

for i in l:         # fisele tuturor produselor
    i.fisap()