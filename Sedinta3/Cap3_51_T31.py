# Cap 3 tema 1
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

"""1. input - cate elemente dorim sa inseram?
2. initializam o lista;
3. bucla while cu input pentru introducere elemente noi --> adaugare in lista
4. sortare lista (metoda) si printare"""

nr = int(input('cate elemente? '))
list = []
while nr > 0:
    x=input("enter new item: ")
    list.append(x)
    nr-=1
list.sort()
print(list)
