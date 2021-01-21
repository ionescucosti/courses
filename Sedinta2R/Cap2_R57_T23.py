# R257 Tema 3
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

nr = input('Introduceti nr de tel in format de 10 cifre \nFormatul numarului este 07xxxxxxxx\n: ')

if nr.isdigit():                # testeaza daca contine doar cifre
    numar_cifre = 0
    for i in nr:                # numara cifrele
        numar_cifre += 1
    if numar_cifre == 10:       # testeaza daca are 10 cifre
        count = 0               # variabila care va numara cifrele (primele 2)
        sir_temp = ''           # variabila in care stocam un subsir format din primele 2 cifre
        for i in nr:
            sir_temp += i
            count += 1
            if count == 2:
                break
        if sir_temp == '07':    # testeaza daca primele 2 cifre sunt 07
            print('Felicitari, nr este corect!')
        else:
            print('Numarul trebuie sa inceap cu 07')
    else:
        print('Numarul dv nu are 10 cifre')

else:
    print('Nu ati introdus cifre')

input('\n\nApasa <enter> pt a iesi.')