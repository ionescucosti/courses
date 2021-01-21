# R255 Tema 21
# if, while, metode pentru siruri de caractere
# PF - 06/10/2017 v3

"""
 Creati un progam care sa verifice daca textul introdus
	de un utilizator de la tastatura este un sir care contine cifre sau litere
 Utilizati if, elif, else
 Trebuie sa afisati urmatoarele mesaje:
 	Numar 		        Daca sirul de caractere este format numai din cifre
	Litere 			    Daca sirul de caractere este format numai din litere
	Orice altceva 		Daca sirul de caractere este format din diferite elemente
Puteti pune totul intr-o bucla while?
""" #

while True:
    var = input('Introduceti textul, sau 000 pentru a iesi: ')  # introducem textul

    if var != '000':                    # testam daca este indeplinita conditia de iesire din bucla

        if var.isdigit():               # testam ce tip de caractere avem in sirul introdus
            print('Numar')
        elif var.isalpha():
            print('Litere')
        else:
            print('Diferite caractere')

    else:                               # iese din bucla daca introducem 000
        break
