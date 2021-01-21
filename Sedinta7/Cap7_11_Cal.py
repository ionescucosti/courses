# Ex 711
# Modulul calendar
# InfoAcademy PF 2016-05-27

import calendar

luna = calendar.month ( 2017, 10 )
print ( luna ) 								# calendarul desfasurat

ziua = calendar.weekday ( 2017, 8, 5 )
print ( ziua ) 								# numarul zilei (0 LUNI - 6)

print ( calendar.February ) 					# returneaza nr lunii

dir(calendar)

calendar.setfirstweekday ( 0 )  			# weekday ( 0 is Monday, 6 is Sunday ) - schmba prima zi

calendar.isleap ( 2017 )  					# testeaza an bisect

calendar.leapdays ( 2016, 2100 )  			# numarul de zile de 29 Feb in perioada

calendar.monthcalendar ( 2017, 10 )  		# liste cu zilele grupate pe saptamani

print ( calendar.day_name[2] )		 		# numele zilei

print ( calendar.month_name[6] ) 			# numele lunii

print ( calendar.month_abbr[7] ) 			# numele abreviat al lunii

print ( calendar.day_abbr[5] ) 				# numele abreviat al zilei

print ( calendar.mdays ) 					# returneaza numarul de zile al lunilor anului

luni = {x+1: calendar.month_abbr[x+1] for x in range(12)}       # dictionar cu lunile anului

saptamana = {x: calendar.day_abbr[x] for x in range(7)}         # dictionar cu zilele saptamanii

help(calendar)
