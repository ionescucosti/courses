# 816
# Excel openpyxl - GRAFICE BIDIMENSIONALE
# PF - 12.01.2017

from openpyxl import Workbook
from openpyxl.chart import (
    AreaChart,
    Reference,
)

wb = Workbook()
ws = wb.active

rows = [
    ['Ziua', 'Intrari', 'Iesiri'],
    [1, 50, 30],
    [2, 80, 60],
    [3, 60, 45],
    [4, 70, 80],
    [5, 50, 50],
    [6, 80, 65],
    [7, 50, 20],
]

for row in rows:
    ws.append(row)

chart = AreaChart()
chart.title = "Magazin"
chart.style = 13
chart.x_axis.title = 'Vanzari'
chart.y_axis.title = 'Mii lei'

cats = Reference(ws, min_col=1, min_row=2, max_row=9)   # min_row = 2 ca sa eliminam antet
data = Reference(ws, min_col=1, min_row=1, max_col=3, max_row=8)    # max_col legenda
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)

ws.add_chart(chart, "A10")      # de unde incepe afisarea graficului

wb.save("area.xlsx")