# Ex 716
# Modulul datetime
# InfoAcademy PF 2016-05-27

import datetime

i = datetime.datetime.now ( )  						# stocheaza momentul de timp curent

print ( i )
print ( "Current date & time = {0}".format(datetime.datetime.now ( )) )
print ( "Date and time in ISO format = {0}".format(i.isoformat ( ) ) )
print ( "Current year = {0}".format(i.year) )  			# extragem diferite componente din datetime
print ( "Current month = {0}".format(i.month) )
print ( "Current date (day) =  {0}".format(i.day) )
print ( "dd/mm/yyyy format =  {0}/{1}/{2}".format(i.day, i.month, i.year) )
print ( "Current hour = {0}".format(i.hour) )
print ( "Current minute = {0}".format(i.minute) )
print ( "Current second =  {0}".format(i.second) )
print ( "hh:mm:ss format = {0}:{1}:{2}".format(i.hour, i.month, i.second) )

# Alternativ

from datetime import datetime

i = datetime.now ( )

print ( str ( i ) )

print ( i.strftime ( '%Y/%m/%d %H:%M:%S' ) ) 				# formatam momentul de timp in formatul dorit
print ( str ( datetime.now ( ).strftime ( '%d%m%Y' ) ) )

print ( datetime.now ( ).strftime ( '%d/%m/%Y %H.%M.%S' ) ) # formatam data curenta in formatul dorit

print ( datetime.strptime ( '27-05/2016T11.59.59', '%d-%m/%YT%H.%M.%S' ) ) # transformam din string in datetime

print ( datetime.strftime(datetime.strptime ('2017-18/01', '%Y-%d/%m'), '%Y-%m-%d'))

import datetime

a = datetime.datetime.now()
b = datetime.datetime.now()

print(b - a)
print(b.replace(microsecond=0) - a.replace(microsecond=0))

x = datetime.datetime(2018,5,27, 5, 35, 59, 1)  # parametrii an, luna, zi, ora, min, secunda, microsecunda
y = datetime.datetime(2018,1,1, 0, 0, 0, 0)     # parametrii sunt numere intregi, pot fi calculati cu expresii

print(x - y)

# class date(year, month, day)

datetime.date.fromtimestamp(1640995200.0)   # primeste nur_de_secunde intoarce localdate

datetime.date.isocalendar(datetime.date.today())   # ISO year, week number, and isoweekday (1-7)

datetime.date.isoformat(datetime.date.today())      # aaaa-ll-zz

datetime.date.timetuple(datetime.date(2017, 1, 1))  # ultimele trei argument datetime.date(an, luna, zi)

datetime.date.today()

# class datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

datetime.datetime.isoformat(datetime.datetime.today())      # aaaa-ll-zzThh:mm:ss[.ffffff][+hh:mm]

datetime.datetime.isoformat(datetime.datetime(2017,3,3))
datetime.datetime.isoformat(datetime.datetime(2017,3,3, 10))
datetime.datetime.isoformat(datetime.datetime(2017,3,3, 10, 15))
datetime.datetime.isoformat(datetime.datetime(2017,3,3, 10, 15, 59))
datetime.datetime.isoformat(datetime.datetime(2017,3,3, 23, 59, 59, 999999))

datetime.datetime.now()

datetime.datetime.timetuple(datetime.datetime(2017,3,3))

# class timedelta

referinta = datetime.timedelta(100, 36000, 101010)    # zile, secunde, microsecunde
                                                # returneaza secunde
datetime.timedelta.total_seconds(referinta)
datetime.timedelta.total_seconds(datetime.timedelta(18993, 0, 0))

datetime.datetime.now() - referinta # returneaza datetime din ziua de referinta

datetime.datetime(2017, 1, 1) - referinta # datetime din urma cu referinta

datetime.datetime.timestamp(datetime.datetime(2017,3,3, 23, 59, 59, 999999))    # secunde de la 1.1.1970
