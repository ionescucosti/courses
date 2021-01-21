# 405 Try / Except
# Calculeaza maxim si minim pentru numere introduse de la tastatura
# PF 27/05/2016

def maxmin():
	"""Returneaza maximul si minimul pentru numerele introduse. Tasteaza done pentru a iesi"""
	largest = None
	smallest = None
	while True:
		numar = input ( "Enter a number (done pentru a iesi): " )
		if numar == "done":  # iese din bucla daca tastam done
			break
		try:
			num_int = int ( numar ) 	# Raise ValueError
		except ValueError as e:
			print ( 'Invalid input:', e)
			continue

		if largest is None:
			largest = num_int
			if smallest is None:
				smallest = num_int
		else:
			if num_int < smallest:
				smallest = num_int
			if num_int > largest:
				largest = num_int
	print ( "Maximum is", largest, '\nMinimum is', smallest )

maxmin ( )

input(' Apasa ENTER pentru a iesi')