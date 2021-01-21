# 104 Input
# Captarea unui text de la tastatura
# PF - 06/10/2017 v3

# captarea unui text de la tastatura cu input (raw_input in versiunea 2.x)
def salut():                                    # o functie simpla
    numele = input('Introduceti numele: ')
    orasul = input('Introduceti orasul: ')
    varsta = input('Introduceti varsta: ')
    return 'Salut, sunt ' +  numele + ', locuiesc in ' + orasul + ', si am ' + varsta + ' ani'

# transformarea stringului captat in float sau int

OreLucr = input('Introduceti numarul de ore: ')     # mesajul este pentru utilizator
TarifOrar = input('Introduceti tariful orar: ')     # input introduce siruri de caractere

print('Ai de incasat: ', float(OreLucr) * float(TarifOrar))

# sau transformare direct la input
OreLucr = float(input('Introduceti numarul de ore: '))
TarifOrar = float(input('Introduceti tariful orar: '))

print('Salariul tau este:', OreLucr * TarifOrar)

input("Apasa <enter> pt a iesi.")

