
import requests
import random
from colorama import Fore
from time import sleep
from tinydb import TinyDB, Query
import datetime
import os
import json,time

r1 = requests.session()
user = '' 
password = ''

count = 0
def getdate():
    return datetime.datetime.now().date()

db = TinyDB("testdb.json")
User = Query()
def insert(dick):
    db.insert(dick)

def sendbot(bot_message):  
    bot_token = '1800189063:AAHtlifMEOAAZV7kL9J2so-AOUBgwYlelY4'
    bot_chatID = '1375199711'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
rd = "abcdefghijklmnopqrwstuvwxyz1234567890"

def rnduser(length):
    global rd
    chars = rd +'_'    
    us = ''
    for i in range(length):
        us += random.choice(chars)
    return us
    
urlreg = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
headreg = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '360',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=aHzIzwZa2UgxIM2pUpIgKZ9SUVmMnR3R; mid=YGKwAQALAAH73Ys3Niv49h7P1dsA; ig_did=C3712B78-D803-4A15-B989-F44E6EB177A4; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'x-csrftoken': 'aHzIzwZa2UgxIM2pUpIgKZ9SUVmMnR3R',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '35a8a756068b',
    'x-requested-with': 'XMLHttpRequest',

}



def check():
    global password,count
    url = 'https://www.instagram.com/accounts/login/ajax/'
    head = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '365',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=8A544DC5-6022-4645-BA04-DE5D18D66340; ig_nrcb=1; csrftoken=n75Tx22fMwD9YkpcBszvFz2SbYmy1R3S; mid=YNt8YQALAAHpMfzMX5-nq-UvVpPv',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'x-asbd-id': '437806',
            'x-csrftoken': 'n75Tx22fMwD9YkpcBszvFz2SbYmy1R3S',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1cb3c391e22f',
            'x-requested-with': 'XMLHttpRequest'
        }
    data = {
            'username': f'{user}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:0:{password}',
            'queryParams': '{"next":"/accounts/logout/"}',
            'optIntoOneTap': 'false',
            'stopDeletionNonce': '',
            'trustedDeviceRecords': '{}'
        }
    Log = r1.post(url, data=data, headers=head)
    if ('"userId"') in Log.text:
  
        print('[+] Done Login !')
    
        while True:
        #    email = random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+'@gmail'
            password = random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)+random.choice(rd)
            f = open('input.txt', 'r')
            for owo in f:
                xowo = owo.split("\n")[0].split(' ')[0]
                sleep(1)
                datareg = {
                    'email': 'hasanalmterowo11@gmail.com',
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:9:nnsdhff44',
                    'username': xowo,
                    'first_name': 'greedy ass',
                    'client_id': 'YGKwAQALAAH73Ys3Niv49h7P1dsA',
                    'seamless_login_enabled': '1',
                    'opt_into_one_tap': 'false',
                }
                reg = requests.post(urlreg, data=datareg, headers=headreg).text
                
                js = json.loads(reg)
                err = js['errors']
                print(err['username'][0]['code'])
                count += 1
                print(count)
                if not "username" in err:
                    
                    u = r1.get(f"https://www.instagram.com/{user}/?__a=1")
                    #idq = str(u.json()["graphql"]["user"]["id"])
                    urlf = 'https://www.instagram.com/accounts/edit/?__a=1'
                    ee = r1.get(urlf)
                    fi = str(ee.json()["form_data"]["first_name"])
                    bi = str(ee.json()["form_data"]["biography"])
                    e = str(ee.json()["form_data"]["email"])
                    ph = str(ee.json()["form_data"]["phone_number"])
                   # rur = Log.cookies['rur']
                    ig_did = Log.cookies['ds_user_id']
                    csrftoken = Log.cookies['csrftoken']
                    sessionid = Log.cookies['sessionid']
                    urlpee = 'https://www.instagram.com/accounts/edit/'
            
                    heade = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                        'content-length': '135',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': f'ig_did={ig_did}; ig_nrcb=1; mid=YNt8YQALAAHpMfzMX5-nq-UvVpPv; csrftoken={csrftoken}; ds_user_id={ig_did}; sessionid={sessionid}; rur="VLL"',
                        'origin': 'https://www.instagram.com',
                        'referer': 'https://www.instagram.com/accounts/edit/',
                        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                        'x-asbd-id': '437806',
                        'x-csrftoken': f'{csrftoken}',
                        'x-ig-app-id': '936619743392459',
                        'x-ig-www-claim': 'hmac.AR04gdj-gOnKqDQw6vN3YPIMMgsN3x-s19fgRfD8YFAz17sN',
                        'x-instagram-ajax': '1cb3c391e22f',
                        'x-requested-with': 'XMLHttpRequest'
                    }
                    
                    
                    datae = {
                        'first_name': f'{fi}1',
                        'email': f'{e}',
                        'username': xowo,
                        'phone_number': f'{ph}',
                        'biography': f'{bi}',
                        'external_url': '',
                        'chaining_enabled': 'on'
                }
                    try:
                      
                        x = r1.post(urlpee, data=datae, headers=heade).text
                        sendbot(f'FUC*ED {xowo} | After: {count}')
                      
                
                    except Exception as ero:
                       print(f'Failed {xowo}',ero)
                elif 'username_is_taken' in err['username'][0]['code']:
                
               
                    print(xowo)
              
    elif ('"checkpoint_required"') in Log.text:
        print('[#] Secure !, please Unlock the secure account')
        
            #    url3 = f'https://api.telegram.org/bot1802989656:AAF5kXslAwh3TVVDd7heK6BD0vXZ52wmwZ8/sendMessage?chat_id=1375199711&text= Secure !'
             #   r1.get(url3)
        
    elif ('"authenticated":false') in Log.text:
                print(Log.text)
                print('[-] Login Fail !')
    else:
                print('[$] Error !')
                print(Log.text)
        
    
check()
