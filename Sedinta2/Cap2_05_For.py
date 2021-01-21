# 205 For
# Utilizarea buclei for
# PF - 06/10/2017 v3

# Tipareste caracterele unui sir si le numara
sir = input ( 'Scrie un sir :' )
print ( 'Sirul tau este: ', sir )

count = 0
for car in sir:
    print (car, end = ', ' )
    count += 1
print ( '\nSirul ales are: ', count, 'caractere!' )


# Numara apartiile unui caracter ... pana la un moment indicat
sir = 'Teleenciclopedia'
count = 0
len1 = -1
for lit in sir:
    len1 += 1					# "tine minte"	indexul caracterului
    if lit == 'e':
        count += 1				# numara apartitiile caracterului dat
    if count == 3:
        print('Indexul este: ', len1)	# daca, count ajunge la 3 returneaza
        break							# indexul caracterului si iese din bucla
print ( count )

# Numara cuvintele dintr-un sir

sir1 = input('Introduceti sirul: ')
count = 0
for i in sir1.split():      # split transforma sirul intr-o lista de cuvinte
    count+=1
    print(i, end = '*')
print('\nAm gasit', count, 'cuvinte')

input ( '\n\nApasa <enter> pt a iesi.' )

