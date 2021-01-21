# Ex 701
# Crearea modulelor in Python package - factorial
# InfoAcademy PF 2016-05-27

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print "Rulezi acest modul direct, deci nu va rula nimic. Importa acest modul."
    raw_input ( "\n\nApasa <enter> pt a iesi." )