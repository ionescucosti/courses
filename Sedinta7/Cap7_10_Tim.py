# Ex 710
# Modulul time
# InfoAcademy PF 2016-05-27

import time

time.localtime ()  					    # returneaza struct_time
time.gmtime()

print ( time.localtime () )

t = time.asctime ( time.localtime() )  	# returneaza data si ora

print ( t ) # le printeaza

time.asctime ( time.localtime ( ) )  	# printeaza data si ora ca string

time.sleep ( 5 )
print ( 'Pauza s-a sfarsit, apuca-te de treaba :)' ) 						# suspenda executia timp de 5 secunde

time.strftime ( "%a %d %b %Y %H:%M:%S", time.gmtime() )

time.strptime ( "30 Nov 00", "%d %b %y" ) # transforma string in struct_time

# 24 hour format
print ( time.strftime ( "%H:%M:%S" ) ) # returneaza time in formatul dorit

# 12 hour format
print ( time.strftime ( "%I:%M:%S" ) )

# zi/luna/an
print ( time.strftime ( "%d/%m/%Y" ) )

# aaaa-ll-zz
print ( time.strftime ( "%Y-%m-%d" ) )

# Diferenta dintre doua date (datetime)

import time

a = time.time()  # current time in second    (TIME 1)

b = time.mktime((2000+17, 3+3, 20, 9, 54, 59, 1, 171, 1))  # refference time (TIME 0)
'''
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
'''

dif = float('{:f}'.format(a - b))       # cu 6 zecimale la secunda
print(dif)

dif = float('{:.0f}'.format(b - a))     # fara zecimale

# puteti reda diferenta cu o functie

def sec_to_time(time_in_second):
    ore = int(time_in_second // 3600)
    dif = time_in_second % 3600
    min = int(dif // 60)
    sec = int(dif % 60)
    return '''Timp: {0}:{1:02d}:{2:02d}
    Zile-timp: {3} zile si '{4}:{1:02d}:{2:02d}'''.\
            format(ore, min, sec, int(ore // 24),
                    ore - int(ore // 24) * 24)

sec_to_time(159900)

# alte functii

c = time.asctime()  # string current time
print(c)

time.ctime(a)   # transforma din secunde Epoch in string

time.gmtime(b)  # struct_time GMT

time.localtime(b)   # struct_time LOCAL



