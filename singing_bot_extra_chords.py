import hub, utime

serial = hub.port.B
serial.mode(hub.port.MODE_FULL_DUPLEX)
serial.baud(115200)
power = hub.port.B.pwm(100)

ssid = 'FiOS-9Y9Z9'
pswd = 'tux6789duck210gate'
API_Key = 'keyjYRqlJJ5SLlnrS'
BaseID = 'appWe18qoA5NGrZ9G'
urlBase = "https://api.airtable.com/v0/"
Table = 'Table 1'

#https://pages.mtu.edu/~suits/notefreqs.html
sound_dict = {
    'a4' : 440,
    'b4' : 493,
    'c4' : 523,
    'd4' : 587,
    'e4' : 659,
    'f4' : 698,
    'g4' : 784,
    'a3' : 220,
    'b3' : 247,
    'c3' : 261,
    'd3' : 294,
    'e3' : 329,
    'f3' : 349,
    'g3' : 392,
    'a5' : 880,
    'b5' : 987,
    'c5' : 1046,
    'd5' : 1174,
    'e5' : 1318,
    'f5' : 1396,
    'g5' : 1567

}

serial.write('\r\n')
serial.write('\r\n')
utime.sleep(1)
serial.read(1000)
serial.read(1000)

#based on milan's airtable.py command set

def send_messages(command_set,Field,Value,Table):
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

ans = send_messages('setup','','','')

def extract_command(last_command):
    step_zero = last_command.decode()
    step_one = step_zero.replace('\r\n','')
    step_two = step_one.replace('print(ans)','')
    step_three = step_two.replace('>>>','')
    step_four = step_three.replace(' ','')
    return step_four

print(ans)
ans = send_messages('wifi','','','')
print(ans)

def play_tune(tune):
    #https://pages.mtu.edu/~suits/notefreqs.html
    for i in tune:
        print(i)
        hub.sound.beep(sound_dict[i])
        utime.sleep(.25)

while True:
    Value = ''
    Field = 'abcde'
    ans2 = send_messages('get',Field, Value,'Table 1')
    print(ans2)
    thing = extract_command((ans2[len(ans2)-2]))
    print(thing)
    play_tune(thing)
    serial.write('\r\n')
    trash1 = serial.read(1000)
    serial.write('\r\n')
    trash2 = serial.read(1000)
        