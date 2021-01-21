# Ex 706
# Modulul tempfile
# InfoAcademy PF 2016-05-27

import tempfile

temp = tempfile.mktemp ( )  			# cream fisierul temp

print ( temp )

fisier = open ( temp, 'w+' )

fisier.write ( '''Astazi e siua ta, Zi frumoasa ca tine''' )

fisier.close ( )

fisier = open ( temp, 'r+' )

fisier.read ( )

fisier.close ( )

print ( tempfile.gettempdir ( ) ) # directorul in care se afla fis temporar )

tempfile.mkdtemp ( )  # creeaza un director temporar

import os

os.remove ( temp )


