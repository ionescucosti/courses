# R258 Tema 24
# if, for, metode siruri de caractere, functii
# PF - 06/10/2017 v3

'''
    Creati un program in care utilizatorul sa introduca un numar de telefon.
 	Acesta trebuie sa introduca un numar cu formatul de 10 cifre si sa inceapa cu 07.
  	Verificati daca utilizatorul a introdus exclusiv un numar si daca incepe cu
		07 (zero sapte) in sir cu ajutorul metodelor invatate si al unui if. In caz contrar
		avertizati utilizatorul de greseala si iesiti din program.
 	Daca sirul de caractere este format din numere si incepe cu 07, numarati caracterele
		sirului cu ajutorul len(). In cazul in care trece de aceste verificari atunci
		afisati mesajul <<Felicitari!>>
''' #

sir = input ( "Scrie un numar de telefon!\nCare sa contina 10 cifre si sa inceapa cu '07'\n" )
nr_caractere = 0

if sir.isdigit ( ) and sir.startswith('07')==True:

	if len(sir) == 10:
		print ( "Felicitari! Numarul e acceptat." )
	else:
		print ( "Numar de cifre invalid\n" )
else:
	print ( "Caracterele din sir nu sunt exclusiv numere sau nu incep 07" )

#---#--- sau ---#---#

nr_tel = input('Introduceti numarul de telefon(10 cifre, incepe cu 07): ')
if nr_tel.isdigit() == False:
    print('Numarul dv este gresit. Trebuie sa contina doar cifre')
else:
    if nr_tel.find('07') != 0:
        print('Numar invalid. Trebuie sa inceapa cu 07')
    else:
        if len(nr_tel) != 10:
            print('Numar invalid. Numarul cifrelor trebuie sa fie 10')
        else:
            print('Felicitari! Numar acceptat.')


input ( "\n\nApasa <enter> pt a iesi." )
