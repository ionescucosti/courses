# Ex 806
# SMTP
# InfoAcademy PF 2016-05-27

import smtplib

import pftp  # parole paul

expeditor = 'info@infoacademy.eu'
destinatar = 'paul@fratila.eu'
username = 'info@infoacademy.eu'
parola = pftp.parola
mesaj = """From: Paul <info@infoacademy.eu>
To: Gabriel <paul@fratila.eu>
Subject: Python e-mail test

Salut Gabriel,

Acesta este un e-mail test la SMTP !

Paul
"""

try:
    smtp_ob = smtplib.SMTP('mail.infoacademy.eu:25')  #
    # smtp_ob.starttls()  	# protocol criptare. e posibil sa nu mearga daca e activat
    smtp_ob.login(username, parola)
    smtp_ob.sendmail(expeditor, destinatar, mesaj)
    print('Mesaj expediat cu succes!')

except:
    print('Mesajul nu a putut fi expediat!')
