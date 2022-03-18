import requests
from pprint import pprint
burp0_url = "https://story-shack-cdn-v2.glitch.me:443/generators/arabic-name-generator/male?count=100"
burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://thestoryshack.com", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://thestoryshack.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,ar;q=0.8", "If-None-Match": "W/\"106-DdzMzwzSVlbyIEabOeAZnjvq3wg\"", "Connection": "close"}
r=requests.get(burp0_url, headers=burp0_headers)


data=r.json()['data']
f_names=[]
l_names=[]
for user in data:
    f_names.append(user['name'])
    l_names.append(user['lastName'])




from random import choice
def generte_name():
    while True:
        name=choice(f_names)
        sname=choice(l_names)
        yield name+' '+sname
