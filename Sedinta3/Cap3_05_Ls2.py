# 305 Lista
# Lista - mutabilitate
# PF - 27/05/2016

# Aliasuri versus liste separate.
lista_1 = ['ana', 'ada', 'ema']
lista_2 = lista_1
lista_2[2] = 'ala'

lw = [["a","b"], 5, "abc"]
ly = lw
lw[0] = ['a', 'x']
print(lw, ly)

print ( lista_1, lista_2 )          # surpriza: modificarea din lista 2 s-a propagat si in lista 1
print ( lista_1 is lista_2 )
print ( lista_1 == lista_2 )
id ( lista_1 )
id ( lista_2 )

# Pentru a evita aceasta situatie creati liste separate, chiar daca initial au elemente identice
lista_3 = [3, 7, 13]
lista_4 = [3, 7, 13]

print ( lista_3 is lista_4 ) 		# diferenta dintre "is" si "==" in cazul listelor
print ( lista_3 == lista_4 )
lista_4[2] = 99
print ( lista_3, lista_4 )
id ( lista_3 )
id ( lista_4 )

# Concatenare / multiplicare
lista1 = [1, 2, 3]
lista2 = [6, 7, 8]
lista3 = lista1 + lista2 +[10] # concatenare liste
print ( lista3 )
lista4 = 3 * lista2  # multiplicare lista
print ( lista4 )

# listele 1 si 2 au ramas in continuare neschimbate

input ( 'Apasa <enter> pt a iesi.' )
