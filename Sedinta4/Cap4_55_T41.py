# Cap 4 tema 1
# Crearea unei functii simple
# PF - 27/05/2016

# --------------------------------------------------------------------------------------#
#	Creati un program cu o functie care returneaza numarul de cifre dintr-un sir        #
#		de caractere dat ca parametru de intrare. Aplicati functia pentru trei siruri   #
#		diferite introduse de la tastatura.                                             #
#	Creati o functie care numara cifrele, spatiile si total caractere                   #
# --------------------------------------------------------------------------------------#
def numaraCifre(text):
    count=0
    for i in text:
        if i.isdigit():
            count+=1
    return count

def countEachType(text):
    numbers=0
    spaces=0
    chars=0
    for i in text:
        if i.isdigit():
            numbers +=1
            chars += 1
        elif i == ' ':
            spaces += 1
            chars += 1
        else:
            chars += 1

    return 'numere: ',numbers,' spatii: ',spaces,' in total: ',chars

#print(numaraCifre('am 35 de ani'))

cat=3
while cat>0:
    cat-=1
    x=input('baga text: ')
    print(numaraCifre(x))

print(countEachType('am 35 de ani'))