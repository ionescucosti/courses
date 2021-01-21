# Ex 612
# Metoda privata - variabila privata
# InfoAcademy PF 2016-05-27

class Masina:
    """Testam metoda privata si atributul privat"""

    def culoare_public(self):  # metoda publica
        """O metoda publica poate avea
            argumente publice si private"""
        self.culoare_public = 'publica'  # argument public
        self.__culoare_privata = 'privata'  # argument privat

    def listeaza_culoare(self):
        """O metoda publica poate acceasa
            si argumente private"""
        print(self.__culoare_privata)

    def __listeazaCuloare(self):  # metoda privata
        """O metoda privata poate avea
            argumente publice si private"""
        print(self.culoare_public)  # argument public
        print(self.__culoare_privata)  # argument privat

    def apeleaza(self):
        """O metoda publica poate
            accesa una privata"""
        self.__listeazaCuloare()


obiect_1 = Masina()

# Apelam metoda listeaza_culoare

obiect_1.culoare_public()  # argumentul public este accesibil

obiect_1.__culoare_privata  # argumentul privat nu este accesibil indiferent cum il apelam
obiect_1.culoare_public

obiect_1._Masina__culoare_privata   # putem totusi sa-l apelam prin constructia obiect._Clasa__atributprivat

# nume_instanta._NumeClasa__variabilaPrivata


# Apelam metoda listeaza_culoare

obiect_1.listeaza_culoare()     # de data aceasta atributul privat va fi listat, chiar daca este intr-o metoda publica



# Apelam metoda privata __listeazaCuloare

obiect_1.__listeazaCuloare()    # nu poate fi apelata

obiect_1._Masina__listeazaCuloare()     # putem s-o apelam prin constructia obiect._Clasa__metodaprivata



# Apelam metoda "apeleaza"

obiect_1.apeleaza() # metoda privata accesata printr-o metoda publica

obiect_1.__dict__

dir(obiect_1)