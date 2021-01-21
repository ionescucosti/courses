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

def credit (val_ach, avans = 10, rata_dob =6, proc_plati_lunare = 5, moneda = 'Lei'):
    nr_luna = 1
    sold = val_ach - val_ach * avans / 100
    dobanzi_platite_total = 0
    print(' Luna-Sold Initial-Dobanda-Principal-Rata Luna-Sold final')
    while sold > 0:
        dob_lunara = sold * (rata_dob / 100 / 12)
        principal_lunar = val_ach * proc_plati_lunare /100
        dobanzi_platite_total += dob_lunara
        if principal_lunar > sold:
            rata_curenta = dob_lunara + sold
        else:
            rata_curenta = dob_lunara +principal_lunar
        print(str(nr_luna).rjust(4), str(sold).rjust(12), str(dob_lunara).rjust(7),
              str(principal_lunar).rjust(10), str(rata_curenta).rjust(8),
              str(sold - rata_curenta + dob_lunara).rjust(10)
              )
        sold -= principal_lunar
        nr_luna += 1
    print(' Luna-Sold Initial-Dobanda-Principal-Rata Luna-Sold final')
    print(' Ai de platit dobanzi totale: ',dobanzi_platite_total)

credit(100000, 10, 12, 5, 'Eur')
