# 491
# Genereaza username dintr-un fisier
# PF 160719

# ------------------------------------------------------------------------------------------#
# Creati un program care sa primeasca date dintr-un fisier text (people1.txt) si            #
# Sa genereze username astfel: litere mici, prima litera din prenume si max 7 din nume      #
# Rezultatul sa fie scris intr-un alt fisier (scrie.txt)                                    #
# Cititi fisierul nou pentru verificare                                                     #
# ------------------------------------------------------------------------------------------#

inp = open('c:/wt/people1.txt', 'r')  	# deschidem fisierul din care luam datele
out = open('c:/wt/scrie.txt', 'w')  	# deschidem fisierul in care postam username

for line in inp:
    line = line.rstrip()
    prenume, nume = line.split(' ')  	# facem split in doua variabile
    usr = str(prenume).lower()[0] + str(nume).lower()[:7]  			# concatenam cele doua siruri
    out.write(usr + '\n')  				# scrie username generat in fisierul destinat
										# concatenarea cu '\n' este necesara pt a sari la linia urmatoare

inp.close()
out.close()

citeste = open('c:/wt/scrie.txt', 'r')

print(citeste.read())

citeste.close()

input('Apasa <enter> pentru a iesi.')
