# Tema 51
# Demonstreaza utilizarea claselor
# PF - v 21/09/2017

'''
 Creati o clasa ce va reprezenta un catalog:
    La initializare trebuie sa oferim doi parametrii de intrare:  nume si prenume
 Creati o metoda care afiseaza absente implementata cu __str__
 Creati o metoda care incrementeaza cu 1 nr. de absente
 Creati o metoda care sterge un numar de absente dat(exclusiv un numar - verifica)
  (pentru cazurile in care avem o scutire medicala) fara a deveni numar negativ

 Creati 1 student numit (alege nume)
 Aplicati de 3 ori prima metoda, pentru incrementare absente
 Stergeti doua absente prin metoda specificata

 Creati al doilea student numit (alege alt nume)
 Aplicati de 4 ori metoda pentru incrementare absente
 Stergeti doua absente prin metoda specificata

 Afisati absentele fiecarui student
'''  #

class Catalog:
    """catalog absente"""

    def __init__(self, Nume, Prenume):
        """initializeaza atribute"""
        self.Nume = Nume
        self.Prenume = Prenume
        self.absente = 0
        self.email = str(Nume)+str(Prenume)+'@'+'gmail.com'

    def __str__(self):
        """afiseaza nr. de absente"""
        return "Numarul de absente al studentului {0} {1} este {2}. Adresa de email este {3}".format(
            str(self.Nume),
            str(self.Prenume),
            str(self.absente),
            str(self.email))

    def IncrAbs(self):
        """Incrementeaza absente"""
        self.absente += 1

    def StergeAbs(self, nr):
        """Scade din nr actual un numar de absente"""
        if type(nr) is int:
            if self.absente < nr:
                self.absente = 0
            else:
                self.absente = self.absente - nr
        else:
            print("Nu ati introdus un numar\n")


# student1

std1 = Catalog("Popa", "Vasile")
std1.IncrAbs()
std1.IncrAbs()
std1.IncrAbs()
print("Cu scop de verificare! nu a fost solicitat in cerinta\n", std1)

std1.StergeAbs("2")
std1.StergeAbs(2)

# student2

std2 = Catalog("Ilie", "Dragomir")
std2.IncrAbs()
std2.IncrAbs()
std2.IncrAbs()
std2.IncrAbs()

print("Cu scop de verificare! nu a fost solicitat in cerinta\n", std2)

std2.StergeAbs("2")
std2.StergeAbs(2)

# afisare
print(std1)
print(std2)
