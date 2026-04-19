import requests

token = input("Paste your GitHub token: ").strip()

r = requests.post(
    "https://api.github.com/repos/gowthm/daily-notification-gold-price/actions/workflows/gold_alert.yaml/dispatches",
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    },
    json={"ref": "main"}
)

if r.status_code == 204:
    print("Success! Check GitHub Actions tab.")
else:
    print(f"Error {r.status_code}: {r.text}")
