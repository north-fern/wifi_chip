# main.py
#based on code by Milan!

import machine
import time
import ujson, urequests, network

pin = machine.Pin(0, machine.Pin.OUT)

time.sleep(.5)
pin.value(1)
time.sleep(.5)
pin.value(0)
time.sleep(.5)


def flash(time_flash):
    pin.value(1)
    time.sleep(time_flash)
    pin.value(0)
    time.sleep(time_flash)

flash(1)

uart = machine.UART(1, 115200)

flash(2)

uart.init(115200, bits=8, parity=None, stop=1)
urlBase = "https://api.airtable.com/v0/"

def read_uart():
    reply = uart.read(100)
    if reply != b'' or reply != '':
        reply.decode()
    flash(.1)
    return reply


wifi_flag = False
Get = False
Put = False

while True:
    
    reply = read_uart()
    #command = reply.split()
    #find_command(command)
    #uart.write(command[0])
    flash(.4)
    
    Get = False
    
    if wifi_flag == True:
        #set_wifi()
        wifi_flag = False
    if Get == True:
        #ans = Get_AT(Table, Field)
        #uart.write(ans)
        Get = False
    if Put == True:
        #ans = Put_AT(Table, Field, Value)
        #uart.write(ans)
        Put = False

'''
#function that reads in commands from spike
def read_uart():
    reply = uart.readline()
    reply.decode()
    return reply



#function that takes wifi ssid and password

def set_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, password)
    ans = wifi.isconnected()
    if ans == True:
        uart.write('Wifi Connected')
    else:
        uart.write('Wifi Connect Failed')

#function that takes the api key
def set_up_air_table():
    urlbase = urlBase
    headers = {"Accept":"applicaiton/json", "Content-Type":"application/json","Authorization":"Bearer " + API_Key}
    return urlbase, headers

#put
def Put_AT(Table,Field,Value):
    urlBase, headers = set_up_air_table()
    urlTag = urlBase + Field
    urlValue = urlBase + BaseID + "/" + Table.replace(" ","%20")
    propValue={"records": [{"fields": {  Field: Value}} ]}
    result = ''
    try:
        value = urequests.post(urlValue,headers=headers, json=propValue).text
        data = ujson.loads(value)
        result = data.get("records")[-1].get("id")
    except Exception as e:
        uart.write('put failed')
    return result

#get
def Get_AT(Table,Field):
    urlBase, headers = set_up_air_table()
    urlValue = urlBase + BaseID + "/" + Table.replace(" ","%20") + "?view=Grid%20view"
    result = ''
    try:
        value = urequests.get(urlValue,headers=headers).text
        data = ujson.loads(value)
        result = data.get("records")[-1].get("fields").get(Field)
    except Exception as e:
        uart.write('get failed') 
    return  result


#if statements to sort
def find_command(command):
    if command[0] == 'ssid':
        global ssid = command[1]
        uart.write('ssid set')
    if command[0] == 'pswd':
        global password = command[1]
        uart.write('password set')
        if ssid != '' and password != '':
            global wifi_flag = True:
    if command[0] == 'api_key':
        global API_Key = command[1]
        uart.write('api_key set')
    if command[0] == 'base_id':
        global BaseID = command[1]
        uart.write('base_id set')
    if command[0] == 'table':
        global Table = command[1]
        uart.write('table name set')
    if command[0] == 'field':
        global Field = command[1]
        uart.write('field name set')
    if command[0] == 'put':
        global Value = command[2]
        global Put = True
        uart.write('put value to change set')
    if command[0] == 'get'
        global Get = True
        uart.write('get value now')
    else
        uart.write('invalid command')
    return 


'''    
