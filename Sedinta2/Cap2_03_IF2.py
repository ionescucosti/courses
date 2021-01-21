# 203 IF
# Utilizarea if
# PF - 06/10/2017 v3

# Conditii multiple separate:

x = 10

if x == 10:
    print('Adevarat')
if x < 100:
    print('Adevarat')

# Conditii multiple if in if:

if x == 10:
    if x < 100:
        print('Adevarat')
        print(x ** x)

# Conditii multiple simultane (and):

y = 20

if x >= 0 and y >= 0:
    print('x / y = : ', x / y)
    print('x * y = : ', x * y)

# Conditii multiple simultane (or):

if x >= 10 or y < 20:
    print(x - y)
    print(x + y)

# Operatorul ( not ) negarea conditiei ( inversarea valorii de adevar):

if not x > 10:
    print(' x este egal cu: ', x)

# Operatorul ( is) compara doua stringuri ( egalitate si spatiu de memorie ocupat):

z = x

if x is z:
    print('x is z')  # cu is egalitatea se refera si la aceeasi zona de memorie ocupata

print(x is z)
id(x)
id(z)

# Operatorul (in) teseteaza existenta, incluziunea:

sir = 'Astazi invatam despre if'

if 'invatam' in sir:
    print(sir)

# functii aplicabile sirurilor de caractere

print(ord('x'))  # returneaza numarul UFT8 alocat unui caracter

print(chr(97))  # returneaza caracterul UTF8 corespunzator

print(len(sir))  # returneaza numarul de caractere al sirului

input('Apasa <enter> pt a iesi')

