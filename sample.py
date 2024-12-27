import requests
TELEGRAM_API_KEY = "7703010489:AAF_Z5zxHfgEuzYqAgzDZun5obG39fE1p8Q"
url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"
payload = {
    "chat_id": 2011774729,
    "text": "HELOO"
}
response = requests.post(url, json=payload)