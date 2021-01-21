# 671 Clase
# Clase
# PF - 10/08/2016

"""
 importati functia datetime din modulul datetime. Instructiune scrisa deja (vezi mai jos)          #
 Initializati o variabila 'cheie' care va da cheile unor dictionare, cu valoarea 1(vezi mai jos)   #
 Creati o clasa 'Stoc' care va avea:                                                               #
 - 2 variabile statice, care sa numere cate produse avem si cate categorii (doar pentru avansati)  #
 - o metoda constructor cu                                                                         #
 denumire produs                                                                                   #
 categoria                                                                                         #
 unitatea de masura default 'Buc'                                                                  #
 sold default 0                                                                                    #
 initializati trei dictionate, cu cheie comuna, pentru data op., intrari si iesiri din stoc        #
 - o metoda intrari cu                                                                             #
 cantitatea,                                                                                       #
 data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )                                             #
 definiti cheia ca variabila globala                                                               #
 testati daca cheia se gaseste in dictionarul cu data op. Daca exista stabileste cheia             #
 ca fiind maximul cheilor existente plus 1, altfel va fi egala cu 1                                #
 introduce in dict intrari cheie si cant                                                           #
 introduce in dict data cheie si data op                                                           #
 actualizeaza soldul                                                                               #
 - o metoda iesiri, similara cu precedenta. Diferente: populam dict iesiri                         #
 - o metoda fisa produsului cu urmatoarele specificatii:                                           #
 Sa printeze 'Fisa produsului "denumire_produs"' (sa stim si noi a cui e fisa)                     #
 Sa printeze ' Nrc ', '  Data  ', ' Intrare', ' Iesire' pentru toate tranzactiile produsului       #
 Sa printeze stocul actual al produsului                                                           #
 pentru avansati - aliniati coloanele                                                              #
 Creati trei instante (produse). Pentru 2 din ele efecturati cate 4-5 operatiuni (intrari, iesiri) #
 Apelati metoda fisa produsului pentru cele 2 produse                                              #
"""  #

from datetime import datetime

class Stoc:
    """Tine stocul unui depozit"""
    tot_categ = 0
    tot_prod = 0
    categorii = list()
    produse = list()
    categ_prod = {}

    def __init__(self, prod, categ, um='Buc', sold=0):
        self.prod = prod			# parametri cu valori default ii lasam la sfarsitul listei
        self.categ = categ  		# fiecare instanta va fi creata obligatoriu cu primii trei param.
        self.sold = sold			# al patrulea e optional, soldul va fi zero
        self.um = um
        self.i = {}					# fiecare instanta va avea trei dictionare intrari, iesiri, data
        self.e = {}					# pentru mentinerea corelatiilor cheia operatiunii va fi unica
        self.d = {}
        Stoc.tot_prod += 1		    # la fiecare instantiere se calculeaza numarul produselor si al categ
        Stoc.produse.append(prod)           # populam lista cu produse

        if categ not in Stoc.categorii:     # populam lista cu categorii, daca nu exista (unicitate)
            Stoc.tot_categ += 1
            Stoc.categorii.append(categ)
            Stoc.categ_prod[categ] = {prod}
        else:
            Stoc.categ_prod[categ].add(prod)

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
        print('----------------------------')
        print(' Nrc ', '  Data ', 'Intrari', 'Iesiri')
        print('----------------------------')
        for v in self.d.keys():
            if v in self.i.keys():
                print(str(v).rjust(5), self.d[v], str(self.i[v]).rjust(6), str(0).rjust(6))
            else:
                print(str(v).rjust(5), self.d[v], str(0).rjust(6), str(self.e[v]).rjust(6))
        print('----------------------------')
        print('Stoc actual       ' + str(self.sold).rjust(10))
        print('----------------------------\n')


fragute = Stoc('fragute', 'fructe', 'kg')       # cream instantele clasei
lapte = Stoc('lapte', 'lactate', 'litru')
ceasuri = Stoc('ceasuri', 'ceasuri')

fragute.sold                    # ATRIBUTE
fragute.intr(100)
fragute.iesi(73)
fragute.intr(100)
fragute.iesi(85)
fragute.intr(100)
fragute.iesi(101)

fragute.d                       # dictinarele produsului cu informatii specializate
fragute.i
fragute.e

fragute.sold
fragute.tot_categ
fragute.categ
fragute.prod
fragute.tot_prod
fragute.um
fragute.categorii
fragute.categ_prod

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

# Mostenire

class Mag1(Stoc):
    """Subclasa a clasei Stoc"""
    def __init__(self, p, c, u, x, y, z = 7):
        self.x = x
        self.y = y
        super().__init__(p,c,u)

    def perisabilitati(self, procent):
        '''Calculeaza valoarea perisabilitatilor si o scade din sold (iesire)'''
        s = 0
        for k,v in self.i.items():
            s += v
        p = int(s * procent / 100 + .99)
        self.iesi(p)

pepeni = Mag1('pepeni', 'fructe', 'kg', 'xpepeni', 'ypepeni')

pepeni.sold

pepeni.intr(2500)
pepeni.intr(1800)
pepeni.iesi(3972)

pepeni.fisap()

pepeni.categ_prod

for elem in Stoc.categ_prod:                               # Listeaza categoriile si produsele aferente
    print ('Produse in categoria: ' + elem)
    for count, val in enumerate(Stoc.categ_prod[elem]):
        print (count+1, val)

fragute.categ_prod

Stoc.categorii
Stoc.tot_categ
Stoc.tot_prod
Stoc.categ_prod

Mag1.produse
Mag1.categorii
Mag1.tot_categ
Mag1.tot_prod
Mag1.categ_prod

tabla = Mag1('tabla', 'mat_constr', 'kg', 'x', 'y')

tabla.intr(1000, '20170501')
tabla.iesi(877, '20170502')
tabla.intr(1500, '20170505')
tabla.iesi(1001)
tabla.intr(500)
tabla.perisabilitati(.5)

tabla.fisap()

pepeni.fisap()

pepeni.perisabilitati(4)

fragute.fisap()

fragute.perisabilitati()
