# Cap 7 ex 3
# Modul, clasa, functie
# PF - 04/10/2017

"""
1.   Creati modulul gestiune, care contine clasa Stoc, cu urmatoarele metode: 
intrari, iesiri, fisa produsului, valoarea stocului, __str__
2.   Importati modulul ( import gestiune ), creati o instanta pentru clasa Stoc, 
apelati toate metodele posibile
3.   Importati clasa stoc din modulul gestiune (from gestiune import Stoc), 
creati o instanta pentru clasa Stoc, apelati toate metodele posibile        
 """  #

from datetime import datetime


class Stoc:
    """Tine stocul unui depozit"""

    def __init__(self, prod, categ, um='Buc', sold=0):
        self.prod = prod  # parametri cu valori default ii lasam la sfarsitul listei
        self.categ = categ  # fiecare instanta va fi creata obligatoriu cu primii trei param.
        self.sold = sold  # al patrulea e optional, soldul va fi zero
        self.um = um
        self.i = {}  # fiecare instanta va avea trei dictionare intrari, iesiri, data
        self.e = {}  # pentru mentinerea corelatiilor cheia operatiunii va fi unica
        self.d = {}

    def intr(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        self.data = data
        self.cant = cant
        self.sold += self.cant  # recalculam soldul dupa fiecare tranzactie
        if self.d.keys():  # dictionarul data are toate cheile (fiecare tranzactie are data)
            cheie = max(self.d.keys()) + 1
        else:
            cheie = 1
        self.i[cheie] = self.cant  # introducem valorile in dictionarele de intrari si data
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
        self.e[cheie] = self.cant  # similar, introducem datele in dictionarele iesiri si data
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

    def val_stoc(self, pret):
        return pret * self.sold

    def __str__(self):
        return 'Stocul actual pentru {0} este de {1} {2}'.format(self.prod, self.sold, self.um)

if __name__ == "__main__":
    pass
