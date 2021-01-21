# 815
# new
# PF - 1/26/13

# Empty window

import TKmodule

ob_tk = TKmodule.Tk ()
ob_tk.mainloop ( )


# Mesaj

from TKmodule import messagebox

ob_tk = TKmodule.Tk ()

def mesaj():
	messagebox.showinfo ( 'Primul meu mesaj', 'Bine ati venit la TKmodule!' )

mB = TKmodule.Button (ob_tk, text='Click aici', command=mesaj)
mB.pack ( )
ob_tk.mainloop ( )


# Mesaj care va fi afisat in consola

def mesaj():
	messagebox.showinfo ( 'Primul meu mesaj', 'Bine ati venit la TKmodule!' )

def afiseaza():
	print ( 'Va fi afisat de Python' )

ob_tk = TKmodule.Tk ()
ob_tk.title ( 'Butoane' )

TKmodule.Button (ob_tk, text='Buton 1', command=mesaj).grid (row=0, column=0)
TKmodule.Button (ob_tk, text='Buton 2', command=afiseaza).grid (row=0, column=100)
TKmodule.Button (ob_tk, text='Exit', fg='red', command=quit).grid (row=0, column=200)

ob_tk.mainloop ( )

input('APASA <ENTER> pentru a iesi')
