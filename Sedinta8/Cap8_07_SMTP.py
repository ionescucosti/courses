# Ex 807
# SMTP
# InfoAcademy PF 2016-05-27

import smtplib

import pftp

expeditor = 'paul@fratila.ro'
destinatar = 'paul@fratila.eu'
username = 'paul@fratila.ro'
parola = pftp.parola
mesaj = """From: Paul <paul@fratila.ro>
To: Gabriel <paul@fratila.eu>
Subject: Python e-mail test
Content-type: text/html
<html>

Salut Gabriel,

<p>Acesta este un e-mail test! </p>
......

<p>Paul</p>

</html>
"""

try:
	smtp_ob = smtplib.SMTP ( 'mail.fratila.ro:25' )
	# smtp_ob.starttls ( )  						# protocol criptare
	smtp_ob.login ( username, parola )
	smtp_ob.sendmail ( expeditor, destinatar, mesaj )
	print ( 'Mesaj expediat cu succes!' )

except:
	print ( 'Mesajul nu a putut fi expediat!' )
