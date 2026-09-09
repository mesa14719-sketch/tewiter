

import os,sys,threading
import requests,random
from user_agent import *

OK = 0
BAD = 0



R = '\x1b[38;5;1m'   # أحمر
M = '\x1b[38;5;244m' # رمادي 
L = '\x1b[38;5;10m' #اخضر 


tok =input(f"{L} [{R} TOKEN {L}] :")
os.system("clear")

id =input(f"{L} [{R} ID {L}] :")
os.system("clear")

if not tok or not id:
	print(R+" لازمك تدخل توكن وايدي ")
	sys.exit()


def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{tok}/sendMessage"
        data = {"chat_id": id, "text": message}
        requests.post(url, data=data, timeout=5)
    except:
        pass

     
ibra = "qwertyuioplkjhgfdsamnbvcxz"

while True:
	len = random.randint(3,5)
	email ="".join(random.choice(ibra) for _ in range (len))  + "@yopmail.com"
	
	headers = {
	        'accept': '*/*',
	        'accept-language': 'ar',
	        'origin': 'https://x.com',
	        'referer': 'https://x.com/',
	        'user-agent': str(generate_user_agent())
	    }
	    
	params = {'email': email}
	    
	response = requests.get('https://api.x.com/i/users/email_available.json', params=params, headers=headers).text
	   
	if '"taken":true' in response:
		
		b1 = f" NEW hits Twiter ✅"
		b2 = f" email : {email}"
		b3 = f" Developer : @I_Z_E_E "
		msg = f"{b1}\n{b2}\n{b3}"
		send_telegram(msg)
		
		OK += 1
	else:
		BAD += 1
		
	print(f"\r Good : {OK} | BAD : {BAD} | email : {email}",end="")
		
