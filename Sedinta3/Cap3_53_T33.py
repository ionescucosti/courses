# Progam dictionar-lista de cumparaturi
# Introduce elem in dictionar
# Paul Fratila - 2015-12-27

"""
    Creati un program cu o lista de CD/DVD-uri utilizand dictionare si liste.
    Va imita lista de cumparaturi prezentata in curs ca si facilitati
(afisare, adaugare, stergere element, stergere dictionar, cautare, modificare, iesire din program).
    Afisarea dictionarului se va face de forma: key => Value.
    Folositi chei numerice incepand de la 1, iar valoarea intrarii trebuie sa fie
introdusa de utilizator de la tastatura din meniul adaugare.
    Value va fi o lista care sa contina urmatoarele elemente introduse de utilizator:
        Titlu   	 sir de caractere
        Continut  	sir de caractere
    La adaugarea unei intrari noi in dictionar sa se caute urmatoarea cheie libera (incrementare).
    Dupa fiecare intrare in dictionar afisati fiecare element al listei stocate pe cate un rand.
    Pe langa facilitatile indicate mai sus (adaugare, stergere, afisare, iesire din program)
adaugati posibilitatea de a cauta o intrare dupa un sir de caractere, dupa Titlu
si Continut (in acelasi timp implementat prin  or  ). Listare titlu si continut sau inexistent.
""" #

dict = {}
k=0
while True:
    title = input('Introduceti Titlul: ')
    content = input('Intorduceti continut: ')
    k+=1
    dict[k]=[title,content]
    print('Titlu: ',dict[k][0], '\nContinut: ', dict[k][0])

    next=input('enter next? y/n: press enter for y, press n for no \n')
    if next=='n':
        break
print(dict)

c1=input('enter word1: ')
c2=input('enter word2: ')
for i in dict.values():
    if i[0]==c1 or i[1]==c2:
        print('Titlu: ', i[0], '\nContinut: ', i[1])
    else:
        print('Listare titlu si continut sau inexistent')