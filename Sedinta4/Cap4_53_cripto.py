# 453
# Codifica / decodifica ASCII
# PF 160718

# ------------------------------------------------------------------------------------------------------#
# Codificati un text cu echivalentul numeric din ASCII (numere despartite de spatii) - functia code()   #
# Decodificati numerele in text - functia decode()                                                      #
# ------------------------------------------------------------------------------------------------------#

a=\
'''Codificati un text cu echivalentul numeric din ASCII (numere despartite de spatii) - functia code()
Decodificati numerele in text - functia decode() 
'''
def code():
    sir = input("Baga: \n")
    code=''
    for c in sir:
        code=str(ord(c))+ ' '
    print(code)

def decode():
    cod = code()
    text=''
    for n in cod.split(' '):
        c = chr(eval(n))
        text+= c

    print(text)

code()
decode()