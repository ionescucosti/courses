# 475
# Genereaza username
# PF 160718

# --------------------------------------------------------------------------------------------------------#
# Creati o functie care sa genereze username format din prima litera a prenumelui si max 7 litere din nume#
# Numele si prenumele se introduc de la tastatura. Userrul va fi format din litere mici                   #
# --------------------------------------------------------------------------------------------------------#

def user():
    """Genereaza username pe baza prenumelui (primul caracter) si numelui (max 7 caractere) - (lowercase)"""
    p = input('Introduceti prenumele : ').lower()  		# introducem first and last name
    n = input('Introduceti numele : ').lower()
    u = p[0] + n[:7]  									# concatenam cele doua siruri
    print('Username este: ', u)  						# returneaza username generat

user()

#sau


def uname(n,p):
    """primeste nume si prenume, returneaza username"""
    p1 = p[0].lower()
    n1 = n[0:7].lower()
    u = p1+n1
    return u

uname('Coman', 'Paraschiva')

input('Apasa <enter> pentru a iesi.')
