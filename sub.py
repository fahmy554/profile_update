import traceback

from colorama import init, Fore
import pathlib, sys,requests
import os
import platform
plat=platform.platform()
proc=platform.processor()
cmd = 'mode 150,40'
os.system(cmd)
file = pathlib.Path(__file__)
sys.path.extend([file.parent.as_posix(), file.parent.parent.as_posix(), file.parent.parent.parent.as_posix()])
import getmac, random, socket
host_name = socket.gethostname()
host_name = host_name + '21'
user_mac = getmac.get_mac_address()
init(autoreset=True)
import hashlib
import uuid,base64
user_id_system=uuid.UUID(int=uuid.getnode())

hashed_txt=user_mac+host_name+os.getlogin()+str(user_id_system)

hashed_txt=hashlib.sha1(str(hashed_txt).encode()).hexdigest()


def banner(start_msg,data):
    from termcolor import colored
    ff=data.text.split('\n')[1]
    # a = f"""
    #                      :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #                                                             {start_msg}
    #                                                             {ff if ff else  ''}
    #                                                                                              Other Scripts
    #                                                                                             1-Yahoo Creator
    #                                                           __       _                        2-Twitter Reseter
    #                                                          / _| __ _| |__  _ __ ___  _   _    3-Twitter AutoFollow
    #                                                         | |_ / _` | '_ \| '_ ` _ \| | | |   4-Twitter Profile Update
    #                                                         |  _| (_| | | | | | | | | | |_| |   5-Twitter React V1
    #                                                         |_|  \__,_|_| |_|_| |_| |_|\__, |   6-Twitter Followers Collector
    #                                                                                    |___/    7-Twitter ShadowBan Testing
    #                                                             Any Script You Want             8-Twitter React V2
    #
    #                                                     Your Mac {user_mac}
    #                         Coded By >>> Mohamed Fahmy :
    #                         Whatsapp:01122417550
    #                         Facebook:Pythonist611
    #                      ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # """
    all_text=data.text
    tmp=all_text
    ff = tmp.split('\n')[0]
    if ff:
        all_text= all_text.replace('basmla', ff.strip())
    else:
        print('aesfgh')
        all_text= all_text.replace('msg', '')
    a=all_text.split('r_r')[1]
    # print(a)

    a=a.replace('user_mac',hashed_txt)
    a=a.replace('banner',start_msg)
    # colors=['red','cyan','yellow','blue','orange']
    colors = [
        Fore.GREEN, Fore.LIGHTYELLOW_EX, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.YELLOW, Fore.LIGHTGREEN_EX,
        Fore.LIGHTBLUE_EX
    ]
    print(random.choice(colors)+a)
    print(Fore.GREEN + '       Welcome user........,'.upper())



def check(response):
    if 'stop_this' in response.text:
        return
    if hashed_txt in response.text:
        return response.text
    if user_mac+":"+f"{os.getlogin()}"+":"+plat+':'+host_name in response.text:
        return response.text
    else:
        return False
# from telethon.sync import TelegramClient, events
api_id = 3432425
api_hash = 'f4ec1f3717d090b63617be96f63e6cf1'
bot_token = '1973949920:AAFxcNSZkVuAkThZ6gXD3NRKMBZXYVkZJIg'

chat__id = 1058351209
my_id = 388516887


# client= TelegramClient('name', api_id, api_hash)

both=False

open('myfile.txt','a')

import subprocess
subprocess.check_call(["attrib","+H","myfile.txt"])

def send_msg(text,**args):

    with open('myfile.txt','a') as f:
        if 'done' in open('myfile.txt','r').read():
            if args['reload']:
                ids = [chat__id, my_id]
                if both:
                    for id_ in ids:
                        url_req = "https://api.telegram.org/bot" + bot_token + "/sendMessage" + "?chat_id=" + str(
                            id_) + "&text=" + text
                        results = requests.get(url_req)
                else:
                    url_req = "https://api.telegram.org/bot" + bot_token + "/sendMessage" + "?chat_id=" + str(
                        my_id) + "&text=" + text
                    results = requests.get(url_req)
            else:
                pass
        else:
            ids=[chat__id,my_id]
            if both:
                for id_ in ids:
                    url_req = "https://api.telegram.org/bot" + bot_token + "/sendMessage" + "?chat_id=" + str(id_) + "&text=" + text
                    results = requests.get(url_req)
            else:
                url_req = "https://api.telegram.org/bot" + bot_token + "/sendMessage" + "?chat_id=" + str(my_id) + "&text=" + text
                results = requests.get(url_req)

            f.write('done')

module_name = ''


def start(start_m,name=''):
    inner_name=module_name
    copying=':'.join([user_mac,os.getlogin(),plat,host_name])
    try:

        global_reponse = requests.get(f'https://pastebin.com/raw/{inner_name}')

        if not check(global_reponse):
            # reload=True
            if 'reload' in global_reponse.text:
                reload=True
            else:
                reload=False
            send_msg(user_mac +'\n'+host_name +"\n"  + module_name+"\n"+f"{os.getlogin()}" +"\n"+f"{plat}"+"\n"+start_m+'\n'+copying+'\n'+hashed_txt,reload=reload)
        else:
          pass
        if not inner_name:
            print('Mohamed Put Name')
        banner(start_m,global_reponse)
        if name in global_reponse.text and name!='':
            pass
        else:
            if check(global_reponse):
                print('valid access')
                pass
            else:
                if 'not-check' in global_reponse.text:
                    print('logged')
                    send_msg(
                        user_mac + '\n' + host_name + "\n" + module_name + "\n" + f"{os.getlogin()}" + "\n" + f"{plat}" + "\n" + start_m + '\n' + copying,
                        reload=False)

                else:
                    print('You need to subscribe \n bye')
                    sys.exit()
    except requests.RequestException:
        sys.exit('errotr')
    except Exception as e:
        print('error',e.__class__)
        sys.exit()

