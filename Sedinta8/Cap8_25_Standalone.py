# 838 StandAlone
# Importul de date dintr-un fisier .csv
# PF 12.01.2017 Cluj


'''
Pasii sunt urmatorii:

- se creaza un fisier setup.py cu un continut ca acesta in acelasi director cu 
hello.py (ar trebui sa fie posibil sa-l creeze automat)
## continut fisier setup.py
from py2exe.distutils_buildexe import py2exe
from distutils.core import setup
setup( console=[{"script": "hello.py"}] )
##
- se ruleaza din linie de comanda: python setup.py py2exe 
(atentie, trebuie sa fie setat path in environment variables, 
altfel se va executa din directorul unde se afla python.exe). 
Rularea va produce un director numit 'dist' care va contine executabilul. 
Acest director contine tot ce-i trebuie ca sa ruleze. Al doilea director creat poate fi sters.

La mine nu NU functioneaza (merge doar pe versiunile 3.3 si 3.4). 

''' #
