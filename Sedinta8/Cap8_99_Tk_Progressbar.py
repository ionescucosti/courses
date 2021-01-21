# 9129
# Progressbar avansat
# Paul Fratila

from TKmodule import ttk

root = Tk()

pb_hd = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length = 200)
pb_hd.pack(expand=True, fill=BOTH, side=TOP)        # Parametrii sunt optionali
pb_hd.start()

pb_hd.config(mode = 'determinate', maximum = 15.0, value =5.0)
pb_hd.step()

value = DoubleVar()
pb_hd.config(variable =value)

scale = ttk.Scale(root, orient = 'horizontal', length = 300, variable = value, from_ = 0.0, to =15.0).pack()

root.mainloop()


