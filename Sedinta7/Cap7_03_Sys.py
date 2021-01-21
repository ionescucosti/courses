# Ex 703
# Modulul sys
# InfoAcademy PF 2016-05-27

import sys

sys.argv                    # denumirea programului +, +

sys.version                 # versiunea de Python

sys.platform                # platforma pe care e instalat

sys.executable              # calea catre executabilul Python

sys.modules                 # lista cu modulele importate

sys.builtin_module_names    # lista modulelor builtin

l = list()
for i in sys.modules:
    l.append(i)
l.sort()
print(l)

sys.path                    # caile unde cauta module

for i in sys.path:
    print ( i )

sys.path.append('C:\WT')    # adaugam o cale noua

sys.exit()                  # utilizat pentru a iesi din program

