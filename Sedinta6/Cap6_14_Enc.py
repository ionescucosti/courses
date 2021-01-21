# Ex 614
# Metode speciale
# InfoAcademy PF 2016-05-27

class Carte:
    def __init__(self, titlu, autor, pagini):  # "constructor"
        print("O noua carte")
        self.titlu = titlu
        self.autor = autor
        self.pagini = pagini

    def __str__(self):  # printare
        return "Titlu: {0}, Autor: {1}, Pagini: {2} ".format(self.titlu, self.autor, self.pagini)

    def __del__(self):  # destructor
        print("Carte casata")

    def __len__(self):
        return self.pagini


HdC = Carte("Hotul de Carti", "Markus Zusak", 573)
PyInfo = Carte("Curs Python InfoAcademy", "Paul Fratila", 186)

print(HdC)

del PyInfo

len(HdC)

HdC = Carte("Hotul de Carti", "Markus Zusak", 573)  # daca cream o instanta cu acelasi nume va fi stearsa si recreata

