# 251 Boolean
# Boolean
# PF - 06/10/2017 v3

"""Boolean Operators
	-------------------------------------
	True    and     True    este      True
	True    and     False   este      False
	False   and     True    este      False
	False   and     False   este      False
	-------------------------------------
	True    or      True    este      True
	True    or      False   este      True
	False   or      True    este      True
	False   or      False   este      False
	-------------------------------------
Not     True    este      False
Not     False   este      True
---------------------------------

-----------PRECEDENTA------------
not     este evaluat primul;

and     este evaluat dupa not;

or      este evaluat ultimul.
""" #

# dati exemple proprii pentru fiecare situatie din cele de mai sus
# 	Ex: (5 + 3 ) >= 8 and 7 > 10 este False

7 > 5 and 5 > 3 # True
7 > 5 and 5 < 3 # False
7 < 5 and 5 > 3 # False
7 < 5 and 5 < 3 # False

7 > 5 or 5 > 3 # True
7 > 5 or 5 < 3 # True
7 < 5 or 5 > 3 # True
7 < 5 or 5 < 3 # False

# dati 7 exemple utilizand operatori combinati,
# 	Ex: not (10 ** 2) > 101 and (10 >5 or 100 < 0) este True

not 225 == 15**2 or 10**2 == 100    # True
not 225 == 15**2 and 10**2 == 100   # False
not 225 == 15**2 or 10**2 > 100     # False
not 225 == 15**2 or not 10**2 == 100   # False
not 225 > 15**2 and 10**2 == 100    # True
not 225 >= 15**2 or 10**2 < 100     # False



input ( "Apasa <enter> pt a iesi." )
