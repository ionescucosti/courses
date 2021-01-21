# Program generare grafic pygal
# Explica functiile pygal
# CP - 1/26/13

"""Test""" #

import pygal

bar_chart = pygal.StackedBar ( )  					# BARE UNELE PESTE ALTELE
lista_finala = [96, 90, 95, 100, 96, 80, 92, 87, 79, 66, 45]

bar_chart.no_data_text = "Fara Date"
bar_chart.title = 'Locatie: Bucuresti'
bar_chart.human_readable = True
bar_chart.y_title = 'Elemente masurate'
bar_chart.x_title = 'Timp'
bar_chart.x_labels = [1,2,3,4,5,6,7,8,9,10,11]
bar_chart.add ( 'Bandw Date-Mbps', lista_finala )
bar_chart.add ( 'Bandw Voce-Mbps', [4, 10, 5, 0, 4, 20, 8, 13, 21, 34, 55] )
bar_chart.render_to_file ( 'grafic5.svg' )

input ( "\n\nApasa <enter> pt a iesi." )
