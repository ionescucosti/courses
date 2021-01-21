# Tema 53
# Demonstreaza utilizarea clasei si a metodelor
# PF - v 21/09/2017

'''
 Creati o clasa pentru prelucrare de texte, la initializare trebuie data calea catre fisier
    Creati o metoda pentru scriere
    Creati o metoda pentru citire fisiere
    Creati o metoda care sa faca split in cuvinte
    Creati o metoda care sa numere cate aparitii are un cuvant dat.
    Utilizati metodele create
''' #

class PrelText:
    """Prelucreaza fisierul text"""

    def __init__(self, fisier):
        self.fisier = fisier

    def citeste(self):
        try:
            self.citire = open ( self.fisier, 'r')
        except FileNotFoundError as e:
            print('Fisierul nu poate fi citit', e)
        else:
            for line in self.citire.readlines():
                line = line.rstrip ( )
                print (line)
            self.citire.close ( )

    def scrie(self, text):
        self.text = text
        try:
            self.scriere = open(self.fisier, 'a+')
        except IOError as e:
            print('Fisierul nu poate fi deschis', e)
        else:
            self.scriere.write ( '\n' + self.text )
            self.scriere.close ()

    def dsplit(self):
        self.cit = open ( self.fisier, 'r' )
        lista = []
        for line in self.cit:
            line = line.rstrip ( )
            for cuv in line.split ( ' ' ):
                lista.append ( cuv )
        print (lista)
        self.cit.close ( )

    def cauta(self, cuvant):
        self.cuvant = cuvant
        self.cit = open ( self.fisier, 'r' )
        lista = []
        for line in self.cit:
            line = line.rstrip ( )
            for cuv in line.split ( ' ' ):
                lista.append ( cuv )
        count = 0
        for i in lista:
            if self.cuvant == i:
                count += 1
        print ( 'Cuvantul', self.cuvant, 'are', count, 'aparitii!' )


Romeo = PrelText('C:/WT/romeo.txt')

Romeo.citeste()

Romeo.scrie ( '\n\t\tShakespeare - Romeo si Julieta' )

Romeo.dsplit ( )

Romeo.cauta('Julieta')

Guta = PrelText('c:/wt/guta.txt')

Guta.citeste()

Guta.scrie ( '\nSi vazand el asta treaba \ncalul a-nhamat degraba\n' )

Guta.cauta ( 'Guta' )

Guta.dsplit ( )
