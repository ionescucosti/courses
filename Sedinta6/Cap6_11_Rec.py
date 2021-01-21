# Ex 611
# Apelarea unei clase din alta clasa
# InfoAcademy PF 2016-05-27

class A:
    def aduna(self, a, b):
        return a + b

class B:
    def inmulteste(self, x, y):
        return x * y

bb = B()
aa = A()

print(bb.inmulteste(aa.aduna(3, 7), bb.inmulteste(15,28)))
