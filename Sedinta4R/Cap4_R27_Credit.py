'''
Contractati un credit. Aveti urmatorii parametrii de intrare:
- valoarea de achizitie:
- avans - default 10% din valoarea de achizitie
- rata anuala a dobanzii - default 6%
- plati lunare principal - default 5% din valoarea de achizitie ( dobanda se adauga )
- moneda - default lei
Scrieti un program care să afișeze un tabel cu scadenta si platile pe durata de viață a împrumutului.
Fiecare rând al tabelului va contine:
- numărul lunii (începând cu 1)
- soldul total datorat
- dobânda datorată pentru luna in curs
- principalul datorat pentru luna in curs
- rata lunii in curs (principal plus dobanda)
- soldul ramas după efectuarea plății
- total dobanzi platite la finalul creditului
Valoarea dobanzii lunare va fi dobanda anuala / 12. Suma
principal pentru o lună este egală cu plata lunară minus dobânzile datorate.
'''#

def credit(valAchiz, procAvans = 0.1, dobAn = .06, procPlata = .05, moneda = 'lei'):
    '''afișeaza un tabel cu scadenta si platile imprumutului'''
    nrl = 0
    sold_ini = valAchiz * (1 - procAvans)
    dobTotal = 0
    print('Structura unui credit de {0:.2f} {4}, cu o dobanda anuala\
        \nde {1:.2f}%, cu un avans de {2:.2f} {4} si plati lunare\
        \n(principal) de {3:.2f} {4} din val de achizitie'.
        format(valAchiz, dobAn * 100, valAchiz * procAvans, valAchiz * procPlata, moneda))
    print('----------------------------------------------------------')
    print(' Luna-Sold Initial-Dobanda-Principal-Rata Luna-Sold final')
    print('----------------------------------------------------------')
    while sold_ini > 0:
        nrl += 1
        dobDat = sold_ini * dobAn / 12
        dobTotal +=dobDat
        princDat = valAchiz * procPlata
        if princDat > sold_ini:
            princDat = sold_ini
        rataLuna = princDat + dobDat
        sold_fin = sold_ini - princDat
        print(str(nrl).rjust(3), '{:.2f}'.format(sold_ini).rjust(12), '{:.2f}'.format(dobDat).rjust(8),\
              '{:.2f}'.format(princDat).rjust(8), '{:.2f}'.format(rataLuna).rjust(10),\
              '{:.2f}'.format(sold_fin).rjust(12))
        print('----------------------------------------------------------')
        sold_ini = sold_fin
    print('Total dobanda: {:.2f}'.format(dobTotal).rjust(25))
    print('----------------------------------------------------------')

credit(100000)

credit(1800000, 0.2, 0.07, 0.016666666667, 'Euro')

credit(1500000, 0.1, 0.07, 0.016666666667, 'GBP')

credit(1000000,0,.08,.021,'Eur')