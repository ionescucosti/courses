# Ex 603
# Atribut instanta versus atribut clasa
# InfoAcademy PF 2016-05-27


class People:
	"""Atribut clasa / atribut obiect - continuare"""
	NrPeople = 0
	specia = 'Homo Sapiens Sapiens'  			# atribute comune tuturor instantelor

	def __init__(self, nume):
		self.nume = nume  						# atribut specific fiecarei instante dat la creare
		People.NrPeople += 1					# incrementeaza la crearea fiecarei instante


George = People ( 'George' )  					# Adaugam noi instante

Alina = People ( 'Alina' )

print ( People.NrPeople ) 						# Returneaza numarul de instante create

print ( Alina.specia,'-->', Alina.nume )

George.NrPeople = 10  				# Fiecare obiect poate avea o variabila proprie cu acelasi nume ca a clasei

print ( George.NrPeople )

Alina.NrPeople = 20

print ( Alina.NrPeople )

print ( People.NrPeople ) 			# Variabila clasei isi mentine valoarea proprie

Gheorghe = People('Ghe')

Gheorghe.NrPeople