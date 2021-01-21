# Program generare grafic pygal
# Explica functiile pygal
# CP - 1/26/13

import pygal

bar_chart = pygal.Bar(title='Locatie: Bucuresti', x_title='Timp',
                      y_title='Elemente masurate', title_font_size=24, human_readable=True)
bar_chart.add('Bandwindth-Kbps',
              [500, 7000, 1000, 0, 800, 12000, 3000, 8000, 13000, 20000, 24000])
bar_chart.add('Latency-ms', [4, 10, 5, 0, 4, 20, 8, 13, 21, 34, 55])
bar_chart.x_labels = [
    '10:15:10',
    '10:20:20',
    '10:30:30',
    '10:40:40']

bar_chart.render_to_file('grafic3.svg')

input("\n\nApasa <enter> pt a iesi.")
