# Ex 616
# Apelarea unei clase din alta clasa
# InfoAcademy PF 2016-05-27

class A:
    x = 10
    y = "a"

class B(A):
    x = 20

class C(B):
    x = 30

class M(A):
    x = 100

class N(M):     # mostenire ierarhica
    x = 1000

class X(N):     # clasa X mosteneste clasa N, care mosteneste M, care mosteneste A
    pass

obj1 = X()

obj1.x          # instanta va prelua atributul x de la cea mai apropiata, N in acest caz
obj1.y

A.x
B.x

class Y(N, B, A):   # Mostenire multipla
    pass

obj2 =(Y)
obj2.y
obj2.x

Y.x             # instanta va prelua atributul x de la cea mai indepartata, C in acest caz


class jucarii:
    def __init__(self, categorie = '3-5 ani'):
        self.categorie = categorie

class m:
    def __init__(self, pret = 1000):
        self.pret = pret

class papusi(jucarii, m ):
    def __init__(self, nume = 'Barbie'):
        self.nume = nume
        super().__init__()
        #super().__init__(prt)         # in versiunea 2.x utilizam:   super(papusi, self).__init__()


p1 = papusi()
p1.nume
p1.categorie
p1.pret








class jucarii:
    def __init__(self, categorie):
        self.categorie = categorie

class papusi(jucarii):
    def __init__(self, var_mostenita, nume = 'Barbie'):
        self.nume = nume
        super().__init__(var_mostenita)
        #super().__init__(prt)         # in versiunea 2.x utilizam:   super(papusi, self).__init__()


p1 = papusi('Copii mari', 'Aradeanca')
p1.nume
p1.categorie



