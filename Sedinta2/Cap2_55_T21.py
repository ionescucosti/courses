# 255 Tema 21
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
x=input("enter: ")
while True:
    if x.isalpha():
        print('Litere')
    elif x.isdigit():
        print('Numar')
    else:
        print('Orice altceva')
    break