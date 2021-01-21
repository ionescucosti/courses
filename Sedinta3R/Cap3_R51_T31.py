# R351 Tema 1
# Introduce elem in lista, o sorteaza
# PF - 2015-12-27

'''
Creati un program ce are ca scop sortarea a x elemente, introduse de utilizator de la       
tastatura (input) printr-o bucla while, intr-o lista.                                                            
Elementele vor fi inserate pe rand intr-o lista prin capturare de text.                     
Inserati la inceputul programului numarul de elemente dorit (x) - in afara buclei. 
Atentie la conditia de iesire din bucla (cand au fost introduse x elemente).                          
Afisati lista sortata la final.                                                            
''' #

List = []
Iteratii = 0

#  Cate elemente dorim sa inseram in lista?

nr = input("Tastati nr. de elemente ale listei:\n")
nr = int(nr)

while Iteratii < nr:
    x = input('Introdu un element:')
    List.append(x)
    Iteratii += 1

List.sort()
print(List)

# - # - #  Sau

count = 1
lista = []
cate = int(input('Cate elem? : '))

while cate > 0:
    elem = input('Intro elementul nr {0}: '.format(count))
    lista.append(elem)
    count +=1
    cate -= 1

lista.sort()
print(lista)

input('Apasa <enter> pentru a iesi.')
