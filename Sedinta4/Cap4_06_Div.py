# 406 Functii
# Functii - argumente multiple
# PF 	10/08/2016

# 01 crearea unei functii cu numar variabil de parametri *args   si   **kwargs

def exemplu(*args):  				# *args - permite un numar variabil de parametri
    """Functia aduna mai multe numere primite ca argument.
	Returneaza suma si lista numerelor"""
    suma = 0
    lista = []

    for i in args:
        if type(i) == int:
            suma += i
            lista.append(i)
    if lista == []:
        return 'Nu ai introdus numere'
    else:
        return 'Suma numerelor este: ' + str(lista) + ' este ' + str(suma)


exemplu(1, 2, 5, 6, 8)
exemplu('a', 'b', 'c')
exemplu(1, 'a', '9', 100)
ln = [5, 10, 25, 117]

exemplu(*ln)

# 02 Exemplul 2

def fructe(*args):
    for count, fruct in enumerate(args):  			# enumerate aloca index incepand cu zero
        print(count+1, fruct)		# count va fi dat de enumerate, fruct de parametri

fructe('alune', 'caise', 'coacaze', 'prune')

lf = ['alune', 'caise', 'coacaze', 'prune']

fructe(*lf)

# 3 Exemplul 3

def pers(nume, *args, **kwargs):  		# *args - parametri multipli  -->  tuplu
    print(nume)  					# **kwargs - paramatri multipli de tip key = values --> dict
    print( '*-------*-------*' )
    if args:  							# daca avem argumente multiple tip tuplu
        print(args)
    print( '*------- * ------- *' )
    if kwargs:  						# daca avem argumente multiple key = value
        print(kwargs)

try:
    pers()						# Apelare fara parametrul obligatoriu nume
except:
    print ('Nu ati introdus numele')

pers("Vasile")							# Apelare doar cu nume

pers("Georgiana", "alt fruct", 'fata blonda', 'ochi albastri', 'necasatorita' )	# Apelare cu nume si argumente tuplu

pers("Marcel", 'barbat brunet', 'ochi negri', 'necasatorit', salariu=100000, masini=3, case=2) # Completa

l = ['bruneta', 'ochi negri', 'necasatorita']
d = {'salariu':100000, 'masini':3}

print(d)

pers('Corina',*l, **d)

def ceva (*y, **x ):
    s = 0
    for elem in y:
        s+= elem
    for k in x:
        print(k, x[k])
    return s

ceva(1, 7, 87, vasile = 'ion', george = 'cristi')
