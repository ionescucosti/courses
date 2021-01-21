# 201 Manipularea sirurilor de caractere
# Metode de manipulare
# PF - 06/10/2017 v3

var1 = 'Astazi e ziua ta'

print ( var1.upper ( ) )    # doar litere mari
print ( var1.lower ( ) )    # doar litere mici
print ( var1.title ( ) )    # prima litera a fiecarui cuvant litera mare

u = var1.upper ( )
print ( u.isupper ( ) )         # testeaza daca contine doar litere mari

l = var1.lower ( )
print ( l.islower ( ) )         # testeaza contine doar litere mici

print ( var1.isalpha ( ) )      # contine si spatii
r = var1.replace ( ' ', '' )
print ( r.isalpha ( ) )         # testeaza contine doar car alpha

print ( var1.split () )        # returneaza o lista cu elementele separate de subsirul ales (spatiu aici)

print ( var1.find ( 'ta' ) )    # Arata pozitia primei aparitii a subsirului
print ( var1.find ( 'ta', 4 ) ) # Arata pozitia primei aparitii a subsirului dupa caracterul cu indexul 7

print ( var1.find ( 'e' ) )

print ( var1 )                  # sirul initial ramane NEMODIFICAT

var2 = 'papadoupulus'

print ( var2.capitalize ( ) )

var2.capitalize ( ).replace ( 'padoupulu', 'ri' )

print (_, "este capitala Frantei!")     # folosin variabila temporara '_'

print ( var1.center ( 40 ), '!' )  # centreaza sirul completand cu spatii pana la 25 de caractere

# ljust si rjust aliniaza la stanga si dreapta

print ( var1.count ( 'ta' ) )   # numara de cate ori apare subsirul 'ta'

print ( var1.join ( '*-*' ) )  # scrie sirul intre caracterele date

print ( ' '.join ( ['Astazi', 'va', 'fi', 'soare'] ) )  # scrie elementele listei despartite de sirul dat, fara capete

print ( var2 )

var3 = '1234560'

var3.isdigit ( )  # testeaza contine doar car numerice
# sau
var3.isnumeric()

var4 = 'A501'
var4.isdigit ( )

var4.isalnum ( )  # testeaza contine car alphanumerice

var5 = '   '

var5.isspace ( )

# formatarea stringurilor
x,y,z = 10,20,30

'{0}, {1}, {2}'.format ( 'x', 'y', 'z' )     # pozitia 0 - 2 coincide cu pozitia din format

'{2}, {2}, {0}, {1}, {0}'.format ( z, y, x ) # pozitia din format va da valorile. Atentie ordine diferita

'{3}{1}{0}'.format ( *'gxyz' )               # face split la sir

'{0}{1}{1}'.format ( 'Tra', ', la' )         # putem repeta sirul

# formatarea stringurilor, argumente cu nume:

print('Produsul: {prod}, \ncantitate: {cant}, \npret: {pret}'.
      format (  cant=100 * 2, pret=5, prod='cirese' ))

# formatarea stringurilor alinierea textului:

"{:<10}".format ('stanga')      # completeaza spatii pana la 20 de caractere si aliniaza stanga

"{:->20}".format ('dreapta')

"{:^19}".format ('centrat')

"Textul este {:*^19}".format ('centrat')    # centrarea si inlocuirea completarea cu caracterul *

# formatarea stringurilor - float cu nr de zecimale implicit sau setat de utilizator

'{: f}'.format ( 15 )           # nr de zecimale implicit

'{:.2f}'.format ( 15 )          # “ .2 “ face ca numarul de zecimale returnat sa fie 2

# formatarea stringurilor - baze de numeratie

# cum reprezentati un numar din baza 10 in alte baze de numeratie?
print("int: {0:d};  hex: {1:x};  oct: {2:o};  bin: {3:b}".format ( 99, 255, 8, 255 ))
# sau cu reprezentarea specifica
print("int: {0:d};  hex: {1:#x};  oct: {2:#o};  bin: {3:#b}".format ( 100, 255, 63, 4 ))

# formatarea stringurilor cu separator grupe de cifre:

'{:,}'.format ( 35735735735 )

# formatarea stringurilor, procente:

raspunsuri_corecte = 17
intrebari_total = 21
print('Nota : {:.2%}'.format ( raspunsuri_corecte / intrebari_total ))

# formatarea stringurilor, completarea cu zpatii sau zerouri:

'{:5d}'.format ( 15 )  # completarea cu spatii, in stanga, pana la lungimea de 5 caractere

'{:05d}'.format ( 15 )  # completarea cu zerouri, in stanga, pana la lungimea de 5 caractere


### Alternativ utilizand metacaracterul "%" ###

# % (procent) este "string formating operator" in exemplele de mai jos

print ( 'Printeaza un numar decimal: %d' % 15987 )      # numar
print ( 'Printeaza un numar float: %f' % 18.999)    # float cu sase zecimale (default)
print ( 'Printeaza un numar float: %.2f' % 18.799)     # float cu numar fix de zecimale
print ( 'Acesta este pentru: %s' % 'sir de caractere' ) # sir de caractere
print ( 'Doar un caracter: %c' % 'x' )                  # un singur caracter
print ( 'Daca vrei hexazecimal: %x' % 255 )        # primmeste decimal returneaza hexa

print ( 'Completeaza spatii la stanga: %5d' % 17)
print ( 'Completeaza spatii la dreapta: %-5d!' % 17)
print ( 'Completeaza zerouri la stanga:%05d' % 17)

pers1 = 'Viorel'
pers2 = "Marinica"
suma1 = 100
suma2 = 50
suma3 = 72.85

print ("Salut %s. Cati bani trebuie sa-mi dai, %d sau %d de lei?"
       % (pers1, suma2, suma1))

print ("Salut %s.  Am sa-ti dau exact %.2f lei."
       % (pers2, suma3))

# Problema: cum putem reprezenta caracterul '%', avand in vedere ca are un alt rol aici?

input ("Apasa <enter> pt a iesi.")


