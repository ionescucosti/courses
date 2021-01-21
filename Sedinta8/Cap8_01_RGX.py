# Ex 801
# RegEx
# InfoAcademy PF 2016-05-27

# Cautare in text cu RE     https://docs.python.org/3.5/library/re.html

# Caractere utilizate in REGEX
"""
- ^   de la inceputul liniei (sinonim \A),
- .   inlocuieste orice caracter
- \d  orice caracter decimal
- \D  orice caracter nondecimal (opusul \d)
- \w  orice caracter alfanumeric
- \W  orice caracter nonalfanumeric
- *   repeta de zero sau mai multe ori expresia de dinainte de semn
- *?  repeta un caracter de 0 sau 1 data (non-greedy - pana la prima aparitie a car de sfarsit)
- \S  fara spatii
- \s  spatiu
- ?  repeta un caracter O DATA sau de mai multe ori (non-greedy - pana la prima aparitie a car de sfarsit)
- +   odata sau de mai multe ori expresia dinainte de semn
- $   sfarsitul liniei (sinonim \Z)
- [aeiou]     un singur caracter din lista
- [^xyz]      un singur caracter cu exceptia celor mentionate
- [0-9]     oricare cifre din interval una cate una (cu + scoate si grupuri)
- [a-z]       oricare litere din interval una cate una (cu + scoate si grupuri)
- (   unde incepe expresia
- )   unde se termina expresia
- [...]       orice caracter intre paranteze
- [^...]      un singur caracter fara paranteze
- {n}         exact n aparitii ale expresiei de dinainte, cu {n'} n sau mai multe
- {n,m}       intre n si m aparitii
- |           desparte mai multe secvente de cautare in aceeasi expresie
"""                                     # Caractere utilizate in REGEX

import re

# Cautare in text fara RE - cauta in linie, toate liniile care contin From

fisier = open('c:/wt/text1.txt')

for line in fisier:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print(line)

# Cautare in text cu re.search() - cauta in linie, toate liniile care contin From

fisier = open('c:/wt/text1.txt')

for line in fisier:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)

# Cautare in text fara RE - de la inceputul liniei - cauta in linie, toate liniile incep cu From

fisier = open('c:/wt/text1.txt')

for line in fisier:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

# Cautare in text cu RE - de la inceputul liniei - cauta in linie, toate liniile incep cu From

fisier = open('c:/wt/text1.txt')
for line in fisier:
    line = line.rstrip()
    if re.search('^From: ', line):       # re.search() - > adevarat sau fals
        print(line)

# re.findall()

a = '''Astazi sunt 22 grade celsius dimineata 32 la pranz si 30 seara.\n
    La noapte vor fi doar 20 grade.'''
b = re.findall('[0-9]+', a)       # returneaza toate aparitiile intr-o lista

# fara plus returneaza cifra cu cifra
print(b)

# sau
print(re.findall('\d+', a))

# cauta la stanga si la dreapta unui caracter de la spatiu pana la caracterul mentionat (@)
# si iarasi pana la spatiu intr-o lista  (toate aparitiile)

c = 'Adresa mea de email este paul@infoacademy.net sau paul@fratila.ro si numarul de telefon...'
d = re.findall('\S+@\S+', c)
e = re.findall(('t' + '[a-z]' + 'e'),  c)   # returneaza cuv care incep cu t si se termina cu n
e = re.findall('\s([t][a-z]*n)\s', fisier.read())
fisier = open('c:/wt/text1.txt')

print(d)
print(e)

# cauta la stanga si la dreapta unui caracter de la spatiu pana la caracter
# si iarasi pana la spatiu intr-o lista

c = 'Email: paul@infoacademy.net si numarul de telefon...'
d = re.findall('^Email: (\S+@\S+)', c)  # returneaza doar ce e in paranteze (patern), nu si 'Email: '

print(d)

# utilizarea slicing cu find

c = 'Email: paul@infoacademy.net si numarul de telefon ...'
domain_name = 'www.' + c[c.find('@') + 1 : c.find(' ', c.find('@'))]

c.find('@') # --> 11
c.find('@') + 1  # --> 12
c.find(' ', c.find('@'))    #  --> c.find(' ', 11)  --> 27
c[c.find('@') + 1 : c.find(' ', c.find('@')) ]       # --> c[12:27

# cauta @, plus o pozitie ca pozitie de inceput;
# cauta spatiul, dupa @, ca poz de sfarsit fara sa fie preluata

print(domain_name)

# dublu split fara REGEX

c = 'Email: paul@infoacademy.net si numarul de telefon ...'
cuvant = c.split()  # split sir in cuvinte
email = cuvant[1]
componente = email.split('@')  # split email in host si domeniu

z = cuvant[1].split('@')

print(componente[0], ',', 'www.' + componente[1])


# acelasi lucru facut cu REGEX pentru domeniu

c = 'Email: paul@infoacademy.net si numarul de telefon ...'
e = re.findall('@([^ ]*)', c)  # cauta toate caracterele dupa @ pana la spatiu, fara acesta

print('www.' + e[0])

# acelasi lucru facut cu REGEX pentru domeniu - alta varianta

c = 'Email: paul@infoacademy.net, paul@fratila.ro si numarul de telefon ...'
e = re.findall('^Email: .*@([^ ]*)', c)

# cauta toate caracterele de la inceput pana la spatiu, toate pana la @ dupa care returnezaza pana la spatiu, fara acesta

print('www.' + e[0])

# sau

c = 'Email: paul@infoacademy.net si numarul de telefon ...'
e = re.findall('^Email: .+@(\S+\.\S+)', c)

print('www.' + e[0])

# extrage numere rationale

fis = open('c:/wt/text1.txt')

rez_list = []

for line in fis:
    line = line.rstrip()
    extrage = re.findall('^X-DSPAM-Confidence: ([0-9]+\.{1}[0-9]*)', line)
    # punctul are sens de virgula aici (toate cifrele inclusiv dupa virgula)

    if len(extrage) != 1:
        continue
    numar = float(extrage[0])
    rez_list.append(numar)

print('Maxim:', max(rez_list))
print(rez_list)

# extrage numere rationale cu escape character

k = 'Avem de incasat $25.0, $3.258 de la clienti'

l = re.findall('\$[0-9.]+', k)  # \$ - caracterul $ nu semnificatia acestuia din REGEX

print(l, l[0])

# Extrage pana la primul caracter ":". Daca scoatem ? - pana la ultimul

x = 'From: Using the : character'

print(re.findall('^F.+?:', x))

# Extragere numere dintr-un text / suma lor

y = open('c:/wt/regex.txt')

counting = 0
big_list = []

for line in y:
    line = line.rstrip()            # scoate spatiile dintre liniile returnate
    z = re.findall('[0-9]+', line)
    big_list += z
    if z:
        for i in z:
            counting += int(i)

print(counting)
print(big_list)

# Split - regex - list

y = open('c:/wt/regex.txt')
l = []
for line in y:
    line = line.rstrip()
    z = re.split('[\s]+', line)
    l += z

print(l)

# re.sub

sir = 'Acasa este soare'
x = re.sub('^A.*?\s', 'Astazi vom sti daca ', sir)

print(x)
