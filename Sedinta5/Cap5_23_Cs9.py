# 523 Clase
# Clase -  aplicatie stoc marfa
# PF - 10/08/2016

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

