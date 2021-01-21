# 452 TxT
# Exercitii stringuri - criptare
# PF 160719

# --------------------------------------------------------------------------------------------------------------#
# Creati un program care sa faca acronime cu prima litera a cuvintelor componente (litere mari)                 #
# Creati un program care sa returneze echivalentul numeric al textului a=1, b=2, ..., z=26 (lista)              #
# Faceti decriptarea                                                                                            #
# [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z'] #
# --------------------------------------------------------------------------------------------------------------#

file = open('C:/Users/ext_constantini/WORK/people1.txt','r')
out = open('C:/Users/ext_constantini/WORK/out.txt','a+')
lines = file.readlines()
for line in lines:
    words=line.split()
    p=words[0]
    n=words[1]
    acronim=p[0]+n[0]+'\n'
    out.write(acronim)

file.close()