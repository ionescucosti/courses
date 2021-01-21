# 521 Clase
# Clase -  aplicatie stoc marfa
# PF - 10/08/2016

'''
Importati functia datetime din modulul datetime. Instructiune scrisa deja (vezi mai jos)

Creati o clasa 'Stoc' care va avea:
  - o metoda constructor cu
        - denumire produs
        - categoria
        - unitatea de masura default 'Buc'
        - sold default 0
        - initializati trei dictionare, cu cheie comuna (numerica), pentru data op.,
        intrari si iesiri din stoc, care vor fi atribuite fiecarei instante

  - o metoda intrari cu
        - cantitatea,
        - data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )
        - testati daca exista chei in dictionarul cu data op. Daca exista stabileste cheia curenta
        ca fiind maximul cheilor existente plus 1, altfel va fi egala cu 1
        - introduce in dict intrari cheie si cant
        - introduce in dict data cheie si data op
        - actualizeaza soldul

  - o metoda iesiri, similara cu precedenta. Diferente: populam dict iesiri

  - o metoda fisa produsului cu urmatoarele specificatii:
        - Sa printeze 'Fisa produsului "denumire_produs"' (sa stim si noi a cui e fisa)
        - Sa printeze ' Nrc ', '  Data  ', ' Intrare', ' Iesire' pentru toate tranzactiile produsului
        - Sa printeze stocul actual al produsului
        - pentru avansati - aliniati coloanele

Creati trei instante (produse). Pentru 2 din ele efectuati cate 4-5 operatiuni (intrari, iesiri)

Apelati metoda fisa produsului pentru cele 2 produse
''' #

from datetime import datetime

class stoc():
    '''Pentru stocul unui depozit'''

    def __init__(self, denp, categ, um = 'Buc', sold = 0):
        self.denp = denp
        self.categ = categ
        self.um = um
        self.sold = sold
        self.dd = {}
        self.di = {}
        self.de = {}

    def intrari(self, cant, data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )):
        self.cant = cant
        self.data = data
        if self.dd.keys():
            cheie = max(self.dd.keys()) + 1
        else:
            cheie = 1
        self.dd[cheie] = self.data
        self.di[cheie] = self.cant
        self.sold += self.cant

    def iesiri(self, cant, data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )):
        self.cant = cant
        self.data = data
        if self.dd.keys():
            cheie = max(self.dd.keys()) + 1
        else:
            cheie = 1
        self.dd[cheie] = self.data
        self.de[cheie] = self.cant
        self.sold -= self.cant

    def fisap(self):
        print(36 * '-')
        print('Fisa produsului {0}, um {1}'.format(self.denp, self.um))
        print(36 * '-')
        print(' Nrc ', '  Data  ', ' Intrare', ' Iesire')
        print(36 * '-')
        for elem in self.dd.keys():
            #for elem in self.di.keys():
            if elem in self.di.keys():
                print(str(elem).rjust(5), self.dd[elem], str(self.di[elem]).rjust(7), str(0).rjust(6))
            else:
                print(str(elem).rjust(5), self.dd[elem],  str(0).rjust(7), str(self.de[elem]).rjust(6))
        print(36 * '-')
        print('Soldul final este:', self.sold)
        print(36 * '-')


alune = stoc('Alune', 'Fructe', 'kg')

alune.intrari(100, '20170105')
alune.intrari(50)

alune.iesiri(73, '20170211')
alune.intrari(29)
alune.iesiri(48, '20170606')

alune.sold

alune.fisap()