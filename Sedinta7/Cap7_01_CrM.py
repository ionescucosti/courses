# Ex 701
# Crearea modulelor in Python (modululmeu)
# InfoAcademy PF 2016-05-27

def patrat(nr=1):
    """ Ridicarea la patrat"""
    try:
        rezult = nr * nr
    except:
        rezult = "Introduceti un numar"
    return rezult


def cub(nr=1):
    """ Ridicarea la cub"""
    try:
        rezult = nr * nr * nr
    except:
        rezult = "Trebuie sa introduci un numar"
    return rezult


def factorial(n=5):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print("E un modul. Importa acest modul pentru a putea utiliza functiile din el.")
