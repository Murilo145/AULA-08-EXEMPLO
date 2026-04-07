import requests

TOKEN = "8154559594:AAF8JFztQIJS65SZ3bTuf2EcXFS7vBHI8zA"
CHAT_ID = "5229401010"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

r = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "🚀 TESTE FUNCIONANDO"
})

print(r.text)