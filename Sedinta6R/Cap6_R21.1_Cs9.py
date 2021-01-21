# 621 Clase avansat
# Clase avansat
# PF - 10/08/2016

'''
Adaptati programul creat la exercitiul 521 astfel incat sa devina o superclasa si creati
   2-3 subclase magazin1, 2, .... Fiecare subclasa va avea si 1-2 metode proprii
 importam functia datetime din modulul datetimxe. Instructiune scrisa deja
 Initializam o variabila 'cheie' care sa dea cheile unor dictionare
 Cream o clasa 'Stoc' care va avea:
	- 2 variabile statice, care sa numere cate produse avem si cate categorii (doar pentru avansati)
	- o metoda constructor cu
 	denumire produs, categoria, unitatea de masura default 'Buc', sold default 0
 	initializare trei dictionate, cu cheie comuna, pentru data op., intrari si iesiri din stoc
    - o metoda intrari cu
 cantitatea,
 data = str ( datetime.now ( ).strftime ( '%Y%m%d' ) )
 testam daca cheia se gaseste in dictionarul cu data op. Daca exista stabileste cheia
   ca fiind maximul cheilor existente plus 1, altfel va fi egala cu 1
 introduce in dict intrari cheie si cant
 introduce in dict data cheie si data op
 actualizeaza soldul
	- o metoda iesiri, similara cu precedenta. Diferente: populam dict iesiri
 	- o metoda fisa produsului cu urmatoarele specificatii:
 Sa printeze 'Fisa produsului denumire_produs' (sa stim si noi a cui e fisa)
 Sa printeze ' Nrc ', '  Data  ', ' Intra', ' Iese' pentru toate tranzactiile produsului
 Sa printeze stocul actual al produsului
 pentru avansati - aliniati coloanele
 Creati trei instante (produse). Pentru 2 din ele efecturati cate 4-5 operatiuni (intrari, iesiri)
 Apelati metoda fisa produsului pentru cele 2 produse
''' #

from datetime import datetime

class depozit_mogosoaia(Stoc):

    def perisabilitati(self, procent_aplicat):
        '''Atentie, procentul va fi de forma .01 pentru 1%'''
        self.date = data
        suma = 0
        for i in self.miscari.values():
            suma += i[1]
        perisabilitati = int(procent_aplicat * suma)
        if self.miscari.keys():
            cheie = max(self.miscari.keys())  + 1
        else:
            cheie = 1
        self.iesiri(perisabilitati)

    def cauta_tranzactii(self,
                            data_start= str(datetime.now().strftime('%Y%m%d')),
                            data_final = str(datetime.now().strftime('%Y%m%d'))):
        if self.miscari != {}:
            print('*-* ' * 8)
            print('Fisa produsului {0}, {1} \nintre {2} si {3}'.
                  format(self.denp, self.um, data_start, data_final)
                  )
            print('-' * 30)
            print(' Nrc ', '  Data  ', ' Intrare', ' Iesire')
            print('-' * 30)
            for i in self.miscari.keys():
                if data_start <= self.miscari[i][0] and data_final >= self.miscari[i][0]:
                    print(i,
                          str(self.miscari[i][0]).rjust(10),
                          str(self.miscari[i][1]).rjust(8),
                          str(self.miscari[i][2]).rjust(6))
            print('-' * 30)
        else:
            print('Sold zero')

bere = depozit_mogosoaia('bere_bruna', 'aliment', 'doze')

bere.intrari(1000, '20170206')
bere.iesiri(870, '20170308')
bere.intrari(2500, '20170509')
bere.iesiri(1897)
bere.perisabilitati(.01)
bere.fisap()
bere.cauta_tranzactii('20170101', '20170531')

