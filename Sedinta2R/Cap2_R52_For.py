# R252 Bucle for
# For / range
# PF - 06/10/2017 v3

print ( "Numara de la 0 la 5:" )

for i in range ( 6 ):
	print ( i, end = ' ' )		# end permite afisarea pe aceeasi linie
								# cu caracterul mentionat (aici spatiu) intre elemente

print ( "Numara din cinci in cinci pana la 50:" )

for i in range ( 0, 51, 5 ):
	print ( i )


print ( "Numara invers de la 10 la 1:" )

for i in range ( 10, 0, -1 ):
	print ( i )

input ( "Apasa <enter> pt a iesi." )
