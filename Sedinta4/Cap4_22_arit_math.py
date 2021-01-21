# 422
# Op aritm / math in Python - Creaza functii care sa faca ...
# PF 160716


#-------------------------------------------------------------------------------------------------------#
# 1.	√a² + b² - Teorema lui Pitagora. Calculeaza lungimea ipotenuzei intr-un triunghi dreptunghic

# def ip(a,b):
#     return sqrt(a**a + b**b)
#
# print(ip(2,3))
#-------------------------------------------------------------------------------------------------------#
# 2.
'''
Scrieti un program, care sa cuprinda o functie ce primeste ca argument raza sferei.
Va returna diametrul, circumferinta, aria si volumul sferei (float cu 2 zecimale).
Fiecare din cele 4 informatii vor fi printate pe cate un rand. Apelati functia.
Utilizati:  from math import pi (D = 2r, C = 2πr, A = 4πr² , V = 4/3πr³)
''' #

# def calc(r):
#     d = 2*r
#     c = 2*pi*r
#     a = 4*pi*r**2
#     v = 4 / 3*pi**3
#     print('diamentrul: ',d,'\ncircumferinta: ',c,'\naria: ',a,'\nvolumul: ',v)
#
# calc(10)

#-------------------------------------------------------------------------------------------------------#
# 3.	Cumparaturi online: costul de transport este de 5 lei(fix) plus 0.02 lei/ 10 lei(variabil) cost produs

# def total(x):
#     tot=x+5+0.02*(x//10)
#     print(tot)
#
# total(100)

#-------------------------------------------------------------------------------------------------------#
# 4.	Pe un plan avem doua puncte a(x1, y1) si b(x2, y2). Scrieti un program care sa calculeze panta
# intre a si b
# panta este (y2-y1)/(x2-x1)

# def panta(x1,x2,y1,y2):
#     return (y2-y1)/(x2-x1)
#
# print(panta(20,3,40,5))
#-------------------------------------------------------------------------------------------------------#
# 5.	Distanta intre doua puncte in plan (radical din (x2-x1)² + (y2-y1)²)
# def panta(x1,x2,y1,y2):
#     return sqrt((x2-x1)**2 + (y2-y1)**2)
#
# print(panta(20,3,40,5))



#-------------------------------------------------------------------------------------------------------#
# 6.	Calculeaza suma a n numere, n introdus de utilizator
# def sumanr(n):
#     return (n*(n+1))/2
# print(sumanr(3))
#-------------------------------------------------------------------------------------------------------#
# 7.	Calculeaza suma cuburilor a n numere, n introdus de utilizator

# def sumacub(n):
#     return (n**3 * (n+1)**3) / 2
# print(sumacub(2))
#-------------------------------------------------------------------------------------------------------#
# 8.	Creati un program care sa listeze puterile lui doi de la 1 la n
# def puteredoi(n):
#     for i in range(1,n+1):
#         print(2**i)
# puteredoi(6)
#-------------------------------------------------------------------------------------------------------#
# 9.

'''Leibniz a calculat valoarea lui π astfel:
π = 4( 1 – 1/3 + 1/5 – 1/7 + … )
Scrieti un program, cu o functie, care sa primeasca numarul de iteratii si sa
returneze valoarea lui π.
''' #
def calculLeibniz(n):
    pi = 0
    x = 1
    for i in range(1,n):
        pi+= 4*(1/x-1/x+2)
        x+=4
    return pi
print(calculLeibniz(3))

#input ( 'Apasa <enter> pentru a iesi.' )

