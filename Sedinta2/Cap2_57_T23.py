# 257 Tema 23
# if, for
# PF - 06/10/2017 v3

'''
 	Creati un program in care utilizatorul sa introduca un numar de telefon.
 	Acesta trebuie sa introduca un numar cu formatul de 10 cifre si sa inceapa cu 07
 	Realizati acest program cu ajutorul unui if in if astfel :
	Nu aveti voie sa folositi and sau or in if. 
	Verificati daca utilizatorul a introdus exclusiv un numar.
	In caz contrar avertizati utilizatorul de greseala si iesiti din program
	Daca sirul de caractere este format din numere, numarati caracterele sirului
	cu ajutorul unui for. Daca numarul de caractere difera informati utilizatorul.
 	Daca numarul de caractere al sirului este 10 verificati daca primele doua caractere
 	sunt 0 si 7 cu ajutorul unui for. Daca primele doua caractere difera informati utilizatorul.
 	In cazul in care trece de toate aceste verificari atunci afisati mesajul <<Felicitari!>>
''' #

x=input('enter: ')

if x.isdigit():
    if x.startswith('07'):
        if len(x)==10:
            print('Phone: ',x)
        else:
            print('Length must be 10')
            c=0
            for i in x:
                c+=1
            print('Not: ',c)
    else:
        print('Must startswith: 07')
else:
    print('Must be digits')

