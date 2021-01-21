# 451
# Genereaza username dintr-un fisier
# PF 160719

# ------------------------------------------------------------------------------------------#
# Creati un program care sa primeasca date dintr-un fisier text (people1.txt) si            #
# Sa genereze username astfel: litere mici, prima litera din prenume si max 7 din nume      #
# Rezultatul sa fie scris intr-un alt fisier (scrie.txt)                                    #
# Cititi fisierul nou pentru verificare                                                     #
# ------------------------------------------------------------------------------------------#

# deschidem fisierul din care luam datele

# deschidem fisierul in care postam username

# facem split in doua variabile
# concatenam cele doua siruri
# scrie username generat in fisierul destinat
# concatenam username cu '\n' este necesara pt a sari la linia urmatoare

file = open('C:/Users/ext_constantini/WORK/people1.txt','r')
userlist= open('C:/Users/ext_constantini/WORK/people.txt','w')
lines = file.readlines()
for line in lines:
    words=line.split()
    p=words[0]
    n=words[1]
    user=p[0]+n[0:8]+'\n'
    userlist.write(user.lower())

userlist.close()
file.close()

