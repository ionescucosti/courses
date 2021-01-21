# Ex 617
# Polymorfism
# InfoAcademy PF 2017-09-27

s = 'maimuta'
t = (1, 2, 3, 5, 8)
x = [1, 2, [9, 8, 7], {'find': 'cauta', 'home': 'acasa', 'dog': 'caine'}, 3, 4, 5, 6]

len ( s )
len ( t )
len ( x )

class Telefoane:
    def __init__(self, name):
        self.name = name

    def camera(self, mpixeli):
        raise NotImplementedError("Metoda abstracta - se defineste in subclasa")

    def ecran(self, diagonala):
        raise NotImplementedError("Metoda abstracta - se defineste in subclasa")


class Telefon_clasic(Telefoane):
    def camera(self, mpixeli):
        self.mpixeli = mpixeli
        return str(mpixeli)

    def ecran(self, diagonala):
        self.diagonala = diagonala
        return str(diagonala)


class Smartfon(Telefoane):
    def camera(self, mpixeli):
        self.mpixeli = mpixeli
        return str(mpixeli)

    def ecran(self, diagonala):
        self.diagonala = diagonala
        return str(diagonala)


i7 = Smartfon('Iphone7')

i7.camera(13)
i7.ecran(5)

n101 = Telefon_clasic('Nokia 101')

n101.camera(2)

n101.ecran(2)

for tel in (i7, n101):
    print('Model: {0} |Camera: {1} mpx |Ecran {2} inch'.format(tel.name, tel.mpixeli, tel.diagonala))