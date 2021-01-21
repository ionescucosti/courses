# Program modul
# Explica crearea unui modul
# PF 2017/04/12

import sys
# import os
lista = [14, 29, 75, 98]

if sys.platform == 'win32':
    import a755     # NUMELE MODULULUI TAU
    print(a755.aduna(1,7,9))
    print( a755.aduna(1,2,3,4,5,6,7,8,9,0))
    print( a755.aduna(*lista))
else:
    print('Sistemul de operare trebuie sa fie Win')
    sys.exit()

