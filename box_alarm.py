import hub, utime

serial = hub.port.B
serial.mode(hub.port.MODE_FULL_DUPLEX)
serial.baud(115200)
power = hub.port.B.pwm(100)
force = hub.port.A.device
force.get()[0]

ssid = 'FiOS-9Y9Z9'
pswd = 'tux6789duck210gate'
API_Key = 'keyjYRqlJJ5SLlnrS'
BaseID = 'appWe18qoA5NGrZ9G'
urlBase = "https://api.airtable.com/v0/"
Table = 'Table 1'


serial.write('\r\n')
serial.write('\r\n')
utime.sleep(1)
serial.read(1000)
serial.read(1000)

#based on milan's airtable.py command set
def send_messages(command_set,Field,Value):
    ans = []
    command_set_put = ['headers = {"Accept"',':"applicaiton/json",','"Content-Type":"appli','cation/json","Auth','orization":"Bearer " + "', API_Key,'"}\r\n', 'urlValue ="', urlBase ,'" + "', BaseID, '" + "/" + "', Table.replace(" ","%20"), '"\r\n', 'propValue={"records"',':[{"fields":{"',Field,'":"',Value,'"} } ]}\r\n','val=urequests.post','(urlValue,headers=headers,','json=propValue).text\r\n','data=ujson.loads(val)\r\n','result=data.get(','"records")[-1]','.get("id")\r\n','print(result)\r\n']
    command_set_get = ['headers = {"Accept"',':"applicaiton/json",','"Content-Type":"appli','cation/json","Auth','orization":"Bearer " + "', API_Key,'"}\r\n', 'urlValue ="', urlBase ,'"+"', BaseID, '"+ "/" + "', Table.replace(" ","%20"), '"+"?view=Grid%20view"\r\n', 'val = urequests.get(','urlValue,headers=headers)','.text\r\n', 'data = ujson.loads(val)\r\n','ans = data.get("records")','[-2].get("fields")','.get("',Field,'")\r\n','print(ans)\r\n']
    command_set_setup = ['import network \r\n','import ujson \r\n','import urequests\r\n', 'import os \r\n']
    command_set_wifi = ['wifi=network.WLAN','(network.STA_IF)\r\n','wifi.active(True)\r\n','wifi.connect("', ssid , '","', pswd, '")\r\n','a=wifi.isconnected()\r\n','print(a)\r\n']

    if command_set == 'get':
        command_set_sent = command_set_get
    if command_set == 'put':
        command_set_sent = command_set_put
    if command_set == 'wifi':
        command_set_sent = command_set_wifi
    if command_set == 'setup':
        command_set_sent = command_set_setup

    for i in command_set_sent:
        serial.write(i)
        utime.sleep(.25)
        add1 = serial.read(1000)
        add2 = serial.read(1000)
        ans.append(add1)
        ans.append(add2)
        
    return ans

def get_time():
    time_now= utime.ticks_ms()
    return time_now

ans = send_messages('setup','','')

def extract_command(last_command):
    step_zero = last_command.decode()
    step_one = step_zero.replace('\r\n','')
    step_two = step_one.replace('print(ans)','')
    step_three = step_two.replace('>>>','')
    step_four = step_three.replace(' ','')
    return step_four

print(ans)
ans = send_messages('wifi','','')
print(ans)

while True:
    val = force.get()[0]
    print(val)
    if val > 0:
        time_string = get_time()
        Value = str(time_string)
        Field = 'data2'
        ans2 = send_messages('put',Field, Value)
        print(ans2)
        serial.write('\r\n')
        trash1 = serial.read(1000)
        serial.write('\r\n')
        trash2 = serial.read(1000)
        