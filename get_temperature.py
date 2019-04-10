import hashlib
import uuid
import requests
import json

password = #password
p = hashlib.md5(password.encode('utf-8')).hexdigest()
UUID = hashlib.md5(str(uuid.getnode()).encode('utf-8')).hexdigest()
MYNAME = #login
MD5HASH = hashlib.md5((UUID+p).encode('utf-8')).hexdigest() 
API_KEY = #apikey
DEVICE_ID = #device id
url_api = 'http://narodmon.ru/'

#logon
r = requests.post(url_api, data={"cmd":"userLogon","login":MYNAME,"hash":MD5HASH,"uuid":UUID,"api_key":API_KEY,"lang":"ru"})

#Indicators of the device
#resp = requests.get('http://narodmon.ru/api/sensorsOnDevice?id='+DEVICE_ID+'&uuid='+UUID+'&api_key='+API_KEY+'&lang=ru').json()
#temp_all = 'Total temperature: ' + str(resp["sensors"][0]["value"])+resp["sensors"][0]["unit"]

#Ответ сервера:
#{"sensors":[{"id":1,"type":0,"value":0,"time":1234567890,"changed":1234567890,"trend":0},{..}]}

resp = requests.get('http://narodmon.ru/api/sensorsValues?sensors='+DEVICE_ID+'&uuid='+UUID+'&api_key='+API_KEY).json()
temp_all = 'Total temperature: ' + str(resp["sensors"][0]["value"])
print(temp_all)
