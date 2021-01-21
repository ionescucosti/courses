# 9126
# Entry
# Paul Fratila

from TKmodule import ttk
    
root = Tk()

entry = ttk.Entry(root, width = 25)     # numarul maxim de caractere
entry.pack()

entry.get()     # returneaza ce s-a introdus de la tastatura
                # nu beneficiaza de metodea set

entry.delete(0, 5)          # sterge primele 5 caractere (index 0-4)
entry.delete(0, END)        # sterge toate caracterele

entry.insert(9, 'acum ')    # insereaza (nu inlocuieste) textul incepand cu pozitia mentionata

len(entry.get())            # putem afla lungimea efectiva a textului introdus

entry.insert(len(entry.get()) + 1, 'Text')

entry.config(show = '*')    # afiseaza caracterul * in locul celor tastate (ex la introducerea parolei)

entry.state(['disabled'])   # blocheaza fereastra de intrare
entry.state(['!disabled'])  # reactivarea ferestrei
entry.state(['readonly'])   # doar citirea continutului


root.mainloop()
