import json
import os
import re
import sys
from time import sleep

import requests

from httpapi.send_msg import send_msg

sys.path.append(os.getcwd())

dirr = "app/HexGame/"
api_url = "http://hack.best/admin/challenges"
session = requests.session()
hexgame_admin = json.load(open("./conf/keys_conf.json"))["YYCTFAdmin"]
admins_group = json.load(open(dirr + "settings.json"))["AdminsGroup"]
login_url = json.load(open(dirr + "settings.json"))["login_url"]
sleep_secs = json.load(open(dirr + "settings.json"))["Intervals"]
challenges_solves_url = api_url

header = {
    "Referer": "http://hack.best/login",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}


def login(name, password):
    postUrl = "http://hack.best/login"
    html = session.get(postUrl, headers=header)
    debug1 = open(dirr + "debug1.txt", "w")
    debug1.write(str(html.text).replace("\"", "").replace("\'", ""))
    str1 = str(html.text).replace("\"", "").replace("\'", "")
    nonce = re.findall(
        r"csrfNonce: [0-9a-f]*", str1)[0][11:].replace("\"", "").replace("\'", "")
    debug2 = open(dirr + "debug2.txt", "w")
    debug2.write(str(nonce))
    postData = {
        "name": name,
        "password": password,
        "nonce": nonce,
    }
    res = session.post(postUrl, data=postData, headers=header)
    open(dirr + "login.html", "w").write(res.text)


def send_blood():
    print("function in")
    challenges_solves = json.loads(session.get(challenges_solves_url).text)
    debug3 = open(dirr + "debug3.html", "w")
    debug3.write(session.get(challenges_solves_url).text)
    if not challenges_solves["success"]:
        send_msg(challenges_solves_url + " 访问失败", admins_group, "group")

    challenges = challenges_solves["data"]

    record = open(dirr + "record.txt", "r").read().split("\n")[:-1]
    for challenge in challenges:
        if challenge["solves"] > 3 or challenge["solves"] == 0:
            continue
        solves_url = api_url + "{}/solves".format(challenge["id"])
        solves = session.get(solves_url).text
        if solves[0] != "{":
            send_msg("YYCTF登陆信息失效[CQ,at=1175078221]", admins_group, "group")
            break
        solves = json.loads(solves)["data"]
        NUM = ["一", "二", "三"]
        for i in range(min(3, challenge["solves"])):
            blood = "恭喜{}拿到了{}的{}血～".format(
                solves[i]["name"], challenge["name"], NUM[i])
            send_msg(blood, admins_group, "group")
            temp = "{}<-->{}".format(solves[i]["account_id"], challenge["id"])
            if temp not in record:
                send_msg(blood, admins_group, "group")
                record.append(temp)
        print(solves)
        print(challenge)
    open(dirr + "record.txt", "w").write("".join([i + "\n" for i in record]))


if __name__ == "__main__":
    login(hexgame_admin["username"], hexgame_admin["password"])
    print("Success")
    while True:
        print("Success Test")
        send_blood()
        sleep(sleep_secs)

# https://game.0xctf.com/api/v1/challenges/solves
# {"data":[{"id":1,"name":"Test","solves":0}],"success":true}
# https://game.0xctf.com/api/v1/challenges

'''

'''
