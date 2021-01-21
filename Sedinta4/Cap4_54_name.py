# 454 Functions
# Exercitii functii - name
# PF 170913

'''
I. Creati o functie, care sa primeasca ca parametri first_name, last_name, middle_name
(initiala tatalui) si sa returneze full_name. 
Atentie:
- middle_name poate sa lipseasca;
- asigurati-va ca numele incep cu litere mari, indiferente cum sunt introdusi parametri;
Hint: folositi parametru cu valoare default si if

II. Creati o functie care sa faca operatiunea inversa, sa primeasca fullname si sa
returneze first_name, last_name, middle_name.
Atentie:
- middle_name poate sa lipseasca;
- asigurati-va ca numele incep cu litere mari, indiferente cum sunt introdusi parametri;
Hint: folositi split intr-un sir si liste
'''#

def fullname(first_name, last_name,*middle):
    fname = first_name.capitalize()
    lname = last_name.capitalize()
    m =''
    if len(middle)>0:
        m=str(middle[0]).capitalize()

    print(fname,lname,m)

fullname('ionescu','constantin','gh')
fullname('ionescu','constantin')

def numeprenumemiddle(fullname):
    n=str(fullname).split()
    nume=n[0].capitalize()
    prenume=n[1].capitalize()
    middle=''
    if len(n)>2:
        middle=n[2].capitalize()

    print(nume,prenume,middle)

numeprenumemiddle('IONESCU CONSTANTIN')
numeprenumemiddle('ionescu constantin gh')


