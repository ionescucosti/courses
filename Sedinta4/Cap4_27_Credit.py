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

def credit(vachiz, avans, doban, rataprincip, moneda):
    soldDatorat = vachiz-10/100
    rprincip=rataprincip*100
    dobLunara = 6/100/12*soldDatorat
    rata = rprincip + dobLunara
    for i in range(1,13):
        print('luna:',i, 'sold:',soldDatorat, 'dobanda lunara:',dobLunara, rata, moneda)
        soldDatorat = soldDatorat-rprincip

credit(30000,5,6,5,'euro')

