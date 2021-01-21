# 302 Type
# Type
# PF - 27/05/2016

# type() indica tipul de date al unei constante, variabile, etc;

x = 'sir'
y = 7
z = 7.3

print(type ( x ))
print(type ( y ))
print(type ( z ))
print(type ( 'string' ))
print(type ( 25 ))
print(type ( 42.5 ))
print(type ( True ))
print(type ( None ))
print(type ( type ))

import math                 # importam modulul math

print(type ( math ))
print(type ( len ))

# Conversii str(), int() si float() - COMPATIBILITATE
print(int ( 15.8 ))
print(float ( 7 ))
print(int ( '357' ))
print(str ( 55 ))
print(float ( '777' ))
print(str ( 222.0 ))
var = input ( 'Introduceti un numar rational: ' )
print ('Float:', float ( var ))
print ('Intreg:', int ( float(var) ))

input ( 'Apasa <enter> pt a iesi.' )
