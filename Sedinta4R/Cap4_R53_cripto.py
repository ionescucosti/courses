# 493
# Codifica / decodifica ASCII
# PF 160718

# ------------------------------------------------------------------------------------------------------#
# Codificati un text cu echivalentul numeric din ASCII (numere despartite de spatii) - functia code()   #
# Decodificati numerele in text - functia decode()                                                      #
# ------------------------------------------------------------------------------------------------------#

def code():
    """Transforma caracterele in numere coresp ASCII"""
    sir = input('Introduceti textul : ')
    sir_code =''
    for car in sir:
        sir_code = sir_code + str(ord(car)) + ' '
    print(sir_code)

code()

def decode():
    """Transforma numerele in caractere coresp ASCII"""
    sir = input('Introduceti numerele : ')  		# Introducem rezultatul codificat
    text = ''  								# Intitializam sirul care primeste textul

    for numar in sir.split(' '):  			# facem split la textul ce cuprinde numerele
        car = chr(eval(numar))  			# Numerele sunt sub forma de string. Mergea si int (numar
                                            # Folosim eval() pentru a transforma digiti in numere
        text += car                         # Adaugam caracterul gasit la sfarsitul textului
    print(text)

decode()
