#code for setup/get/pull based off of milan's airtable.py
#https://github.com/milandahal213/airtable/blob/master/airtable.py
#thanks milan!!

import ujson, urequests, network
from machine import UART

global ssid = ''
global password = ''
global API_Key = ''
global BaseID = ''
global Table = ''
global wifi_flag = False
global Put = False
global Get = False

uart = UART(1, 115200)
uart.init(115200, bits=8, parity=None, stop=1)
urlBase = "https://api.airtable.com/v0/"

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

def find_command(command):
    if command[0] == 'ssid':
        ssid = command[1]
        uart.write('ssid set')
    if command[0] == 'pswd':
        password = command[1]
        uart.write('password set')
        if ssid != '' and password != '':
            wifi_flag = True:
    if command[0] == 'api_key':
        API_Key = command[1]
        uart.write('api_key set')
    if command[0] == 'base_id':
        BaseID = command[1]
        uart.write('base_id set')
    if command[0] == 'table':
        Table = command[1]
        uart.write('table name set')
    if command[0] == 'field':
        Field = command[1]
        uart.write('field name set')
    if command[0] == 'put':
        global Value = command[2]
        Put = True
        uart.write('put value to change set')
    if command[0] == 'get'
        Get = True
        uart.write('get value now')
    else
        uart.write('invalid command')
    return 


while True:
    reply = read_uart()
    command = reply.split()
    find_command(command)
    if wifi_flag == True:
        set_wifi()
    if Get == True:
        ans = Get_AT(Table, Field)
        uart.write(ans)
        Get = False
    if Put = True:
        ans = Put_AT(Table, Field, Value)
        uart.write(ans)
        Put = False


    