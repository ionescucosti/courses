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
'''#

from Course.Sedinta5R import Cap5_R21_Cs91


class magazin1(Cap5_R21_Cs91.stoc):
    pass