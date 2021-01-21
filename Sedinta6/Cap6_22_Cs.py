# 622 Clase avansat
# Urare an nou 2017 :)
# PF - 01/01/2017

class An2017:
    '''Anul tau cel mai bun de pana acum
    cu sanatate, iubire si bani''' #

    def __init__(self, numar):
        self.sanatate = 'Maxima'    # default pentru tine
        self.iubire = 'Sublima'
        self.bani = numar

    def adauga_bani(self, suma):    # daca nu-ti ajung :)
        self.bani += suma

    def __str__(self):
        return '{0},{1},{2}'.format(self.sanatate,self.iubire,self.bani)

Tu = An2017(1000000)

print(Tu)