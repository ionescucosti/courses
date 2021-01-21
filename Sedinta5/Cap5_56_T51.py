# Tema 51
# Demonstreaza utilizarea claselor
# PF - 28/11/2016

'''
 Creati o clasa ce va reprezenta un catalog:
    La initializare trebuie sa oferim doi parametrii de intrare:  nume si prenume
 Creati o metoda care afiseaza absente implementat cu __str__
 Creati o metoda care incrementeaza cu 1 nr. de absente
 Creati o metoda care sterge un numar de absente dat(exclusiv un numar - verifica)
  (pentru cazurile in care avem o scutire medicala) fara a deveni numar negativ

 Creati 1 student numit (alege nume)
 Aplicati de 3 ori prin metoda pentru incrementare absente
 Stergeti doua absente prin metoda specificata

 Creati al doilea student numit (alege alt nume)
 Aplicati de 4 ori metoda pentru incrementare absente
 Stergeti doua absente prin metoda specificata

 Afisati absentele fiecarui student
''' #
class Catalog():
    Absente = 0

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume

    def __str__(self):
        return self.nume+' '+self.prenume+': '+str(self.Absente)

    def absenteaza(self,nr=1):
        self.Absente += nr
        print('Absenta de',nr,'ori!')

    def motiveazaAbsente(self, nr=1):
        if nr <= self.Absente:
            self.Absente -= nr
            print('Au fost motivate ',nr,'absente. Nr. actual absente: ',self.Absente)
        else:
            self.Absente = 0
            print('Nr. actual absente este mai mic. Toate absentele au fost motivate.')

student1 = Catalog('Ionescu','Gica')
student1.absenteaza()
student1.absenteaza(2)
student1.motiveazaAbsente()
student1.motiveazaAbsente(1)
print(student1)
