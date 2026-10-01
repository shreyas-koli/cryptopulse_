import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("COINMARKETCAP_API_KEY")

URL = "https://pro-api.coinmarketcap.com/v3/cryptocurrency/listings/latest"

headers = {
    "Accept": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY
}

params = {
    "start": 1,
    "limit": 3,
    "convert": "USD"
}


response = requests.get(
    URL,
    headers=headers,
    params=params
)

print("HTTP Status:", response.status_code)

data = response.json()

print("\nAPI Response:")
print(data)