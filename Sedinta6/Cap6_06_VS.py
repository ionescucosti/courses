# Ex 606
# 'self' / NumeClasa
# InfoAcademy PF 2016-05-27

class Auto:
	"""Atribut clasa / atribut obiect - continuare"""
	Culoare = 'Alb'
	Model = 'Berlina'

	# in interiorul clasei putem folosi atat self cat si numele clasei pentru a returna variabilele statice
	def __init__(self):
		print ( 'primeste culoarea la creare: ' + self.Culoare )
		print ( 'primeste atribut model la creare: ' + Auto.Model )

MasinaMea = Auto()  				# cream instanta

# in exterior putem apela VS atat cu NumeClasa.VS cat si cu NumeInstanta.VS
print ( Auto.Culoare )

print ( MasinaMea.Culoare )

MasinaMea.Culoare = 'Verde'  		# Putem sa-i atribuim o culoare proprie

