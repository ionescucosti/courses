# Ex 608
# Variabila Globala: apelare, existenta, creare
# InfoAcademy PF 2016-05-27

a = 100                     # Creare VG
b = 'caine'

globals()                   # DICT cu VG la un moment dat


if 'b' in globals():
    print ( b )             # verifica existenta VG

globals()['b'] = 'pisica'   # atribuire valoare VG

globals()['c'] = 'maimuta'  # atribuire valoare VG
