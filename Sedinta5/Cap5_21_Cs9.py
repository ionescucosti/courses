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

