# Cap 4 tema 4
# Crearea unei functii simple
# PF - 27/05/2016

# ------------------------------------------------------------------#
# Sa se realizeze un program cu o functie care sa caute             #
# cuvinte in fisierul dat de utilizator cu ajutorul (try-except)    #
# Functia trebuie sa afiseze linia unde gaseste cuvantul respectiv. #
# ------------------------------------------------------------------#

def search(word, file):
    try:
        f=open(file,'r')
        lines=f.readlines()
        for line in lines:
            if word in line:
                print(line)
    except Exception as e:
        print('Error: ',e)

search('a', 'try_test.txt')