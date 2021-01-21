#  R353 Tema 3
#  Introduce elem in lista, o sorteaza - Progam dictionar-lista de cumparaturi
#  Paul Fratila - 2015-12-27

"""
    Creati un program cu o lista de CD/DVD-uri utilizand dictionare si liste.
    Va imita lista de cumparaturi prezentata in curs ca si facilitati
(afisare, adaugare, stergere element, stergere dictionar, cautare, modificare, iesire din program).
    Afisarea dictionarului se va face de forma: key => Value.
    Folositi chei numerice incepand de la 0, iar valoarea intrarii trebuie sa fie
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

from datetime import datetime

datetime.strftime(datetime.now(), 'Azi %d %b %Y %H:%M:%S' )

print("\t\t Dictionar de DVD -uri")

dvdict = {}     # initializam dictionarul
new_key = 1     # initializam cheile dictionarului (prima cheie)
new_val = []    # intializam lista tempoarare utilizata la popularea valorilor in dictionar

while True:
    print("""\nSelecteaza
--------------------------------------------
0 - Pentru afisare dictionar actual
1 - Pentru introducerea unui element nou
2 - Pentru stergerea unui element existent
3 - Pentru stergerea dictionarului
4 - Pentru cautare in dictionar
5 - Pentru modificare element existent
9 - Pentru iesire
--------------------------------------------
""")
    alege = input('Optiunea mea este: ')
    if alege == '0':
        if dvdict != {}:
            for elem in dvdict:
                print(elem, 'Titlu:', dvdict[elem][0], ' Continut:', dvdict[elem][1])
        else:
            print('Dictionarul este gol\n')

    elif alege == '1':
        titlu = input('Introduceti titlul DVD: ')
        continut = input('Introduceti continutul DVD: ')
        new_val.append(titlu)
        new_val.append(continut)
        dvdict.update({new_key: new_val})
        for elem in dvdict:
            print('Element:', elem, ' Titlu:', dvdict[elem][0], ' Continut:', dvdict[elem][1])
        new_val = []
        new_key += 1

    elif alege == '2':
        if dvdict:
            for elem in dvdict:
                print('Element:', elem, ' Titlu:', dvdict[elem][0], ' Continut:', dvdict[elem][1])
            sterge = int(input('Sterge elementul cu cheia: '))
            if sterge in dvdict.keys():
                dvdict.pop(sterge)
                print('Elementul cu cheia', sterge, 'a fost sters.')
            else:
                print('Element inexistent!\n')

        else:
            print('Dictionarul este gol\n')

    elif alege == '3':
        dvdict = {}
        print('Dictionar sters\n')

    elif alege == '4':
        cauta = input('Introduceti textul cautat: ')
        for expr in dvdict.values():
            if cauta in expr[0] or cauta in expr[1]:
                print('Titlul:', expr[0], 'Continut:', expr[1])
            else:
                print ('Textul cautat nu exista.')

    elif alege == '5':
        if dvdict:
            modifica = int(input('Introduceti cheia elementului de modificat: '))
            if modifica in dvdict.keys():
                t, c = input('Introduceti titlul: '), input('Introduceti continutul: ')
                dvdict[modifica] = [t, c]
            else:
                print('Cheia', modifica, 'nu se afla in dictionar.')
        else:
            print('Dictionarul este gol.')

    elif alege == '9':
        print('O zi frumoasa!')
        break

    else:
        print('Nu ai ales o optiune corecta')

input('Apasa <enter> pentru a iesi.')
