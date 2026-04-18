# Salem Gold Price Alert 🥇

Automatically fetches the live 22K gold price for Salem and sends a Telegram notification twice a day — at **10:00 AM IST** and **3:00 PM IST**.

## How It Works

1. GitHub Actions triggers the script on a schedule
2. `gold_alert.py` scrapes the current 22K gold rate from [goodreturns.in](https://www.goodreturns.in/gold-rates/salem.html)
3. Compares it with the previous price stored in `price.json`
4. Sends a Telegram message with the current price, date, and change info
5. Commits the updated `price.json` back to the repo to persist state

### Sample Notification

```
🥇 Salem Gold Price Update
📅 18 Apr 2026, 10:00 AM
22K Gold: ₹14360/g
Change: 📈 UP by ₹120
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/daily-notification-gold-price.git
cd daily-notification-gold-price
```

### 2. Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` and follow the steps
3. Copy the **Bot Token** you receive

### 3. Get your Chat ID

1. Search for your bot in Telegram and send `/start`
2. Open this URL in your browser (replace `<BOT_TOKEN>`):
   ```
   https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
   ```
3. Find `"chat": {"id": ...}` — that number is your **Chat ID**

### 4. Add GitHub Secrets

Go to your repo → **Settings → Secrets and variables → Actions → New repository secret**

| Secret Name | Value |
|-------------|-------|
| `BOT_TOKEN` | Your Telegram bot token |
| `CHAT_ID` | Your Telegram chat ID (numeric) |

### 5. Run locally (optional)

Create a `.env` file:

```env
BOT_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
```

Install dependencies and run:

```bash
uv run python gold_alert.py
```

---

## Project Structure

```
├── gold_alert.py                   # Main script
├── price.json                      # Stores last fetched price (auto-updated)
├── .env                            # Local secrets (never committed)
├── pyproject.toml                  # Python dependencies
└── .github/
    └── workflows/
        └── gold_alert.yaml         # GitHub Actions schedule
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `cloudscraper` | Bypasses Cloudflare protection on the gold price site |
| `requests` | Sends Telegram API calls |
| `python-dotenv` | Loads `.env` file for local runs |

## Schedule

| Run | IST | UTC (cron) |
|-----|-----|------------|
| Morning | 10:00 AM | `30 4 * * *` |
| Afternoon | 3:00 PM | `30 9 * * *` |

You can also trigger a manual run from **GitHub → Actions → Gold Price Alert → Run workflow**.
