# 425
# Genereaza username
# PF 160718


# --------------------------------------------------------------------------------------------------------#
# Creati o functie care sa genereze username format din prima litera a prenumelui si max 7 litere din nume#
# Numele si prenumele se introduc de la tastatura. Userul va fi format din litere mici                   #
# --------------------------------------------------------------------------------------------------------#

def generateusername(name, surname):
    n=name[0]
    p=surname[0:8]
    user=n+p
    print(user)

generateusername('gigel', 'iliescu')