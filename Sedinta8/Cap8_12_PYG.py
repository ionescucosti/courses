# Program generare grafic pygal
# Explica functiile pygal
# CP - 1/26/13

import pygal

bar_chart = pygal.Line ( )
bar_chart.no_data_text = "Fara Date"
bar_chart.title = 'Locatie: Bucuresti'
bar_chart.human_readable = True
bar_chart.y_title = 'Elemente masurate'
bar_chart.x_title = 'Timp'
bar_chart.x_labels = ['1','2','3','4','5','6','7','8','9','10','11']
bar_chart.add ( 'Bandwindth-Mbps', [0.5, 7, 1, 0, 0.8, 12, 3, 8, 13, 20, 24] )
bar_chart.add ( 'Latency-ms', [4, 10, 5, 0, 4, 20, 8, 13, 21, 34, 55] )
bar_chart.render_to_file ( 'grafic4.svg' )

input ( "\n\nApasa <enter> pt a iesi." )
