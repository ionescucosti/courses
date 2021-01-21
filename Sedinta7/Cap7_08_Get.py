# Ex 708
# Modulul getpass
# InfoAcademy PF 2016-05-27

import getpass

usr = getpass.getuser ( )  # returneaza userul logat

print ( usr )

passw = getpass.getpass ( "Introdu parola pentru userul " + usr + ":" )

print ( passw )
