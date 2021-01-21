# cap 7 Tema 2
# Utilizarea random si calendar
# CP  01/01/2013

"""
 Creati un program care sa aiba o functie numita dataAleatoriu care returneaza
   o lista din trei elemente.
       - Primul element al listei sa fie un an aleatoriu intre 2016 si 2050.
       - Al doilea element al listei sa fie o luna aleatorie returnata ca numar intre 1 si 12.
       - Al treilea element al listei sa fie o zi intre 1 si numarul maxim de zile din luna aleasa
 Apelati de trei ori functia si stocati rezultatul in cate o variabila.
 Aflati ziua din saptamana a datelor returnate.
 """ #

import calendar
import datetime
import random

saptamana = {x: calendar.day_abbr[x] for x in range(7)}

# sau:
# saptamana={0:"luni",1:"marti",2:"miercuri",3:"joi",4:"vineri",5:"sambata",6:"duminica"}

def dataAleatoriu():
    lista = []
    an = random.randrange(2016,2050)
    luna = random.randrange(1,12)
    if calendar.isleap(an) == True and luna == 2:           # sau calendar.monthrange(an,luna)[1]
        zi = random.randrange ( 1, calendar.mdays[luna] +1 )
    else:
        zi = random.randrange(1, calendar.mdays[luna])
    lista += [an]
    lista += [luna]
    lista += [zi]
    return lista

Apelare1 = dataAleatoriu()

print ( "Data aleasa este anul: ",Apelare1[0],", luna: ",Apelare1[1],", ziua: ",Apelare1[2] )

zi_sap1 =  calendar.weekday(Apelare1[0],Apelare1[1],Apelare1[2])
print ("Ziua saptamanii pt. data aleasa este ",saptamana[zi_sap1] )

Apelare2 = dataAleatoriu()
print ( "Data aleasa este anul: ",Apelare2[0],", luna: ",Apelare2[1],", ziua: ",Apelare2[2] )

zi_sap2 =  calendar.weekday(Apelare2[0],Apelare2[1],Apelare2[2])
print ( "Ziua saptamanii pt. data aleasa este ",saptamana[zi_sap2] )

Apelare3 = dataAleatoriu()
print ( "Data aleasa este anul: ",Apelare3[0],", luna: ",Apelare3[1],", ziua: ",Apelare3[2] )

zi_sap3 =  calendar.weekday(Apelare3[0],Apelare3[1],Apelare3[2])
print ( "Ziua saptamanii pt. data aleasa este ",saptamana[zi_sap3] )

# Reda date cu datele primite
print ( datetime.datetime.strptime ( str(Apelare3[0]) + str(Apelare3[1]) + str(Apelare3[2]),
                                     '%Y%m%d' ) )

      
