# 822
# regex
# CP

import os
import re

print ( "aplicam comanda ping in consola" )

stdin = os.popen('ping -n 1 8.8.8.8')
stdout = os.popen('ping -n 1 8.8.8.8')
print ( stdin )
print ( stdout,"\n\n" )
stdin.close()

print ( "Citim output" )
captura = stdout.read()

print ( "Afisam output" )
print ( captura )

print ( "Cautam cu ajutorul modulului re statusul ping" )
print ( "Metoda 1" )

cauta=re.search("((\d){1,3}%\sloss)",captura)
if cauta:
    print ( cauta.group(0) )

print ( "\nCautam cu ajutorul modulului re statusul ping" )
print ( "Metoda 2" )

cauta=re.search("Lost\s=\s(\d+)",captura)
if cauta:
    print ( cauta.group(0) )

print ( "\nCautam cu ajutorul modulului re statusul ping" )
print ( "Metoda 3" )

cauta=re.search("Lost = (\d+)",captura)
if cauta:
    print ( cauta.group(0) )
    
