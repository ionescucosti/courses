# Ex 713
# Explica zipfile
# PF 31/05/2016

import zipfile

ob_citeste = zipfile.ZipFile ( "c:/wt/exemplu.zip", "r" )  			# cream obiectul
ob_citeste.read ( 'guta.txt' )  									# citim fisierul
ob_citeste.close ( )

ob_scrie = zipfile.ZipFile ( "c:/wt/exemplu.zip", "a" )
ob_scrie.writestr ( 'paulf.txt', "Am reusit sa scriu" )  			# fisierul in care scriem //  textul
ob_scrie.close ( )

ob_citeste = zipfile.ZipFile ( "c:/wt/exemplu.zip", "r" )
ob_citeste.read('paulf.txt')

for name in ob_citeste.namelist ( ):  						# citire fisier cu selectare nume fisier
	if name == 'guta.txt':
		print (	ob_citeste.read ( name ) )

ob_citeste.extractall ( 'c:/wt/test' )  # extrage  toate fisierele in directorul dat

ob_citeste.extract ( 'guta.txt', 'c:/wt/test' )  			# extrage fisierul specificat in directorul dat

ob_citeste.close ( )

input ( "\n\nApasa <enter> pt a iesi." )
