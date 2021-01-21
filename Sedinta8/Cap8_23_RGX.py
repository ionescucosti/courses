# Ex 821
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
- [0-9]       oricare cifre din interval una cate una (cu + scoate si grupuri)
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

# punctul si pipe ( | )

la = 'ala ana ama asa ada ela ema eba ena eva'
print(re.search('a.a', la))         # prima aparitie
print(re.findall('a.a', la))        # toate aparitiile a orice caracter a
print(re.findall('e.a',la))         # toate aparitiile e orice caracter e
print(re.findall('e.a|a.a',la))     # toate aparitiile a orice caracter a si e orice caracter e
print(re.search('e.a | a.a',la))    # atentie, spatiul e tratat ca atare
print(re.search('e.a|a.a',la))      # acelasi lucru, fara spatii, alt rezultat

# Metacaracterele ^, $ , \b, \B

print(re.search('^a.a', la))            # care incepe cu
print(re.search('e.a$', la))            # care se termina cu
lb = 'test regex'
print(re.search('^test regex$', lb))   # care contine exact textul

# dog       - care contine dog
# \bdog     - care incepe cu dog
# \bdog\b   - doar cuvantul dog
# \Bdog     - care contine dar nu incepe cu dog

# paranteze drepte - se mapeaza cu unul si doar unul din caracterele dintre paranteze

print(re.findall('e[blmnvx]a',la))

lc = 'CO2 SO4 NaCl K2SO4'
print(re.findall('[CS][O][24]',lc))     # contine trei caractere, cate unul din fiecare multime
# print(re.findall('e[blmnvx]a',lc))      # contine trei caractere, incepe cu e, se termina cu a

# cratima si negatia cu ^

ld = 'a1 a2 a3'
print(re.findall('a[0-9]',ld))      # toate apartitiile a urmat de o singura cifra
print(re.findall('a[^aeiou]a', la)) # toate aparitiile a orice consoana a (fara caracterele mentionate)


sir = """ton, aton, telefon, trianon, ten"""

m = re.findall("\s(t\w+n)", sir)
n = re.findall("(t\w+n)", sir)

print(m)
print(n)

