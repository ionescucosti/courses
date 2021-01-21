# Ex 712
# Explica zipfile - cream obiect zip, listeaza fisiere, listeaza caracteristici
# CP - 1/26/13

import zipfile

fisier_zip = zipfile.ZipFile ( "c:/wt/exemplu.zip", "r" )  # cream un obiect cu arhiva

for nume in fisier_zip.namelist ( ):  # listeaza numele fisierelor din arhiva
	print ( "Fisier:", nume )

for info in fisier_zip.infolist ( ):  # lista cu informatii despre fisiere
	print ( '\n', info.filename )
	print ( '\tComment:\t', info.comment )
	print ( '\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)' )
	print ( '\tZIP version:\t', info.create_version )
	print ( '\tCompressed:\t', info.compress_size, 'bytes' )
	print ( '\tUncompressed:\t', info.file_size, 'bytes' )

fisier_zip.close ( )

input ( "\n\nApasa <enter> pt a iesi." )
