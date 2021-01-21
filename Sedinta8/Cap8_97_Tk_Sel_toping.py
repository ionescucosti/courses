# 9127
# Selectii dintr-o lista de optiuni
# Paul Fratila

from TKmodule import ttk
    
root = Tk()

week = StringVar()
selectie = ttk.Combobox(root, textvariable = week)
selectie.pack()         # in acest moment avem o fereastra cu posibilitatea de alegere, fara optiuni inca

selectie.config(values = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
print(week.get())

week.set('Fri')
week.set('A new day!')  # atentie, cu set pot fi introduse si valori care nu exista in lista de optiuni

year = StringVar()
Spinbox(root, from_ = 1900, to = 2017, textvariable = year).pack()
print(year.get())    # pentru valori sortate, cum ar fi o lista cu numere, putem derula in sus si in jos
                     # daca introducem manual o valoare in afara plajei de valori la derulare revine in lista
root.mainloop()