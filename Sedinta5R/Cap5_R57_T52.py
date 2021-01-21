# Tema 52
# Demonstreaza utilizarea clasei si a metodelor
# PF - v 21/09/2017

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
"""  #


class PythonClass:
    """clasa mea"""
    catalog_clasa = {}  # initializam dictionarul cu catalogul clasei

    def __init__(self, nume):  # metoda init
        """Initializeza nume student si catalog student"""
        self.nume = nume  # La crearea instantei student ii atribuim nume
        self.catalog = []  # Initializam catalogul individual al fiecarui student

    def mNota(self, nota):  # metoda atribuire note
        """Atribuim nota obtinuta, populam cataloagele"""
        self.nota = nota
        self.catalog.append(self.nota)  # nota in catalog student
        PythonClass.catalog_clasa[self.nume] = self.catalog  # nota in catalog clasa

    def __str__(self):
        """Listeaza catalogul studentului, media obtinuta si catalogul clasei"""
        media = float(sum(self.catalog)) / len(self.catalog)  # media studentului
        mc = 0  # media clasei
        count = 0  # numara studentii
        sumac = 0  # suma tuturor notelor
        for item in PythonClass.catalog_clasa:
            for val in PythonClass.catalog_clasa[item]:
                sumac += val
                count += 1
        mc = sumac / count

        return 'Notele pentru {0} sunt: {1}\n {0} a obtinut media: {2:.2f}\n ' \
               'Catalogul clasei este: {3}\n Media clasei este: {4:.2f}'. \
            format(str(self.nume), str(self.catalog), media, str(PythonClass.catalog_clasa), mc)


George = PythonClass('George')
Dorel = PythonClass('Dorel')
Corina = PythonClass('Corina')

George.mNota(89)
Dorel.mNota(78.28)
Corina.mNota(99.07)

print(George.catalog)

print(George)

George.mNota(92)
George.mNota(76)
Dorel.mNota(87.13)
Corina.mNota(95.78)
Corina.mNota(100.00)
Corina.mNota(89)

print(Corina.catalog)

print(Corina)

print(PythonClass.catalog_clasa)  # catalogul clasei poate fi redat in mai multe moduri
print(George.catalog_clasa)

for item in PythonClass.catalog_clasa:  # putem prelucra datele
    print(item)  # pt fiecare student
    for i in PythonClass.catalog_clasa[item]:
        print('{:.2f}'.format(i).rjust(10))  # notele format float cu 2 zecimale si aliniate
