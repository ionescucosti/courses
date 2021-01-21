# Ex 715
# Explica zipfile -  arhiva compresata / necompresata
# PF 31/05/2016

import zipfile

# Cream arhiva necompresata

arh_necomp = zipfile.ZipFile ( 'c:/wt/exemplu5.zip', 'r' )  	# cream o arhiva noua, necompresata

for info in arh_necomp.infolist ( ):  							# verificam daca e compresata
	print ( '\n', info.filename )
	print ( '\tCompressed:\t', info.compress_size, 'bytes' )
	print ( '\tUncompressed:\t', info.file_size, 'bytes' )

arh_necomp.close ( )

# Cream arhiva compresata (necesita modulul zlib, instalat standard )

arh_comp = zipfile.ZipFile ( 'c:/wt/exemplu6.zip', mode='w', compression=zipfile.ZIP_DEFLATED )
arh_comp.write ( 'c:/wt/medici.txt' )

for info in arh_comp.infolist ( ):  							# verificam daca e compresata
	print ( '\n', info.filename )
	print ( '\tCompressed:\t', info.compress_size, 'bytes' )
	print ( '\tUncompressed:\t', info.file_size, 'bytes' )

arh_comp.close ( )

input ( "\n\nApasa <enter> pt a iesi." )


help(zipfile)