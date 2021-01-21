# Program ftp Client
# Explica functiile ftplib
# CP - 1/26/13

import ftplib

ftp = ftplib.FTP('speedtest.tele2.net')
ftp.login()
ftp.retrlines('LIST')
ftp.close()

input("\n\nApasa <enter> pt a iesi.")
