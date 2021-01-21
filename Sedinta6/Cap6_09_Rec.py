# Ex 609
# Functii recursive
# InfoAcademy PF 2016-05-27

# exemplu de functie recursiva

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


factorial(105)


def factorial(n):
    if n == 1:
        return 1
    else:
        res = n * factorial(n - 1)
        print("rezultat intermediar pentru ", n, " * factorial(", n - 1, "): ", res)
        return res


factorial(300)

print(len(str(factorial(300))))
