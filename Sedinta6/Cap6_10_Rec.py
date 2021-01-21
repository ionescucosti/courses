# Ex 610
# Clase recursive
# InfoAcademy PF v2017-09-27

from random import randint      # importam functia randint care returneaza un numar intreg aleator dint-un interval

class Banca:
    """Institutie financiara"""
    NrConturi = 0               # numara cate conturi saunt create la un moment dat
    lista_conturi = []          # incrementeaza numarul de conturi disponibile la fiecare instantiere

    def __init__(self, nume_cont):
        '''Numele contului va fi de forma: Cont + 10 cifre'''
        self.nume_cont = nume_cont
        self.sold = 0
        Banca.NrConturi += 1
        Banca.lista_conturi.append(self.nume_cont)

    # cream o metoda care poate crea multiple instante apeland clasa

    def creez_cont(self, Cate):
        for i in range(Cate):
            x = randint(0, 10000000000)
            x = 'Cont' + '%010d' % x
            self.nume_cont = x
            globals()[x] = Banca(x)
            print (x)


Cont1111111111 = Banca('Cont1111111111')  # Cream un cont

print(Banca.NrConturi)

Cont1111111111.creez_cont(10)  # Cream 10 conturi

print(Banca.NrConturi)

# print(Cont3691105262.NrConturi)  # Verificam numarul de conturi create

Banca.lista_conturi

# Cont3691105262.creez_cont(7)

