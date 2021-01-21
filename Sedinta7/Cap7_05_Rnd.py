# Ex 705
# Modulul random
# InfoAcademy PF 2016-05-27

import random

random.choice ( 'Astazi e ziua ta' )  		# alege un caracter aleator

random.randrange (3, 1000, 5)  			# numar aleator intreg intre [0-1000), pass 5

random.random () * 100  					# numar aleator intre [0.0-1.0)

# inmultit cu un numar schimba plaja de numere [0.0-100.0)

random.randrange (100)  					# numar aleator intreg intre [1-100)

random.randint(999,1000)                  # numar aleator intreg intre 999 - 1000, inclusiv

help(random)