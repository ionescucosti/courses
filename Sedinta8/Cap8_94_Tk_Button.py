# 9124
# Butoane
# Paul Fratila

from TKmodule import ttk
    
root = Tk()

button = ttk.Button(root, text = "Apasa aici, acum!")   # crearea unui buton
button.pack()

def afiseaza():
    print('Efectuat!')

button.config(command = afiseaza)           # la apasarera butonului apeleaza functia afiseaza
button.invoke()                         # acelasi lucru, plus o linie cu None

button.state(['disabled'])              # dezactiveaza butonul
print(button.instate(['disabled']))     # arata starea butonului (dezactivat = True, altfel faalse)
button.state(['!disabled'])             # anularea dezactivarii (reactivarea butonului)
print(button.instate(['!disabled']))

logo = PhotoImage(file = 'c:/wt/python_logo.gif')
button.config(image = logo, compound = CENTER)

small_logo = logo.subsample(10, 10)
button.config(image = small_logo)

root.mainloop()
