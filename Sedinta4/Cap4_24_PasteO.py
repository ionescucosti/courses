# 424
# Exercitii IF - Pastele Ortodox
# PF 160720

#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#
# Creati un program care sa returneze ziua sarbatoarii Pastelui Ortodox intre 1900 -2099            #
# Aplicand algoritmul lui Gauss pentru calculul datei Pastelui pentru anul N, avem urmatorii pasi:  #
# 1. a = N mod 19       2. b = N mod 4      3. c = N mod 7      4. d = (19 a + 15) mod 30           #                          #
# 5. e = (2 b + 4 c + 6 d + 6) mod 7        6. ziua = d + e + 4   (Aprilie)  . 						#
#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#

def paste(N):
    a = N%19
    b = N%4
    c = N%7
    d = (19*a + 15)%30
    e = (2*b + 4*c + 6*d + 6)%7
    ziua = d + e + 4
    if ziua>30:
        print(ziua-30,'mai')
    else:
        print(ziua, 'aprilie')

paste(2020)
paste(2021)
paste(2022)
paste(2023)
paste(2024)
paste(2025)


