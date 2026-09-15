import os
import json
from dotenv import load_dotenv

load_dotenv(".env")

ENVIRONMENT = os.getenv("CRYPTOPULSE_ENV")

CONFIG_FILE = "config/config.json"
with open(CONFIG_FILE, "r") as file:
    # config_data = json.load(file)
    CONFIG = json.load(file)
# print(CONFIG)
# print(CONFIG["project"]["name"])

# print(ENVIRONMENT)


