# Cap 4 Tema 4
# Crearea unei functii simple
# PF - 27/05/2016

# ------------------------------------------------------------------#
# Sa se realizeze un program cu o functie care sa caute             #
# cuvinte in fisierul dat de utilizator cu ajutorul (try-except)    #
# Functia trebuie sa afiseze linia unde gaseste cuvantul respectiv. #
# ------------------------------------------------------------------#

def cauta_cuv(fisier, cuvant):
    try:
        file = open(fisier)
    except:
        print("Nu se poate deschide fisierul ", str(fisier))
    else:
        print("Fisierul urmator a fost dechis: ", str(fisier))
        text = file.readlines()
        if type(cuvant) == str:
            for line in text:
                if line.find(cuvant) != -1:
                    print(line)
        else:
            print("Cuvant nu este sir de caractere")
        file.close()
    print("\n")

cauta_cuv("c:/wt/guta.txt", "Guta")
cauta_cuv("c:/wt/guta.txt", "gagauta")
cauta_cuv("c:/wt/guta.txt", "si")

input("\n\nApasa enter pt. a iesi")
