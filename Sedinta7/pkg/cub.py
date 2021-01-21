# Ex 701
# Crearea modulelor in Python package - cub
# InfoAcademy PF 2016-05-27

def cub(nr=1):
    """ Ridicarea la cub"""
    try:
        rezult = nr * nr * nr
    except:
        rezult = "Trebuie sa dai un numar"

    return rezult

if __name__ == "__main__":
    print "Rulezi acest modul direct, deci nu va rula nimic. Importa acest modul."
    raw_input ( "\n\nApasa <enter> pt a iesi." )