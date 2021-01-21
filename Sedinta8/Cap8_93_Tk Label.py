# 9123
# Label
# Paul Fratila

from TKmodule import ttk
    
root = Tk()

label = ttk.Label(root, text = "Hi, Romania!")   # numele etichetei
label.pack()
label.config(text = 'Hi, Reader!')      # modificare nume
label.config(text = 'Hi, Readear again!')
label.config(wraplength = 110)              # modificare latime in pixeli
label.config(justify = CENTER)              # aliniere RIGHT, LEFT or CENTER
label.config(foreground = 'green', background = 'yellow')    # setare culori text si fundal
label.config(font = ('Arial', 18, 'italic'))    # setare caractere
label.config(text = 'Hi, Romania!')

logo = PhotoImage(file = 'c:/wt/python_logo.gif')   # adaugare imagine
label.config(image = logo)
label.config(compound = 'text')             # revine la afisarea textului
label.config(compound = 'center')           # afiseaza textul centrat, suprapus peste imagine
label.config(compound = 'left')             # afiseaza textul la stanga, suprapus peste imagine

label.img = logo
label.config(image = label.img)

root.mainloop()
