# Ex 714
# Explica zipfile - cream o arhiva noua
# PF 31/05/2016

import zipfile

arh_noua = zipfile.ZipFile('c:/wt/exemplu5.zip', 'a')   	# cream o arhiva noua
arh_noua.write('c:/wt/medici.txt')                            # adaugam un fisier existent

arh_noua.close()

input("\n\nApasa <enter> pt a iesi.")

