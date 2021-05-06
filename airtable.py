'''
callable python class to use the airtablef
functions and the wifi breakoutboard

makes things easier for people to use (hopefully)


'''

import hub, utime

class Airtable:
    urlBase = "https://api.airtable.com/v0/"
    command_set_put = ['headers = {"Accept"',':"applicaiton/json",','"Content-Type":"appli','cation/json","Auth','orization":"Bearer " + "', self.api_key,'"}\r\n', 'urlValue ="', urlBase ,'" + "', self.base_id, '" + "/" + "', Table.replace(" ","%20"), '"\r\n', 'propValue={"records"',':[{"fields":{"',Field,'":"',Value,'"} } ]}\r\n','val=urequests.post','(urlValue,headers=headers,','json=propValue).text\r\n','data=ujson.loads(val)\r\n','result=data.get(','"records")[-1]','.get("id")\r\n','print(result)\r\n']
    command_set_get = ['headers = {"Accept"',':"applicaiton/json",','"Content-Type":"appli','cation/json","Auth','orization":"Bearer " + "', self.api_key,'"}\r\n', 'urlValue ="', urlBase ,'"+"', self.base_id, '"+ "/" + "', Table.replace(" ","%20"), '"+"?view=Grid%20view"\r\n', 'val = urequests.get(','urlValue,headers=headers)','.text\r\n', 'data = ujson.loads(val)\r\n','ans = data.get("records")','[-1].get("fields")','.get("',Field,'")\r\n','print(ans)\r\n']
    command_set_setup = ['import network \r\n','import ujson \r\n','import urequests\r\n', 'import os \r\n']
    command_set_wifi = ['wifi=network.WLAN','(network.STA_IF)\r\n','wifi.active(True)\r\n','wifi.connect("', self.ssid , '","', self.pswd, '")\r\n','a=wifi.isconnected()\r\n','print(a)\r\n']

    def__init__(self):
    self.data = []

    def ssid(self, ssid):
        self.ssid = ssid
    
    def pswd(self, pswd):
        self.pswd = pswd

    def api_key(self, api_key):
        self.api_key = api_key

    def base_id(self, base_id):
        self.base_id = base_id
    
    def get(self, Table, Field):
        ans = []
        command_set_sent = self.command_set_get
        for i in command_set_sent:
            serial.write(i)
            utime.sleep(.25)
            add1 = serial.read(1000)
            add2 = serial.read(1000)
            ans.append(add1)
            ans.append(add2)
        
        return ans
    
    def wifi(self):
        ans1 = []
        ans2 = []
        command_set_sent = self.command_set_setup
        for i in command_set_sent:
            serial.write(i)
            utime.sleep(.25)
            add1 = serial.read(1000)
            add2 = serial.read(1000)
            ans1.append(add1)
            ans1.append(add2)

        command_set_sent2 = self.command_set_wifi
        for i in command_set_sent2:
            serial.write(i)
            utime.sleep(.25)
            add1 = serial.read(1000)
            add2 = serial.read(1000)
            ans2.append(add1)
            ans2.append(add2)
        
        return ans1, ans2
    
    def put(self, Table, Field, Value):
        ans = []
        command_set_sent = self.command_set_put
        for i in command_set_sent:
            serial.write(i)
            utime.sleep(.25)
            add1 = serial.read(1000)
            add2 = serial.read(1000)
            ans.append(add1)
            ans.append(add2)
        
        return ans

