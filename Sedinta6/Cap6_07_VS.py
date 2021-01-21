# Ex 607
# Valoare variabila instanta / valoare variabila clasa
# InfoAcademy PF 2016-05-27

class Test:
    """Atribut clasa / atribut obiect - continuare"""
    x = 3
    y = 7


ob1 = Test()  # preia atributele definite de clasa
ob2 = Test()

print(ob1.x)
print(ob2.x)

ob1.x = 100  # setam atribut propriu obiectului

print(ob1.x)
print(ob2.x)

Test.x = 30  # schimbam valoarea atributului de clasa

print(ob1.x)  # a ramas cu atributul propriu instantei
print(ob2.x)  # neavand atribut propriu instantei a preluat noul atribut al clasei

print(ob1.y)
print(ob2.y)

Test.y = 70

print(ob1.y)
print(ob2.y)
