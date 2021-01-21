# Ex 707
# Modulul pickle
# InfoAcademy PF 2016-05-27

import pickle

prenume = {1: "Gina", 2: "Dragos", 3: "Alina", 4: "Marian"}
nume = ["Popa", "Miulescu", "Vasile", "Coman"]
x = 100
y ='lkjahflksdjfh'

fisier = open("pickle.txt", "wb")  	    # numele fisierului este ales de noi

pickle.dump(nume, fisier)	            # scriere variabila nume in fisier
pickle.dump(prenume, fisier)
pickle.dump(x, fisier)
pickle.dump('Astazi ploua', fisier)
pickle.dump(y,fisier)

fisier.close ( )

fisier_citit = open ( "pickle.txt", "rb" )

nume_citit = pickle.load ( fisier_citit )       # citire variabila nume / atribuire unei variabile
prenume_citit = pickle.load ( fisier_citit )
y = pickle._load(fisier_citit)

print (nume_citit)
print (prenume_citit)

# Putem prelucra informatia
for item in prenume_citit:
	print (item, prenume_citit[item], nume_citit[item - 1])

input ( "\n\nApasa <enter> pt a iesi." )
