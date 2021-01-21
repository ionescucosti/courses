# Ex 855
# HTTP
# InfoAcademy PF 2017-06-01     http://docs.python-requests.org/en/master/user/quickstart/


import requests
from pftp import gp, xc  # Nu face asta acasa :) - e din modulul meu

r = requests.get('https://api.github.com/user', auth=('pagulro', gp))
# gp e o variabila care contine  parola mea pe GitHub
r.status_code
r.headers['content-type']

r.encoding

r.text

r.json()

for k,v in r.json().items():
    print(str(k).ljust(30), ':', v)


r = requests.post('http://httpbin.org/post', data={'1': 100})

r.json() # verificam raspunsul
# va fi prelucrat de o aplicatie (fisiere php, python, etc.)

r = requests.put('http://httpbin.org/put', data = {'a': 100})
r.json() # verificam raspunsul

r = requests.delete('http://httpbin.org/delete')
r.json()

r = requests.head('http://httpbin.org/get')

r = requests.options('http://httpbin.org/get')

# Passing Parameters In URLs

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)

# ca sa acceseze resurse si sa paseze parametrii

print(r.url)

# Response Content

r = requests.get('https://api.github.com/events')

r.text
r.encoding
r.encoding = 'ISO-8859-1'

# Binary Response Content

r.content
'''
# create an image from binary data returned by a request - ???
from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content), 'r')
'''

# JSON Response Content

r = requests.get('https://api.github.com/events')
r.json()

r.raise_for_status()

r.status_code


# Raw Response Content

r = requests.get('https://api.github.com/events', stream=True)

r.raw

r.raw.read(10)
# preferabil pt fisiere diferite de fisierele text (octeti)

r = requests.get('https://api.github.com/user', auth=('pagulro', gp))

with open('C:/WT/_test.txt', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

with open('C:/WT/_test.txt', 'r') as fr:
    fisier = fr.read()
    print(fisier)

fr = open('c:/wt/_test.txt')

# x = fr.read()
    # trebuie vazut cum il extragem din JSON
# l = x.split(',')

# Custom Headers

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
r.text
'''
Note: Custom headers are given less precedence than more specific sources of information. For instance:

Authorization headers set with headers= will be overridden if credentials are specified in .netrc, 
which in turn will be overridden by the auth= parameter.
Authorization headers will be removed if you get redirected off-host.
Proxy-Authorization headers will be overridden by proxy credentials provided in the URL.
Content-Length headers will be overridden when we can determine the length of the content.
Furthermore, Requests does not change its behavior at all based on which custom headers are specified. 
The headers are simply passed on into the final request.

Note: All header values must be a string, bytestring, or unicode. While permitted, it's advised to 
avoid passing unicode header values.
'''

# More complicated POST requests

payload = {'key1': 'value1', 'key2': 'value2'}  # dictionar
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

# Sau

payload = (('key1', 'value1'), ('key1', 'value2'))  # tuplu --> genereaza lista de valori
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

# json-encoded

import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, json=payload)
r.text


# POST a Multipart-Encoded File

url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}

r = requests.post(url, files=files)
r.text

#  can set the filename, content_type and headers explicitly

url = 'http://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

r = requests.post(url, files=files)
r.text

# can send strings to be received as files

url = 'http://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

r = requests.post(url, files=files)
r.text.join('file')


# Response Status Codes

r = requests.get('http://httpbin.org/get')
r.status_code
r.raise_for_status()

r.status_code == requests.codes.ok

bad_r = requests.get('http://httpbin.org/status/404')
bad_r.status_code
bad_r.raise_for_status()

# Response Headers

r.headers

for i in r.headers:
    print(str(i).ljust(40) + ':' + r.headers[i])

r.headers['Content-Type']

# Cookies

# If a response contains some Cookies, you can quickly access them:

url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name']

# To send your own cookies to the server, you can use the cookies parameter:

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
r.text

'''
Cookies are returned in a RequestsCookieJar, which acts like a dict but also offers a more complete 
interface, suitable for use over multiple domains or paths. Cookie jars can also be passed in 
to requests:
'''

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
r.text


# Redirection and History

import requests
r = requests.get('http://infoacademy.net/course.php?p=Python&c=programa')

r.url

r.status_code

r.text
    # vezi daca exista decoder de HTML
r.text.split('<')

r.history

# If you're using GET, OPTIONS, POST, PUT, PATCH or DELETE, you can disable redirection
# handling with the allow_redirects parameter:

r = requests.get('http://github.com', allow_redirects=False)

r.status_code

r.history


# If you're using HEAD, you can enable redirection as well:

r = requests.head('http://github.com', allow_redirects=True)

r.url

r.history


# Timeouts

# single value for the timeout (will be applied to both the connect and the read timeouts)

requests.get('http://github.com', timeout=5)

# a tuple if you would like to set the values separately

r = requests.get('https://github.com', timeout=(3, 2))


# If the remote server is very slow, you can tell Requests to wait forever for a response, by passing None
# as a timeout value and then retrieving a cup of coffee

r = requests.get('https://github.com', timeout=None)

'''
You can tell Requests to stop waiting for a response after a given number of seconds with the 
timeout parameter. Nearly all production code should use this parameter in nearly all requests. 
Failure to do so can cause your program to hang indefinitely:
timeout is not a time limit on the entire response download; rather, an exception is raised if the 
server has not issued a response for timeout seconds (more precisely, if no bytes have been received 
on the underlying socket for timeout seconds). If no timeout is specified explicitly, requests do not 
time out.
'''


# Authentication - Basic Authentication

from requests.auth import HTTPBasicAuth

requests.get('https://api.github.com/user', auth=HTTPBasicAuth('pagulro', gp))

# Digest Authentication

from requests.auth import HTTPDigestAuth

url = 'http://httpbin.org/digest-auth/auth/user/pass'

requests.get(url, auth=HTTPDigestAuth('user', 'pass'))

# OAuth 1 Authentication

import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

requests.get(url, auth=auth)

# OAuth 2 and OpenID Connect Authentication
"""
Web Application Flow
Mobile Application Flow
Legacy Application Flow
Backend Application Flow
Other Authentication
Requests is designed to allow other forms of authentication to be easily and quickly plugged in. 
Members of the open-source community frequently write authentication handlers for more complicated 
or less commonly-used forms of authentication. Some of the best have been brought together under the 
Requests organization, including: Kerberos and NTLM
"""

# To do so, subclass AuthBase and implement the __call__() method:

import requests
class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        # Implement my authentication
        return r

url = 'http://httpbin.org/get'
requests.get(url, auth=MyAuth())




# requests.request(method, url, **kwargs)

'''
•	method -- method for the new Request object.
•	url -- URL for the new Request object.
•	params -- (optional) Dictionary or bytes to be sent in the query string for the Request.
•	data -- (optional) Dictionary or list of tuples [(key, value)] (will be form-encoded), bytes, 
or file-like object to send in the body of the Request.
•	json -- (optional) json data to send in the body of the Request.
•	headers -- (optional) Dictionary of HTTP Headers to send with the Request.
•	cookies -- (optional) Dict or CookieJar object to send with the Request.
•	files -- (optional) Dictionary of 'name': file-like-objects (or {'name': file-tuple}) 
for multipart encoding upload. file-tuple can be a 2-tuple ('filename',fileobj), 3-tuple ('filename', 
fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers), where 
'content-type' is a string defining the content type of the given file and custom_headers a 
dict-like object containing additional headers to add for the file.
•	auth -- (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
•	timeout (float or tuple) -- (optional) How many seconds to wait for the server to send data 
before giving up, as a float, or a (connect timeout, read timeout) tuple.
•	allow_redirects (bool) -- (optional) Boolean. 
Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
•	proxies -- (optional) Dictionary mapping protocol to the URL of the proxy.
•	verify -- (optional) Either a boolean, in which case it controls whether we verify the server's 
TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.
•	stream -- (optional) if False, the response content will be immediately downloaded.
•	cert -- (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
'''

import requests
req = requests.request('GET', 'http://httpbin.org/get')

req.text

# requests.head(url, **kwargs)

'''
•	url -- URL for the new Request object.
•	**kwargs -- Optional arguments that request takes.
'''

# requests.get(url, params=None, **kwargs)

'''
•	url -- URL for the new Request object.
•	params -- (optional) Dictionary or bytes to be sent in the query string for the Request.
•	**kwargs -- Optional arguments that request takes.
'''

# requests.post(url, data=None, json=None, **kwargs)

'''
•	url -- URL for the new Request object.
•	data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in 
the body of the Request.
•	json -- (optional) json data to send in the body of the Request.
•	**kwargs -- Optional arguments that request takes.
'''

# requests.put(url, data=None, **kwargs)

'''
•	url -- URL for the new Request object.
•	data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in 
the body of the Request.
•	json -- (optional) json data to send in the body of the Request.
•	**kwargs -- Optional arguments that request takes.
'''

# requests.patch(url, data=None, **kwargs)

'''
•	url -- URL for the new Request object.
•	data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the 
body of the Request.
•	json -- (optional) json data to send in the body of the Request.
•	**kwargs -- Optional arguments that request takes.
'''

# requests.delete(url, **kwargs)

'''
•	url -- URL for the new Request object.
•	**kwargs -- Optional arguments that request takes.
'''


#-#-#-#    ADVANCED     #-#-#-#

# Session Objects

"""
The Session object allows you to persist certain parameters across requests. 
It also persists cookies across all requests made from the Session instance, and will use urllib3's 
connection pooling. So if you're making several requests to the same host, the underlying TCP 
connection will be reused, which can result in a significant performance increase 
(see HTTP persistent connection).

A Session object has all the methods of the main Requests API.
"""

import requests
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')

print(r.text)


# Sessions can also be used to provide default data to the request methods

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})    # both 'x-test' and 'x-test2' are sent

s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})


# This example will only send the cookies with the first request, but not the second

s = requests.Session()

r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)

r = s.get('http://httpbin.org/cookies')
print(r.text)

# Sessions can also be used as context managers:

with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

'''
Remove a Value From a Dict Parameter
Sometimes you'll want to omit session-level keys from a dict parameter. To do this, you simply set 
that key's value to None in the method-level parameter. It will automatically be omitted.
'''


# Request and Response Objects

# - access the headers the server sent back to us

r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')

r.headers

for k, v in r.headers.items():
    print(str(k).ljust(30), v)

# - get the headers we sent the server

r.request.headers


# Prepared Requests

from requests import Request, Session

s = Session()

req = Request('POST', url, data='2017-06-01', headers=r.headers)
prepped = req.prepare()

# do something with prepped.body
prepped.body = 'No, I want exactly this as the body.'

# do something with prepped.headers
del prepped.headers['Content-Type']

resp = s.send(prepped,
    #stream=stream,      ?
    #verify=verify,      ?
    #proxies=proxies,    ?
    #cert=cert,          ?
    timeout=0.01
)

print(resp.status_code)

# sau

from requests import Request, Session

s = Session()
req = Request('GET',  url, data='2017-06-01', headers=r.headers)

prepped = s.prepare_request(req)

# do something with prepped.body
prepped.body = 'Seriously, send exactly these bytes.'

# do something with prepped.headers
prepped.headers['Keep-Dead'] = 'parrot'

resp = s.send(prepped #,
    #stream=stream,
    #verify=verify,
    #proxies=proxies,
    #cert=cert,
    #timeout=timeout
)

print(resp.status_code)


# SSL Cert Verification

requests.get('https://requestb.in')

requests.get('https://github.com')

requests.get('https://github.com', verify='/path/to/certfile')

# sau

s = requests.Session()
s.verify = '/path/to/certfile'

requests.get('https://kennethreitz.org', verify=False)


# Client Side Certificates

requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))

# Streaming Uploads

with open('massive-body', 'rb') as f:
    requests.post('http://some.url/streamed', data=f)


# POST Multiple Multipart-Encoded Files

url = 'http://httpbin.org/post'
multiple_files = [
        ('images', ('C:/Users/admin/Pictures/3Py8_1.png',
                    open('C:/Users/admin/Pictures/3Py8_1.png', 'rb'), 'image/png')),
        ('images', ('C:/Users/admin/Pictures/3Py-Mid-1.png',
                    open('C:/Users/admin/Pictures/3Py-Mid-1.png', 'rb'), 'image/png'))]
r = requests.post(url, files=multiple_files)
r.text


# Custom Authentication

from requests.auth import AuthBase

class PizzaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r

requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))

# Proxies

# can configure individual requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('http://example.org', proxies=proxies)

# can also configure proxies by setting the environment variables HTTP_PROXY and HTTPS_PROXY

'''
$ export HTTP_PROXY="http://10.10.1.10:3128"
$ export HTTPS_PROXY="http://10.10.1.10:1080"

$ python
'''

requests.get('http://example.org')

# use HTTP Basic Auth with your proxy, use the http://user:password@host/ syntax

proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}

# http://docs.python-requests.org/en/master/user/advanced/#advanced


# wunderground.com/whethear/api - pentru GET
# incearca facebook pt POST
# QUOTES.REST -



r = requests.get('https://infoacademy.net/a', auth=('mihaela', xc))

r.text


import requests

resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))

task = {"summary": "Take out trash", "description": "" }
resp = requests.post('https://todolist.example.com/tasks/', json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))

