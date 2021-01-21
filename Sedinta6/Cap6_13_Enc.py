# Ex 613
# Variabila privata - incapsulare
# InfoAcademy PF 2016-05-27

class Car:

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed


redcar = Car()
redcar.drive()
redcar._Car__name
redcar._Car__maxspeed


redcar.__maxspeed = 10      # nu putem s-o schimbam direct, e privata
redcar.drive()

redcar.setMaxSpeed(320)     # ... doar prin intermediul unei metode
redcar.drive()

redcar.__maxspeed

print(redcar.__maxspeed)

redcar.__dict__

redcar._Car__maxspeed = 150
