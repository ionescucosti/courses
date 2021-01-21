# 9125
# Butone cu optiuni
# Paul Fratila

from TKmodule import ttk
    
root = Tk()

checkb = ttk.Checkbutton(root, text = 'Alege!')     # Creaza un buton cu posibilitatea de alegere (check)
checkb.pack()

decizie = StringVar()       # putem sa cream un obiect caruia ii atribuim o variabila
decizie.set('Alege!')
print(decizie.get())

checkb.config(variable = decizie, onvalue = 'Da!', offvalue = 'Nu!')    # configuram optiuni on/off pentru buton
print(decizie.get())    # arata ultima selectie efectuata sau empty daca nu a fost selectat

optiuni = StringVar()   # cream radiobutoane
ttk.Radiobutton(root, text = 'Vacanta', variable = optiuni, value = 'Mamaia').pack()
ttk.Radiobutton(root, text = 'Invata', variable = optiuni, value = 'InfoAcademy').pack()
ttk.Radiobutton(root, text = 'Distractie', variable = optiuni, value = 'Club').pack()
ttk.Radiobutton(root, text = 'Job', variable = optiuni, value = 'IBM').pack()

print(optiuni.get()) # arata ultima selectie efectuata sau empty daca nu a fost selectat

checkb.config(textvariable = optiuni)   # inlocuieste butonul cu selectia radiobuton efectuata

root.mainloop()
