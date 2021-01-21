# Ex 605
# Validarea atributelor de intrare ale unui obiect - update
# InfoAcademy PF 2016-05-27

class People:
	"""Atribut clasa / atribut obiect - continuare"""
	AnStudiu = {'Anul 1', 'Anul 2', 'Anul 3', 'Anul 4', 'Anul 5'}  		# ani de studiu
	Facultate = {'Inginerie', 'Drept', 'Finante', 'Geografie'}  		# specializari

	def __init__(self, nume, anul, studii):
		self.nume = nume
		self.anul = anul
		self.studii = studii

	def __str__(self):
		self.verif_anul = 0  			# inainte de toate reinitializam varibilele de verificare !!!
		self.verif_studii = 0
		if self.anul in People.AnStudiu:  		# verificam anul de studii
			self.verif_anul = 1
		if self.studii in People.Facultate:  	# verificam facultatea
			self.verif_studii = 1
		if self.verif_anul == 1 and self.verif_studii == 1:
			return self.nume + " este in " + self.anul + ' la ' + self.studii + '.'
		else:
			return self.nume + ' nu este studentul nostru.'

			# Dorel

Dorel = People ( 'Dorel', 'Finante', 'Anul 3' )
print ( Dorel )

# Dorel vrea sa pacaleasca sistemul...si NU poate

Dorel.verif_anul = 1
Dorel.verif_studii = 1
print ( Dorel )