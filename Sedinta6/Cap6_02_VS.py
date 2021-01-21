# Ex 602
# Atribut obiect - 'self' versus atribut propriu instanta versus atribut clasa
# InfoAcademy PF 2016-05-27

class Clasa:
    """Atribut clasa / atribut obiect"""
    atribut_clasa = 0

    def __init__(self, atribut_instanta = 1):
        self.atribut_instanta = atribut_instanta
                   # valoare default a atributului la crearea instantei

    # Cream trei instante, preiau atribut_instanta de la clasa. Listam atributele fiecarei instante

cont1 = Clasa('a')
cont2 = Clasa('b')
cont3 = Clasa('c')

print('Nume cont 1: ', cont1.atribut_instanta)
print('Nume cont 2: ', cont2.atribut_instanta)
print('Nume cont 3: ', cont3.atribut_instanta)

# Modificam atributele instantelor. Listam noile atribute

cont1.atribut_instanta = 10  # atribuire de valori proprii instantelor
cont2.atribut_instanta = 20
cont3.atribut_instanta = 30

print('atribut_instanta cont 1: ', cont1.atribut_instanta)
print('atribut_instanta cont 2: ', cont2.atribut_instanta)
print('atribut_instanta cont 3: ', cont3.atribut_instanta)

# Incercarea de a utiliza o variabila de clasa cu acelasi nume genereaza o eroare

print(Clasa.atribut_instanta)

print(cont1.atribut_instanta)

print(cont1.atribut_clasa)

print(cont2.atribut_clasa)

cont1.atribut_clasa = 77

Clasa.atribut_clasa

cont1.atribut_clasa