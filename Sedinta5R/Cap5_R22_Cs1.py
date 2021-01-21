# 522 Clase
# Clase -  dictionar
# PF - 10/08/2016

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
        - testeaza daca dictionarul e gol
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
        self.dict_cuv ={}

    def adauga(self):
        while True:
            cuvant = input('Introduceti cuvantul:')

            if cuvant == '000':
                break

            if cuvant in self.dict_cuv.keys():
                self.adauga()
            else:
                descriere = input('Introduceti descrierea: ')
                self.dict_cuv[cuvant] = descriere


    def modifica(self):

        if self.dict_cuv != {}:
            while True:
                cuvant = input('Introduceti cuvantul de modificat:')
                if cuvant == '000':
                    break

                if cuvant in self.dict_cuv.keys():
                    self.dict_cuv[cuvant] = input('Introduceti noua descriere: ')
                else:
                    print('Cuvantul nu exista in dictionar')
                    continue
        else:
            print('Dictionarul este gol "M"')


    def cauta(self):

        if self.dict_cuv != {}:
            while True:
                cuvant = input('Introduceti cuvantul cautat:')
                if cuvant == '000':
                    break

                if cuvant in sorted(self.dict_cuv.keys()):
                    print('\n{0}\n{1}'.format(cuvant, self.dict_cuv[cuvant]))
                else:
                    print('Cuvantul nu exista in dictionar "c"')
                    continue
        else:
            print('Dictionarul este gol "C"')

    def sterge(self):

        if self.dict_cuv != {}:
            while True:
                cuvant = input('Introduceti cuvantul de sters:')
                if cuvant == '000':
                    break

                if cuvant in self.dict_cuv.keys():
                    del(self.dict_cuv[cuvant])
                else:
                    print('Cuvantul nu exista in dictionar "s"')
                    continue
        else:
            print('Dictionarul este gol "S"')

    def afiseaza(self):

        if self.dict_cuv != {}:
            for cuv in self.dict_cuv.keys():
                print('\n{0} - {1}'.format(cuv, self.dict_cuv[cuv]))
        else:
            print('dictionar gol')

der = dictionar()

der.adauga()

der.modifica()

der.cauta()

der.sterge()

der.afiseaza()

