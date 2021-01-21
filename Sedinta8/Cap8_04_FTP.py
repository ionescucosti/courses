# Ex 804
# FTP (ftplib)	- DE REVIZUIT
# InfoAcademy PF 2016-05-27

import ftplib

import pftp  # pftp e modul propriu cu parola de ftp:)

# Conectare

host = 'ftp.infoacademy.net'
ftp = ftplib.FTP ( host )
ftp.login ( 'paul@infoacademy.net', pftp.parol )
ftp.retrlines ( 'LIST' )			# lista fisiere existente
file = 'text9.txt'
ftp.storbinary ( 'STOR ' + file, open ( file, 'rb' ) )			# upload fisier


from ftplib import FTP

ftp = FTP ( 'ftp.debian.org' )  				# connect to host, default port
ftp.login ( )  									# user anonymous, passwd anonymous@

ftp.cwd ( 'debian' )  							# change into "debian" directory

ftp.retrlines ( 'LIST' )  						# Lista fisiere disponibile

ftp.retrbinary ( 'RETR README', open ( '.\README', 'wb' ).write ) # download fisier


# download fisier - alta varianta

deschide = open ( 'README.mirrors.txt', 'wb' )

ftp.retrbinary ( 'RETR ' + 'README.mirrors.txt', deschide.write, 2048 )  	# buffer

ftp.quit ( )