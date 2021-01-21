# 523.1 Clase
# Clase -  aplicatie stoc marfa
# PF - 12/10/2017

'''
Rescrieti aplicatia de la Exercitiul 521 astfel:
    In loc de trei dictionare folositi doar un dictionar, care la valori va avea
    informatiile fiecarei tranzactii astfel
        Ex:  ds = {1: {'20170101', 100, 0}, 2: {'20170103', 0, 29} }
                      {data, intrare, iesire}
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

    lista_produse = []
    dictionar_categorii = {}

    def __init__(self, denp, categ, um = 'Buc', sold = 0):
        self.denp = denp
        self.categ = categ
        self.um = um
        self.sold =sold
        self.miscari = {}
        self.lista_produse = Stoc.lista_produse
        self.dictionar_categorii = Stoc.dictionar_categorii
        self.lista_produse.append(self.denp)
        if self.categ in self.dictionar_categorii.keys():
            self.dictionar_categorii[self.categ] += [self.denp]
        else:
            self.dictionar_categorii[self.categ] = [self.denp]

    def intrari(self, cant, data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) ) ):
        self.cant = cant
        self.date = data
        if self.miscari.keys():
            cheie = max(self.miscari.keys())  + 1
        else:
            cheie = 1
        self.miscari[cheie] = (self.date, self.cant, 0)
        self.sold += self.cant

    def iesiri(self, cant, data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) ) ):
        self.cant = cant
        self.date = data
        if self.miscari.keys():
            cheie = max(self.miscari.keys())  + 1
        else:
            cheie = 1
        self.miscari[cheie] = (self.date, 0, self.cant)
        self.sold -= self.cant

    def fisap(self):
        print('*-* ' * 8)
        print('Fisa produsului {0}, {1}'.format(self.denp, self.um))
        print('-' * 30)
        print(' Nrc ', '  Data  ', ' Intrare', ' Iesire')
        print('-' * 30)
        for cheie in self.miscari:
            print(str(cheie).rjust(3),
                  str(self.miscari[cheie][0]).rjust(10),
                  str(self.miscari[cheie][1]).rjust(8),
                  str(self.miscari[cheie][2]).rjust(6))
        print('-' * 30)
        print('Stocul final \t\t\t {0}'.format(self.sold))
        print('*-* ' * 8)

alune = Stoc('Alune', 'Fructe', 'kg')
caise = Stoc('Caise', 'Fructe', 'kg')

alune.dictionar_categorii
caise.lista_produse

alune.iesiri(100, '20170101')
alune.intrari(250, '20161230')
alune.intrari(180)
alune.iesiri(89)

alune.fisap()

alune.miscari
