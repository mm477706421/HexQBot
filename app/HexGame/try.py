import json
import requests
import re
# from httpapi.send_msg import send_msg
import sys
import os
from time import sleep
sys.path.append(os.getcwd())

dirr = "app/HexGame/"
api_url="http://hack.best/admin/submissions/correct"
session = requests.session()
hexgame_admin = json.load(open("./conf/keys_conf.json"))["YYCTFAdmin"]
admins_group = json.load(open(dirr+"settings.json"))["AdminsGroup"]
login_url = json.load(open(dirr+"settings.json"))["login_url"]
sleep_secs = json.load(open(dirr+"settings.json"))["Intervals"]
challenges_solves_url = api_url

def login(name,password):
    html = requests.get(login_url)
    print(html.text)

login("BOT","3a8G4r_e8g")