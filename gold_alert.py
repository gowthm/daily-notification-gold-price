import cloudscraper
import re
import json, os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def get_gold_price():
    url = "https://www.goodreturns.in/gold-rates/salem.html"
    scraper = cloudscraper.create_scraper()
    res = scraper.get(url)
    match = re.search(r'&#x20b9;([\d,]+)</strong> per gram for 22 karat', res.text)
    if not match:
        raise ValueError("22K gold price not found on page")
    return int(match.group(1).replace(",", ""))

def send_telegram(message):
    import requests
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHAT_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    r = requests.post(url, data={"chat_id": chat_id, "text": message})
    r.raise_for_status()

prev_price = None
if os.path.exists("price.json"):
    with open("price.json") as f:
        prev_price = json.load(f)["price"]

current_price = get_gold_price()

with open("price.json", "w") as f:
    json.dump({"price": current_price}, f)

if prev_price and current_price != prev_price:
    diff = current_price - prev_price
    arrow = "📈 UP" if diff > 0 else "📉 DOWN"
    change_line = f"Change: {arrow} by ₹{abs(diff)}"
else:
    change_line = "No change from last check"

date_str = datetime.now().strftime("%d %b %Y, %I:%M %p")
msg = f"🥇 Salem Gold Price Update\n📅 {date_str}\n22K Gold: ₹{current_price}/g\n{change_line}"

send_telegram(msg)
print(msg)
