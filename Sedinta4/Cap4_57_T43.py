# Cap 4 tema 3
# Crearea unei functii simple
# PF - 27/05/2016

# Creati un program cu o functie care sa poata cauta cuvinte in orice text

def search(word, text):
    if word in text:
        print('yes')
    else:
        print('nop')

search('mu', 'muma')