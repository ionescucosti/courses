# 402 Functii
# Functii utile
# PF - 27/05/2016

# 	Aria triunghiului
def aria_tri(baza, inaltime):
    return baza * inaltime * .5

aria_tri(5, 7)

# Calificative
def grade(score):
    """Calculeaza calificativul obtinut pe baza notei"""
    try:
        score = float(score)
    except:
        print('nu e numar')
    else:
        if score > 10.0 or score < 0.0:
            print('Bad score')
        elif score > 9.0:
            return 'A'
        elif score > 8.0:
            return 'B'
        elif score > 7.0:
            return 'C'
        elif score > 6.0:
            return 'D'
        else:
            return 'F'

grade(9.01)

# Transforma celsius in fahrenheit si invers
def cel_fahr(temp, tip):
    """Transforma c->f sau f->c. Tip este c sau f corespunzator temp introduse"""
    if tip.upper() == 'C':
        fahr = temp * 9 / 5 + 32
        return fahr
    elif tip.upper() == 'F':
        cel = 5 / 9 * (temp - 32)
        return cel

cel_fahr(0, 'c')
cel_fahr(100, 'f')

# Transforma fahrenheit in kelvin
def fahr_kelvin(fahr):
    cel = cel_fahr(fahr, 'F')
    kel = cel + 273.15
    return kel

fahr_kelvin(32)

# An bisect - calculam daca anul este bisect si verificam daca este intre 1-9999
def bisect(an):
    """Returneaza 1 daca e an bisect, 0 daca nu este"""
    if 1 <= an <= 9999:
        if an % 400 == 0:
            bis = 1
        elif an % 100 == 0:
            bis = 0
        elif an % 4 == 0:
            bis = 1
        else:
            bis = 0
        return bis
    else:
        print('In afara intevalului')

print(bisect.__doc__)           # returneaza docstringul functiei
bisect(2016)                    # apelam functia

# Lista lui Fibonacci - o functie care se apeleaza pe sine - recursiva
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(35))

# sau
def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fibo(1000))
len(str(fibo(1000)))

input('Apasa <enter> pentru a iesi.')