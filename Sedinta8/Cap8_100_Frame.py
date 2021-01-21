# 9130
# Frame
# Paul Fratila

from TKmodule import ttk

root = Tk()

fr = ttk.Frame(root)
fr.pack()
fr.config(height = 100, width = 200)
fr.config(relief = RIDGE)
ttk.Button(fr, tex  t = 'Apasa').pack()   # grid geometry mng creaza butonul in frame, asa cum pack creaza frame-ul
fr.config(padding = (20, 10))           # pading adaugat butonului
ttk.LabelFrame(root, height = 100, width = 200, text = 'Test Frame').pack()

root.mainloop()


