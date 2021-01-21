# 501 Clase
# Clase
# PF - 30/11/2016

""" ***-***  A - Clasa - Metoda ***-*** """ #


class Biciclete:					    # Numele clasei
    """Creaza clasa biciclete"""		# Docstring

    def nr_viteze(self, viteze):         # Metoda de adaugare atribut
        """Seteaza numar viteze"""
        self.viteze = viteze

    def listeaza(self):
        print('Bicicleta are', self.viteze)

Pegas = Biciclete()			# cream o instanta, un obiect
Cross = Biciclete()			# cream o instanta, un obiect

Pegas.nr_viteze(3)			# aplicam metoda oricarei instante
Cross.nr_viteze(27)		    # aplicam metoda oricarei instante

Biciclete.__doc__
Biciclete.nr_viteze.__doc__

dir(Biciclete)

print(Pegas.viteze)
print(Cross.viteze)

""" ***-***  B - Clasa - Metoda - Atribut - Parametri default  ***-*** """ #

class Biciclete:					    # Numele clasei
    """Creaza clasa biciclete"""		# Docstring

    def nr_viteze(self, viteze = 1):     # Metoda de adaugare atribut cu parametri default
        """Seteaza numar viteze"""
        self.viteze = viteze

    def provenienta(self, p='Romania'):
        """Seteaza tara provenienta"""
        self.p = p

Pegas = Biciclete()			# cream o instanta, un obiect
Cross = Biciclete()			# cream o instanta, un obiect

Pegas. nr_viteze(3)			# aplicam metoda oricarei instante
Cross. nr_viteze()		# aplicam metoda oricarei instante

Pegas.viteze                 # chiar daca am modificat clasa instanteele sunt mentinute
Cross.viteze                 # metodele vor functiona diferit, daca sunt modificate

Carpati = Biciclete()       #

Carpati.nr_viteze()
Carpati.provenienta()

Carpati.p
Carpati.viteze

Cross.provenienta('Turcia')

Cross.p


""" ***-***  C - Metode speciale   ***-*** """ #

class Biciclete:					    # Numele clasei
    """Creaza clasa biciclete"""		# Docstring

    def __init__(self, nume, culoare='neagra'):
        """Metoda constructor"""
        self.nume = nume  # culoare are valoare default
        self.culoare = culoare

    def __str__(self):
        """ Afiseaza starea obiectului """
        return "Bicicleta: ({0}, culoare: {1}, viteze: {2}, prov: {3})"\
            .format(self.nume, self.culoare, self.viteze, self.p)

    def __del__(self):
        """Sterge obiecte"""
        print('Stergerea a fost efectuata.')

    def nr_viteze(self, viteze = 1):     # Metoda de adaugare atribut cu parametri default
        """Seteaza numar viteze"""
        self.viteze = viteze

    def provenienta(self, p='Romania'):
        """Seteaza tara provenienta"""
        self.p = p

Pegas = Biciclete('Pegas', 'alb')	# cream o instanta, un obiect
Pegas. nr_viteze(3)
Pegas.provenienta()

Cross = Biciclete('Cross')			# preia culoarea default, neagra
Cross.nr_viteze(27)
Cross.provenienta('Germania')

Carpati = Biciclete('Carpati', 'verde')
Carpati.nr_viteze()                 # preia default viteze si provenienta
Carpati.provenienta()

print( Pegas ); print( Cross ); print( Carpati )

del (Pegas)

print( Pegas )