# Ex 615
# Mostenirea
# InfoAcademy PF 2016-05-27

class Banca:  						# creem clasa
	"""Institutie financiara"""
	NrConturi = 0

	def __init__(self):  	# metoda constructor - se mosteneste
		self.sold = 0 			# se aplica la crearea fiecarui obiect - se mosteneste
		Banca.NrConturi += 1  		# incrementeaza numarul de conturi disponibile - se mosteneste

	def alim_cont(self, suma):  	# metoda - aplicabila pentru fiecare obiect - se mosteneste
		self.sold += suma
		self.sold_nou ( )

	def extr_cash(self, suma):  	# metoda - aplicabila pentru fiecare obiect - se mosteneste
		self.sold -= suma
		self.sold_nou ( )

	def sold_nou(self):  			# metoda - aplicabila pentru fiecare obiect - se mosteneste
		print ( 'Noul sold este: {:.2f}'.format(self.sold ) )

class CEC(Banca):

	def plata_op(self, suma):  		# metoda proprie a subclasei
		self.sold -= suma
		self.sold_nou ( )

	def desc_cont(self, suma):  	# metoda proprie a subclasei
		self.sold += suma
		self.sold_nou ( )

Cont_Germin = CEC ( )  				# instanta noua subclasa

Cont_Germin.alim_cont ( 20000 )  	# metoda mostenita

Cont_Germin.plata_op ( 1800 )  		# metoda proprie

Cont_Germin.extr_cash ( 1950 )  	# metoda mostenita

Cont_Germin.sold_nou ( )  			# metoda mostenita

Cont_Alina = Banca ( )  			# instanta noua superclasa

Cont_Alina.desc_cont ( 5000 )  		# o instanta a unei superclase nu poate accesa metode proprii subclaselor

Cont_Dorel = CEC()

Banca.NrConturi  					# numar de conturi poate fi apelat de orice instanta, superclasa si subclasa

CEC.NrConturi

Cont_Alina.NrConturi

Cont_Germin.NrConturi
