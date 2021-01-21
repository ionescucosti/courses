# Cap 3 Tema 2
# Introduce elem in lista, o sorteaza
# Paul Fratila - 2015-12-27

"""
 Creati un program cu o lista de cumparaturi utilizand dictionare in loc de liste.                         
 Programul va imita lista de cumparaturi prezentata in curs ca si facilitati (Ex. 306)    
 (adaugare, stergere, afisare, iesire din program).                                        
 Folositi chei numerice incepand de la 1
 Valoarea intrarii trebuie sa fie introdusa de utilizator de la tastatura din meniul adaugare.                              
 Afisarea dictionarului se va face de forma: key => Value                                    
 """ #

cumparaturi = {}

cumparaturi[4]='oua'
cumparaturi[2]='paine'
cumparaturi[1]='lapte'
# print('items: ',cumparaturi.items())
# print('keys: ',cumparaturi.keys())
# print('values',cumparaturi.values(),'\n\n')


print(cumparaturi)
cumparaturi.update({6:'oua',3:'paini',2:'lapte'})
print(cumparaturi)
cumparaturi.pop(2)
cumparaturi.pop(4)
print(cumparaturi)

x=input('apasa Enter pt a iesi: ')
