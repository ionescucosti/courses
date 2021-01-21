# Cap 4 Tema 3
# Cautare in text
# PF - 27/05/2016

# Creati un program cu o functie care sa poata cauta cuvinte in orice text
def cauta_cuv(cuv, text):
    text_s = text.split(' ')
    for e in text_s:
        if e == cuv:
            return True

fisier = open("c:/wt/guta.txt")

cauta_cuv('caruta', fisier.read())

fisier.close()

input("\n\nApasa enter pt. a iesi")
