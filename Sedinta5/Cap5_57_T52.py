# Tema 52
# Demonstreaza utilizarea clasei si a metodelor
# PF - 31/05/2016

"""
 Creati un program cu studentii unei grupe de Python.
 Vom avea un catalog al grupei (dictionar) cu toti studentii si notele obtinute
 (numele va fi cheia, valoarea va fi o lista cuprinzand toate notele unui student)

 Fiecare student va primi un nume la inscrierea in clasa (instantiere) si i se va initializa
 o lista cu catalogul (unde vor fi introduse notele obtinute de studentul respectiv)
  - Vom avea o metoda de atribuire de nota (nota 0-100)
  - Vom avea o metoda de calculare si de listare a mediei pentru fiecare student,
 media clasei, catalogul unui student si catalogul clasei
 Inscrieti in clasa 2-3 studenti, introduceti cateva note pentru fiecare si listati starea fiecaruia
""" #

Catalog = {}

class Student():

    def __init__(self, fullname):
        self.fullname = fullname
        Catalog[self.fullname]= []

    def puneNota(self, nota):
        self.lista = Catalog[self.fullname]
        self.lista.append(nota)

student1 = Student('Gica Ion')
student1.puneNota(80)
student1.puneNota(60)
student2 = Student('Gigi Kent')
student2.puneNota(90)
student2.puneNota(70)

# mediei student,
#  media clasei,
#  catalog student
#  catalogul clasei

ccount=0
ctotal=0
for i in Catalog:
    print(i, ':', end=' ')
    count=0
    total=0
    for m in Catalog[i]:
        print(m,end=' ')
        total += m
        count += 1
    ctotal += total/count
    ccount += 1
    print('Media: ',total/count)
print('Catalog: ',ctotal/ccount)