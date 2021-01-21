# 572 Clase
# Clase -  dictionar
# PF - v 21/09/2017

'''
Creati o clasa dictionar, cu urmatoarele metode:
    - init, care atribuie fiecarei instante un dictionar
        (cheia va fi cuvantul, valoarea va fi descrierea)
    - adauga, care va permite adaugarea succesiva de cuvinte. Va avea:
        - input cuvant
        - o conditie de iesire daca am terminat de introdus cuvinte
        - testeaza daca cuvantul introdus exista. Daca exista apeleaza aceeasi metoda: self.adauga()
        - daca nu exista introduce si descrierea
        - il introduce in dictionar
    - modifica, care va permite modificarea succesiva de cuvinte. Va avea:
        - testeaza daca dicfionarul e gol
        - input cuvant
        - o conditie de iesire daca am terminat de modificat cuvinte
        - testeaza daca cuvantul de modificat exista. Daca exista il modifica.
    - cauta, care va permite cautare succesiva de cuvinte. Va avea:
        - testeaza daca dictionarul e gol
        - input cuvant
        - o conditie de iesire daca am terminat de cautat cuvinte
        - testeaza daca cuvantul exista. Daca exista printeaza cheie si valoare.
    - sterge, care va permite stergerea succesiva de cuvinte. Va avea:
        - testeaza daca dictionarul e gol
        - input cuvant
        - o conditie de iesire daca am terminat de sters cuvinte
        - testeaza daca cuvantul exista. Daca exista il sterge.
    - afiseaza, care va permite listarea dictionarului:
        - input cuvant
        - o conditie de iesire daca am terminat de introdus cuvinte
        - testeaza daca cuvantul de modificat exista. Daca exista il modifica.
''' #


class dictionar():

    def __init__(self):
        self.dict_cuv = {}

    def adauga(self):
        while True:
            cuvant = input("Ce cuvant doriti sa adaugati? \
                Introduceti '000' (trei de zero) pentru a iesi: ").lower()
            if cuvant == '000':
                break
            elif self.dict_cuv.get(cuvant):
                print('Cuvant Existent. Adaugati alt cuvant: ')
                self.adauga()       # putem sa apelam propria metoda (recursivitate)
            else:
                descriere = input("Introduceti descrierea: ").lower()
                self.dict_cuv[cuvant] = descriere
                print("Am introdus in dictionar {0} = {1}".format(cuvant, descriere))
                print(self.dict_cuv)

    def modifica(self):
        while self.dict_cuv:
            cuvant = input("Ce cuvant doriti sa modificati? \
                Introduceti '000' pentru a iesi: ").lower()
            if cuvant == '000':
                break
            elif self.dict_cuv.get(cuvant):
                descriere = input("Introduceti noua descriere: ").lower()
                self.dict_cuv[cuvant] = descriere
                print("Am modificat dictionarul: {0} = {1}".format(cuvant, descriere))
                print(self.dict_cuv)
            else:
                print("Cuvantul " + str(cuvant) + " nu exista in dictionar!")

    def cauta(self):
        while self.dict_cuv:
            cuvant = input("Ce cuvant cautati? \
                Introduceti '000' pentru a iesi: ").lower()
            if cuvant == '000':
                break
            if self.dict_cuv.get(cuvant):
                print('Cuvant: {0}, Descriere: {1}'.format(cuvant, self.dict_cuv[cuvant]))
            else:
                print("Cuvantul " + cuvant + " nu exista in dictionar!")


    def sterge(self):
        while self.dict_cuv:
            cuvant = input("Ce cuvant doriti sa stergeti? \
                Introduceti '000' pentru a iesi: ").lower()
            if cuvant == '000':
                break
            if self.dict_cuv.get(cuvant):
                self.dict_cuv.pop(cuvant)
                print('Cuvantul: {0} a fost sters.'.format(cuvant))
            else:
                print("Cuvantul {0} nu exista in dictionar!".format(cuvant))

    def afiseaza(self):
        for i in self.dict_cuv:
            print('Cuvant:', i, "Descriere:", self.dict_cuv[i])


dict_eng = dictionar()
dict_eng.adauga()

dict_eng.cauta()
dict_eng.sterge()

dict_eng.afiseaza()
dict_eng.modifica()

