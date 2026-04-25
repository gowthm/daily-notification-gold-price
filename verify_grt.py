import sys, cloudscraper, re
sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.grtjewels.com/"
scraper = cloudscraper.create_scraper()
res = scraper.get(url)
match = re.search(r'GOLD 22 KT/1g\s*-\s*₹\s*([\d,]+)', res.text)
if match:
    price = int(match.group(1).replace(',', ''))
    print(f"SUCCESS: 22K Gold price = Rs.{price}/g")
else:
    print("FAILED: no match")
