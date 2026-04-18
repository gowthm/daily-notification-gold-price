import requests

bot_token = "8534948823:AAHJyg9ZEF9t40E-7BLKmO4J7OIjtO1ar4w"
chat_id = "1264444084"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
r = requests.post(url, data={"chat_id": chat_id, "text": "Test: Salem 22K Gold = Rs14360/g - bot is working!"})
print("status:", r.status_code)
print("ok:", r.json().get("ok"))
