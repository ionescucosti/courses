# Program generare grafic pygal
# Explica functiile pygal	DE REVIZUIT
# CP - 1/26/13

import pygal

bar_chart = pygal.Bar()
bar_chart.add('Vineri', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.render_to_file('grafic1.svg') 

input("\n\nApasa <enter> pt a iesi.")
