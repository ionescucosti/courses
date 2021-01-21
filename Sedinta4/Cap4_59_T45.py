# Cap 4 tema 5
# Crearea unei functii simple
# PF - 27/05/2016

# --------------------------------------------------------------------------------------------------#
# Creati o functie care sa calculeze si sa returneze [a(a+3)/b]*c exclusiv pentru 3 numere a, b, c. #
# Daca nu sunt numere returnati sirul de caractere "Parametrii trebuie sa fie numere: ":            #
# --------------------------------------------------------------------------------------------------#

a = input('enter a: ')
b = input('enter b: ')
c = input('enter c: ')

def calculate(a,b,c):
    if a.isdigit() and b.isdigit() and c.isdigit():
        a = int(a)
        b = int(b)
        c = int(c)
        return (a*(a+3)/b)*c
    else:
        return "Parametrii trebuie sa fie numere: ",a,b,c

print(calculate(a,b,c))