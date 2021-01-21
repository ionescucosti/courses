# Ex 805
# HTTP
# InfoAcademy PF 2016-05-27

# Instalare:      pip install requests

import requests

conect = requests.get ( 'https://python.org' )  # extragem pagina

print(conect.content)  							# vizualizam pagina
print(conect.text)

# pagina speciala pentru teste

r = requests.get ( 'http://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd') )

print ( r.content )
print ( r.text )

print ( r.status_code )						# starea executarii operatiunii solicitate

requests.codes.INTERNAL_SERVER_ERROR  		# introducem tipul erorii si returneaza codul

r.headers   # ['Content-Type']				# returneaza un dictionar cu headerele
r.headers.keys ()
r.headers.values ()


import json  								# JavaScript Object Notation

url = 'https://api.github.com/'

payload = {'some': 'data'}

headers = {'content-type': 'application/json'}

r = requests.post ( url, data=json.dumps ( payload ), headers=headers )

print ( r.headers )

r.close ( )


payload = dict(key1='value1', key2='value2')
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
