# Ex 808
# pygal
# InfoAcademy PF 2016-05-27

import pygal

ob_chart = pygal.Bar ( )  				# creare obiect - grafic cu bare verticale una langa alta
ob_chart.add ( 'Grafic', [1, 3, 7, 15, 31, 46] )  			# adaugare date
ob_chart.render_to_file ( 'grafic.svg' )  			# salvare fisier grafic

ob_chart.add ( 'Grafic_1', [1, 2, 1, 2, 1, 2, 1] )  		# cu add intercalam alte valori
ob_chart.render_to_file ( 'grafic.svg' )

# adaugam titlu, den axe, dim font
ob_c1 = pygal.StackedLine ( title='Note Python',
							x_title='Capitol',
							y_title='Nota',
							title_font_size=25 )
ob_c1.add ( 'Catalog', [91, 95, 87, 99, 100, 79, 100, 98] )
ob_c1.x_labels = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
ob_c1.render_to_file ( 'catalog.svg' )

ob_c2 = pygal.StackedBar ( )  								# bare verticale una peste alta
ob_c2.add ( 'Vanzari', [1, 3, 2, 4, 3, 5, 4] )
ob_c2.add ( 'Incasari', [1, 2, 3, 4, 5, 6, 7] )
ob_c2.x_labels = ['Lu', 'Ma', 'Mi', 'Jo', 'Vi', 'Sa', 'Du'] # punem etichete valorilor pe axa x
ob_c2.render_to_file ( 'vanzari.svg' )

ob_c3 = pygal.Line  			# puncte unite de linii, linii una langa alta
ob_c4 = pygal.StackedLine ( )  	# puncte unite de linii, linii una peste alta
ob_c5 = pygal.Pie ( )  			# rotund
ob_c6 = pygal.BaseMap ( )
