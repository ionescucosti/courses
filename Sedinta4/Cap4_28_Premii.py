'''
Organizati un concurs, la care pot participa pana un numar variabil de concurenti.
- daca sunt mai putin de 3 participanti se anuleaza;
- intre 3-10 participanti - vor fi trei premianti 50%, 35%, 15% din valoarea premiului;
- intre 11-30 participanti - 5 premianti cu 40%, 30%, 10%, 10%, 10%
- peste 31 de participanti - 10 premianti cu 30%, 20%, 15%, 7 ori 5%

Creati o functie care sa primeasca ca argument valoarea premiului si numarul de participanti
si sa returneze valoarea premiilor pentru fiecare castigator (locul 1, 2, etc.).

Creati o alta functie, care sa tina cont si de impozit, astfel incat premiile mai mari de
10000 de lei sa fie impozitate cu 16%.
'''#

def concurs(n, premiu):
    if n<3:
        print('anulat')
    elif n>=3 and n<=10:
        print('prmiul 1: ',0.5*premiu,
              '\npremiul 2: ',0.35*premiu,
              '\npremiul 3: ',0.15*premiu)
    elif n>10 and n<=30:
        print('prmiul 1: ', 0.4 * premiu,
              '\npremiul 2: ', 0.30 * premiu,
              '\npremiul 3: ', 0.1 * premiu,
              '\npremiul 4: ', 0.1 * premiu,
              '\npremiul 5: ', 0.1 * premiu)
    else:
        print('prmiul 1: ', 0.3 * premiu,
              '\npremiul 2: ', 0.2 * premiu,
              '\npremiul 3: ', 0.15 * premiu,
              '\npremiul 4: ', 0.7 * premiu,
              '\npremiul 5-10: ', 0.5 * premiu)

concurs(31,1000)