# Cap 7 ex 1
# Explica crearea unui modul
# PF 2017/04/12

def aduna(*x):
    suma = 0
    for i in x:
        try:
            suma += i
        except:
            print('Parametri trebuie sa fie numerici')
    return suma

if __name__ == '__main__':
    print('primul meu modul')