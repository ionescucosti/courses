# 308 Set
# Set
# PF - 27/05/2016

# Metode aplicabile unui set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8}

set1.add ( 6 )  			# Adauga elementul, daca nu exista
print ( set1 )

set2.clear ( )  			# Sterge toate elementele
print ( set2 )
set2 = {3, 4, 5, 6, 7, 8}

set3 = set1.copy ( )  		# Creaza o copie a setului
id ( set3 )
id ( set1 )

print ( set3 is set1 )
print ( set3 == set1 )

print ( set1 - set2 )			# Returneaza elem set 1 mai putin elementele comune cu set 2
print ( set2.difference ( set1 ) )

set1.discard ( 6 )  			# Elimina elementul, daca exista
print ( set1 )

print ( set1 & set2 )			# Returneaza elementele identice din cele 2 seturi
print ( set2.intersection ( set1 ) )

set1.pop ( )  					# Sterge primul element
print ( set1 )
set2.pop ( )
print ( set2 )

set2.remove ( 6 )  				# Sterge elementul daca exista. Altfel eroare
print ( set2 )

print ( set1 ^ set2 ) 			# Dif simetrica. Uneste sirurile, mai putin elem comune
print ( set2.symmetric_difference ( set1 ) )

set1 | set2  					# returneaza valori unice din cele 2 siruri (elimina duplicatele)
set2.union ( set3 )

set2.update ( set3 )  			# Adauga elem set3 la set 2
print ( set2 )
len ( set2 )

if 8 in set2:  					# cautare intr-un set dupa numele elementului
	print ( 'Element gasit!' )

input ( 'Apasa <enter> pt a iesi.' )
