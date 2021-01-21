# Cap 4 tema 2
# Explica accesarea fisierelor
# PF - 27/05/2016

# --------------------------------------------------------------------------------------------------#
# Creati un program care sa citeasca toate liniile unui text (guta.txt) sub forma unei liste si     #
# afisati lista. Scrieti o linie intr-un fisier, cu un text la alegere                              #
# Cititi tot fisierul intr-un singur sir de caractere apoi afisati-l.                               #
# --------------------------------------------------------------------------------------------------#

print ( "Citeste liniile unui text si le adauga intr-o lista.\n" )
text = open ( 'c:/wt/guta.txt', "r" )
linii = text.readlines()
print (linii)

print ( "\nVom scrie o linie la sfarsitul textului\n" )
text = open ( 'c:/wt/guta.txt', "w+" )
text.write ( "\nAstazi am testat scrierea in fisier\n" )  		# scrie o linie in fisier
text.close ( )

text = open ( "c:/wt/guta.txt", "r" )
print ( text.read ( ) ) # citeste toate liniile intr-un sir de caracter
text.close ( )
