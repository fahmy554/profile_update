# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
import sys,os
sys.path.append(os.getcwd())
import requests, uuid, time, os
from colorama import init
from termcolor import colored
import urllib3, re, oauth2, json, tweepy, string, sys
from random import choice, randint
import urllib.parse

urllib3.disable_warnings()

quote_plus=urllib.parse.quote_plus
quote=urllib.parse.quote

init()
requests.urllib3.disable_warnings()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def random_char(y=8):
    return ('').join(choice(string.ascii_letters) for x in range(y))




def red(*args):
    text = ''
    for arg in args:
        text += colored(arg, 'red') + ' '

    return text


def yellow(*args):
    text = ''
    for arg in args:
        text += colored(arg, 'yellow') + ' '

    return text


def green(*args):
    text = ''
    for arg in args:
        text += colored(arg, 'green') + ' '

    return text


def cyan(*args):
    text = ''
    for arg in args:
        text += colored(arg, 'cyan') + ' '

    return text


def magenta(*args):
    text = ''
    for arg in args:
        text += colored(arg, 'magenta') + ' '

    return text

import threading
lock=threading.RLock()
def debug(*args):
    with lock:
        txt=' '.join([str(a) for a in args])
        print(txt)

