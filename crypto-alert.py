import requests
import json
from config import watchedCryptos, endpoint, mailConfig
from sendmail import sendEmail

for crypto in watchedCryptos:
    url = endpoint+crypto["pair"]
    r = requests.get(url)
    rates = json.loads(r.content)
    if float(rates["last"]) < crypto["min"] or float(rates["last"]) > crypto["max"]: 
        print(f"Pair {crypto['pair']} reached value {rates['last']}")
        sendEmail(crypto["pair"], rates["last"], mailConfig)