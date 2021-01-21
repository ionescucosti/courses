# 258 Tema 24
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

x=input("enter: ")

if x.isdigit() and x.startswith('07') and len(x)==10:
    print(x)
else:
    print('wrong format')