# ═══════════════════════════════════════
# 📁 connection.py - ملف الاتصال
# ═══════════════════════════════════════

import requests
import random
import time
from user_agent import generate_user_agent

def check_twitter(email):
    """التحقق من الإيميل في تويتر"""
    
    headers = {
        'accept': '*/*',
        'accept-language': 'ar',
        'origin': 'https://x.com',
        'referer': 'https://x.com/',
        'user-agent': generate_user_agent()
    }
    
    params = {'email': email}
    
    try:
        response = requests.get('https://api.x.com/i/users/email_available.json', params=params, headers=headers, timeout=10)
        return '"taken":true' in response.text
    except:
        return False
