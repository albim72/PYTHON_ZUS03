 #Przykład 1: logowanie do switcha przez SSH z netmiko
from netmiko import ConnectHandler

# Dane dostępowe do urządzenia (np. Cisco IOS)
device = {
    'device_type': 'cisco_ios',       # typ urządzenia
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'haslo',
    'secret': 'enable_haslo',         # jeśli potrzebne do trybu enable
}

# Połączenie i przejście w tryb enable
net_connect = ConnectHandler(**device)
net_connect.enable()

# Wykonanie komendy i odczyt odpowiedzi
output = net_connect.send_command('show ip interface brief')
print(output)

# Zakończenie sesji
net_connect.disconnect()


#Przykład 2: Odczyt statusu przez SNMP (pysnmp)

from pysnmp.hlapi import *

for (errorIndication, errorStatus, errorIndex, varBinds) in getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('192.168.1.1', 161)),
        ContextData(),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))):  # sysDescr

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


#Przykład 3: REST API do urządzenia

import requests

url = "http://192.168.1.1/api/interface"
auth = ('admin', 'haslo')
response = requests.get(url, auth=auth)

print(response.json())
