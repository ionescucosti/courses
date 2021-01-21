# Ex 601
# Variabila statica (de clasa)
# InfoAcademy PF 2016-05-27

class Clasa:                            # cream clasa
	"""'Aceasta clasa are o variabila proprie,
	 variabila statica, sau variabila de clasa"""
	NrConturi = 0  						# variabila de clasa (statica). Nu i se pot aplica metodele.
										# Numara cate conturi sunt deschise
	def __init__(self):
		Clasa.NrConturi += 1  			# apelare! nume_clasa.variabila


cont_paul = Clasa ( )  					# obiect - instantiere

print ( Clasa.NrConturi ) 				# apelarea variabilei se poate face prin nume clasa sau nume instanta

print ( cont_paul.NrConturi )

cont_maria = Clasa ( )                  # obiect - instantiere

print ( cont_maria.NrConturi )

input("Apasa ENTER pentru a iesi: ")

