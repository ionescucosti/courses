# 426
# Exercitii IF -Pastele Catolic
# PF 160720

# ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#
# Creati un program care sa returneze ziua in care are (a avut) loc sarbatoarea Pastelui Catolic intre 1900 -2099    #
# a = year%19, b = year%4, c = year%7, d = (19a + 24)%30, e = (2b + 4c + 6d + 5)%7                                   #
# data Pastelui este 22 Martie + d + e. Atentie, in anii 1954,1981, 2049, 2076 este cu o saptamana mai devreme       #
# ---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#

def pasteCatolic(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    data=22+d+e
    if data>31:
        print(data-31,'aprilie')
    else:
        print(data,'martie')

pasteCatolic(2020)
