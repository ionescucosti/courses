# 202 IF
# Utilizarea if
# PF - 06/10/2017 v3

# Onorariu 10 lei/ora.
# Daca numarul de ore este mai mare de 170 tariful va fi dublu
Ore = float( input('Introduceti numarul de ore: ') )

Tarif = float( input('Introduceti tariful orar: ') )

if Ore > 170:
    Onorariu = Ore * Tarif + (Ore - 170) * Tarif  # tarif conditionat
else:
    Onorariu = Ore * Tarif  # tarif normal

print('Onorariul este: ', Onorariu)

''' Schimb valutar RON -> EUR sau EUR -> RON
	- introducem valuta dorita si schimbam in caractere mari
	- testeaza daca introducem corect numele valutei (caractele alpha)
	- testeaza daca am introdus valuta corecta RON sau EUR
	- introducem suma. Testeaza daca am introdus suma corect (cifre) si o transforma in intreg
	- returneaza suma si valuta sau mesaj de eroare '''

valuta = input('Introduceti RON pentru conversia Euro in Lei :\nsau EUR pt. conversia  Lei in Euro: ')
valuta = valuta.upper()
curs = 4.60

if valuta.isalpha():
    if valuta == 'RON':
        euro = input('Cati euro schimbati? ')
        if euro.isdigit():
            euro = int(euro)
            print('Ati primit', '%.2f' % float(euro * curs), 'RON')
        else:
            print('Nu ati introdus un numar valid!')

    elif valuta == 'EUR':
        lei = input('Cati lei schimbati? ')
        if lei.isdigit():
            lei = int(lei)
            print('Ati primit', '%.2f' % float(lei / curs), 'EURO')
        else:
            print('Nu ati introdus un numar valid!')

    else:
        print('Valuta inexistenta!')
else:
    print('Valoarea introdusa poate fi RON sau EUR!')

# putem pune totul intr-o functie si o apelam ori de cate ori avem nevoie

input('Apasa <enter> pt a iesi')
