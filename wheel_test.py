# wheel test

import hub, utime

serial = hub.port.B
serial.mode(hub.port.MODE_FULL_DUPLEX)
serial.baud(115200)
power = hub.port.B.pwm(100)
test = hub.port.A.motor
test.mode(2)




ssid = 'FiOS-9Y9Z9'
pswd = 'tux6789duck210gate'
API_Key = 'keyjYRqlJJ5SLlnrS'
BaseID = 'appWe18qoA5NGrZ9G'
urlBase = "https://api.airtable.com/v0/"
Table = 'Table 1'
Field = 'data2'
Value = 'SpikeSaysHi!'


serial.write('\r\n')
serial.write('\r\n')
utime.sleep(1)
serial.read(1000)
serial.read(1000)
def send_messages(command_set):
    ans = []
    for i in command_set:
        serial.write(i)
        utime.sleep(.25)
        add = serial.read(1000)
        new = add.decode()
        new = new.replace('>>>',"")
        simpl = new.replace('\r\n',' ')
        ans.append(simpl)
    return ans


#based on milan's airtable.py command set
command_set_setup = ['import network \r\n','import ujson \r\n','import urequests\r\n']

command_set_put = ['headers = {"Accept"',':"applicaiton/json",','"Content-Type":"appli','cation/json","Auth','orization":"Bearer " + "', API_Key,'"}\r\n', 'urlValue ="', urlBase ,'" + "', BaseID, '" + "/" + "', Table.replace(" ","%20"), '"\r\n', 'propValue={"records"',':[{"fields":{"',Field,'":"',Value,'"} } ]}\r\n','val=urequests.post','(urlValue,headers=headers,','json=propValue).text\r\n','data=ujson.loads(val)\r\n','result=data.get(','"records")[-1]','.get("id")\r\n','print(result)\r\n']

command_set_get = ['headers = {"Accept"',':"applicaiton/json",','"Content-Type":"appli','cation/json","Auth','orization":"Bearer " + "', API_Key,'"}\r\n', 'urlValue ="', urlBase ,'"+"', BaseID, '"+ "/" + "', Table.replace(" ","%20"), '"+"?view=Grid%20view"\r\n', 'val = urequests.get(','urlValue,headers=headers)','.text\r\n', 'data = ujson.loads(val)\r\n','ans = data.get("records")','[-1].get("fields")','.get("',Field,'")\r\n','print(ans)\r\n']

command_set_wifi = ['wifi=network.WLAN','(network.STA_IF)\r\n','wifi.active(True)\r\n','wifi.connect("', ssid , '","', pswd, '")\r\n','a=wifi.isconnected()\r\n','print(a)\r\n']


ans = send_messages(command_set_setup)

print(ans)
ans = send_messages(command_set_wifi)
print(ans)
while True:
    ans2 = send_messages(command_set_get)
    leng = len(ans2)
    reply = ans2(leng-1)
    sort = reply.replace('print(a)','')
    print(sort)
    if sort == '1':
        motor.pwm(50)

    serial.write('\r\n')
    serial.read(1000)