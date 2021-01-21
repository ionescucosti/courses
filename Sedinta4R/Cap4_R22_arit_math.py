# 472
# Op aritm / math in Python
# PF 160716

from math import sqrt  # importa functiile mentionate din modulul math


# 1.	√a² + b² - Teorema lui Pitagora. Calculeaza lungimea ipotenuzei intr-un triunghi dreptunghic
#-------------------------------------------------------------------------------------------------------#

def pitag(a, b):
    """Primeste ca argumente lungimea celor doua catete si returneaza lungimea ipotenuzei"""
    ipotenuza = sqrt ( a ** 2 + b ** 2 )
    print ( 'Ipotenuza este: ' + str ( ipotenuza ) )

pitag ( 3, 4 )
#-------------------------------------------------------------------------------------------------------#
# 2.	Aria si volumul sferei A = 4πr² , V = 4/3πr³

def sfera(raza):
    d = 2 * raza
    c = pi * ( raza ** 2 )
    s = 4 * pi * ( raza ** 2 )
    v = (4 / 3) * pi * ( raza ** 3 )
    return 'Diametrul: {0:.2f}\nCircumferinta: {1:.2f}\nAria: {2:.2f}\nVolumul: {3:.2f}'.\
        format(d,c,s,v)

sfera ( 5 )
#-------------------------------------------------------------------------------------------------------#
# 3.	Cumparaturi online: costul de transport este de 5 lei(fixa) plus 0.20 lei/ 10 lei cost produs

def shiping_cost(cos_cump):
    sc = cos_cump / 10.0 * .2 + 5
    return sc

print ( shiping_cost ( 568 ) )
#-------------------------------------------------------------------------------------------------------#
# 4.	Pe un plan avem doua puncte a(x1, y1) si b(x2, y2). Scrieti un program care sa calculeze panta intre a si b
# panta este (y2-y1)/(x2-x1)

def panta(x1, y1, x2, y2):
    """Calculeaza panta intre doua puncte situate pe un plan"""
    return ( (y2 - y1) / (x2 - x1) )

panta ( 1, 2, 5, 5 )
#-------------------------------------------------------------------------------------------------------#
# 5.	Distanta intre doua puncte in plan (radical din (x2-x1)² + (y2-y1)²

def distp(x1, y1, x2, y2):
    d = sqrt ( (x2 - x1) ** 2 + (y2 - y1) ** 2 )
    return d

print ( distp ( 1, 2, 5, 5 ) )
#-------------------------------------------------------------------------------------------------------#
# 6.	Calculeaza suma primelor n numere, n determinat de utilizator

def suma_n(n):
    """Calculeaza suma a n numere"""
    aduna = 0
    for i in range ( n + 1 ):
        aduna += i
    print ( aduna )

suma_n ( 10 )
#-------------------------------------------------------------------------------------------------------#
# 7.	Calculeaza suma cuburilor a n numere, n determinat de utilizator

def suma_cub(n):
    """Calculeaza suma cubului a n numere"""
    aduna = 0
    for i in range ( n + 1 ):
        aduna = aduna + i ** 3
    print ( aduna )

suma_cub ( 10 )
#-------------------------------------------------------------------------------------------------------#
# 8.	Creati un program care sa listeze puterile lui doi de la 1 la n

def two_to_n(n):
    x = 1
    for i in range ( n + 1 ):
        x = 2 ** i
        print ( i, x )

two_to_n ( 32 )

#-------------------------------------------------------------------------------------------------------#
# 9.

'''Leibniz a calculat valoarea lui π astfel:
π = 4( 1 – 1/3 + 1/5 – 1/7 + … )
Scrieti un program, cu o functie, care sa primeasca numarul de iteratii si sa
returneze valoarea lui π.
''' #

from math import pi

def calc_pi(iter):
    s = 1
    for i in range(2, iter + 1):
        if 2 * i % 4 == 0:
            s -= 1 / (2 * i - 1)
            print('i=', i)
            print('numarator = ',(2 * i - 1))
        else:
            s += 1 / (2 * i - 1)
            print('ie=', i)
            print('numarator e = ', (2 * i - 1))
    return 'pi: ' + str(s *4)


input ( 'Apasa <enter> pentru a iesi.' )
