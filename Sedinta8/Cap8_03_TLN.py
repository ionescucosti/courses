# Ex 803
# Telnet (telnetlib)
# InfoAcademy PF 2016-05-27

import telnetlib

host = 'route-server.he.net' # 'route-server.ip.tiscali.net'  sau 'route-server.he.net'
# host = 'route-server.ip.tiscali.net'

obiect = telnetlib.Telnet ( host )

obiect.read_until ( b'Login: ', 2)
obiect.read_until ( b'Password: ', 2 )
obiect.write ( 'show ip route'.encode('ascii') + b'\r\n' )
print ( obiect.read_until ( b'free', 2 ) )

obiect.write ( '?'.encode('ascii') + b'\r\n' )
print ( obiect.read_until ( b'free', 2 ) )

obiect.write ( 'show ip interface brief'.encode('ascii') + b'\r\n' )
print ( obiect.read_until ( b'free', 2 ) )

obiect.write ( 'enable'.encode('ascii') + b'\r\n' )
print ( obiect.read_until ( b'free', 2 ) )

obiect.write ( ' show ip bgp 8.8.8.8'.encode('ascii') + b'\r\n' )
print ( obiect.read_until ( b'free', 2 ) )
obiect.write ( 'show users'.encode('ascii') + b'\r\n' )
print ( obiect.read_until ( b'free', 2 ) )

obiect.close ( )
