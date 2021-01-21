# 101 Stringuri
# Stringuri, print, comentarii, concatenare, repetitie, secvente de evadare
# PF - 06/10/2017 v3

# Salut traditional in IT

print('Hello World!')

# folosim ghilimele sau apostroafe. Cand avem de cuprins ceva intre ghilimele folosim celelalt semn

print('Acum "Ghilimelele vor fi listate" ')

# sau folosim \caracter (bacslash face ca ' sa nu aiba semnificatia de inceput/sfarsit de string)

print('Dar si \'Apostroful va fi listat\'')

# Ghilimelele triple (cu print) permit scrierea pe mai multe linii,
# care vor fi vizualizate exact asa cum sunt scrise

print("""Eu nu strivesc corola de minuni a lumii
si nu ucid
cu mintea tainele, ce le-ntalnesc
in calea mea
""")

# putem continua o instructiune print, care contine un string, pe mai multe linii cu  '\' .
# rezultatul va fi vizualizat pe un singur rand (sau randuri coomplete, daca se intinde pe mai multe randduri.
# numarul de caractere recomandat pe un rand fizic este de 79

print('Invat\
 Python!\
Faceti\
 liniste...')

# ";" (semicolon) permite sa scriem mai multe instructiuni pe o linie. Vor fi redate pe linii separate

print('Astazi e ziua ta') ; print("Zi frumoasa ca tine") ; print('Ti-am adus trandafiri')

# virgula ne permite sa afisam diferite expresii, de diferite tipuri, pe acelasi rand

print('Invat Python!','Faceti liniste...',      2 + 4,    'minute')

# Concatenare +

print('Alina' + ' ' + 'viseaza!')

# Multiplicare * ;

print(3 * 'Goool !')
print('Goool !' * 3)

print('Sunati la: 07' + 8 * '3')

# Secvente de evadare

print("\a Bip, bip\a")

print("""\t un tab
\t\t doua tab-uri
\t\t\t trei tab-uri
tab-urile\tpot\tfi\tsi\tin\t\t\tinteriorul\tstringului""")

# formatare simpla utilizand secventele de evadare

print("Paul poate fi contactat la:\n\tTelefon: 0721.259.520\n\te-mail: paul@infoacademy.net\n")

# Urmatoarea instructiune este folosita in programele de tip non grafic
# Are scopul de a opri rularea pana la apasarea tastei enter.
# Atflel va ri rulat si iese automat din consola, fara sa vizualizam executia

input("Apasa tasta <enter> pt a iesi.")




