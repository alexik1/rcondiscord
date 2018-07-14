import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import string

#------------panel main test-----
payload = {'command': 'status', 'ip': '162.244.55.91','key':'485jvyro47cd','password':'hw4dm1nJ@ck','port':'64234'}
r = requests.get("http://servers.miscreatedgame.com/api/rcon_client.py", params=payload)

str = str(r.text)
str = str.replace("Server Status:", '')
str = str.replace("name:", '')
str = str.replace("gamerules: Miscreated", '')
str = str.replace("next ",'')
str = str.replace("in",'')
str = str.replace("round time remag: 0:00",'')
str = str.replace('ip: Server50009', '')
str = str.replace('version: 0.1.1.1972', '')
str = str.replace('level: Multiplayer/islands', '')
str = str.replace('round time remaining: 0:00', '')


str = str.replace('uptime:', 'Online for:')
str = str.replace('players:', 'How many Players Online:')
str = str.replace('time:', 'Ingame Clock:')
str = str.replace('restart :', 'Remaining Time until Restart:')

print(str)

#----------------publictest----------
import json
import requests
from lxml import html


#payload = {'ip': '162.244.55.91','port':'64232'}
#r = requests.get("http://servers.miscreatedgame.com/api/server_info.py", params=payload)

#data = r.json()

#print("Server Name: " + data['name'])
#print("Players Online: " + data['players'])
#print("Server Clock: " + data['time'])
#print("Whitelisted? (If Yes-1 , if No-2): " + data['whiteListed'])

