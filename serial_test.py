'''
Code to test serial communications to verify a 32-35 bit
character limit on serial.write commands

'''


import hub, utime
serial = hub.port.B
serial.mode(hub.port.MODE_FULL_DUPLEX)
serial.baud(115200)
a = serial.read(1000)
serial.write('abcdefghijklmnopqrstuvwxyz1234567890!?#$%^&')
#serial.read(1000)
utime.sleep(.55)
b = serial.read(1000)
c = serial.read(1000)
d = serial.read(1000)
e = serial.read(1000)
print(a)
print(b)
print(c)
print(d)
print(e)


'''
response: 

b''
b'abcdefghijklmnopqrstuvwxyz123456789'
b''
b''
b''

'''