# Ex 802
# NTP (ntplib)
# InfoAcademy PF 2016-05-27

import time

import ntplib

ob = ntplib.NTPClient ()

r = ob.request ( "3.ro.pool.ntp.org", 2, 123, 5 )
time.ctime ( r.tx_time )

# Servere ntp Romania: 0.ro.pool.ntp.org;	1.ro.pool.ntp.org;	2.ro.pool.ntp.org;	3.ro.pool.ntp.org
# Lista servere din toata lumea http://support.ntp.org/bin/view/Servers/StratumOneTimeServers
# (click pe campul ISO)

v = ob.request ( 'ts2.aco.net', 2, 123, 10 )  			# Ex: AUSTRIA, VIENA
time.ctime ( v.tx_time )

f = None

if True:
    print(time.ctime ( ob.request ( 'ts2.aco.net', 2, 123, 10 ).tx_time ))
    print(time.ctime ( ob.request ( "3.ro.pool.ntp.org", 2, 123, 5 ).tx_time ))

if time.ctime ( ob.request ( 'ts2.aco.net', 2, 123, 10 ).tx_time) == \
        time.ctime ( ob.request ( "3.ro.pool.ntp.org", 2, 123, 5 ).tx_time ):
    print('Ceasuri sincronizate!')