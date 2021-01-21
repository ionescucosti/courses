# Ex 704
# Modulul os
# InfoAcademy PF 2016-05-27

import os

os.getcwd()                     	# directorul de unde ruleaza programul (IDE)

os.system('ping 8.8.8.8')    		# comand prompt (terminal)
os.system('ipconfig')    			# comand prompt (terminal)

os.chdir('C:\Python35\Lib')          			# schimba directorul

os.listdir('c:\wt')   # lista cu fisierele din director

for i in os.listdir('c:\python35\lib\pkg'):		# cautare fisier pe HDD
	if i == 'cub.py':
		print ( 'l-am gasit' )

os.linesep                      # returneaza separatorul de linie

os.sep                          # returneaza separatorul de directoare

os.remove('c:/wt/text2.txt')     # sterge fisierul

os.rmdir('c:/wt/test')      # sterge directorul, DACA NU ARE FISIERE

os.system('rmdir /S /Q c:\\wt\\test2') # sterge directorul CHIAR DACA ARE FISIERE





