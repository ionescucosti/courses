# 103 Variabile
# Variabile
# PF - 06/10/2017 v3

# atribuirea valorii unei variabile
x = 5
print ( x )

# atribuire de valoare mai multor variabile cu aceeasi instructiune
x, y, z, w = 'Ana', 'are', 'mere', ' '
print ( x, y, z )
print(x + w + y + w + z)

# Inversarea valorilor a doua variabile prin metoda atribuirii multiple
a = "animal"
p = 'planta'
a, p = p, a
print(a)
print(p)

x = 0

x = x + 5           # atribuire de valoare printr-o expresie
print ( x )

x += 5              # incrementare ( augmentation )
print ( x )

x -= 5              # decrementare
print ( x )

x *= 7              # inmultire
print ( x )

x /= 7             # impartire
print ( x )

# se dau urmatoarele variabile
numele = 'Popa'
prenumele = 'Victor'
data_nasterii  = '1989-12-22'
locul_nasterii = 'Targoviste'
profesia = 'inginer'
salariul = 9999

# putem completa un formular predefinit, utilizand aceste variabile:
print ( 'Numele studentului: ' + numele +'\nPrenumele studentului: ' + prenumele +
        '\nNascut la data de: ' + data_nasterii + '\nIn localitatea: ' + locul_nasterii +
        '\nProfesia: ' + profesia + '\nSalariul net: ' + str(salariul))

# Concatenare

cifra = 4
nume = 'Bogdan'
cifra2 = '10'

print(nume + cifra)
print(nume + str(cifra))

print(cifra + int(cifra2))

input ( "Apasa <enter> pt a iesi." )

