# Ex 701
# Crearea modulelor in Python package -patrat
# InfoAcademy PF 2016-05-27

def patrat(nr=1):
    """ Ridicarea la patrat"""
    try:
        rezult = nr * nr
    except:
        rezult = "Introduceti un numar"

    return rezult

if __name__ == "__main__":
    print "Rulezi acest modul direct, deci nu va rula nimic. Importa acest modul."
    raw_input ( "\n\nApasa <enter> pt a iesi." )