from bs4 import BeautifulSoup
import datetime
import requests
import http.cookiejar as cookielib
import re
import time
import json

session = requests.session()
hexctf_admin = json.load(open("./conf/keys_conf.json"))["YYCTFAdmin"]

dirr = "app/HexCTF_Spider/"


def get_time():
    local_time = [i for i in time.localtime()][:5]
    return local_time


def is_right_time(t, Date):
    t = [int(t[0:4]), int(t[5:7]), int(t[8:10]), int(t[11:13]), int(t[14:16])]
    timea = datetime.datetime(t[0], t[1], t[2], t[3], t[4])
    timeb = datetime.datetime(
        Date[0], Date[1], Date[2], Date[3], Date[4])  # 晚上 9 点
    if ((timeb - timea).total_seconds() / 3600) < 24:  # 相差 24 小时
        return True
    return False


header = {
    "Referer": "http://hack.best/login",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}


def get_page_num(html_txt):
    text = [int(i[5:]) for i in re.findall(r"page=[0-9]*", html_txt)]
    return max(text)


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


def download_url(num):
    html = session.get("http://hack.best/admin/submissions/correct?page={}".format(num), headers=header)
    open(dirr + "debug.log", "w").write("Test1")
    open(dirr + "page{}.html".format(num), "w").write(html.text)


def html_parser(text, Date, usr_data):
    soup = BeautifulSoup(text, 'html.parser')
    text = (soup.find_all('tr'))[1:]
    debug3 = open(dirr + "debug3.txt", "w")
    for temp in text:
        record = temp.find_all('a')
        username = (re.findall(r"\">[\s\S]*</a>,", str(record)))[0][2:-5].replace("								",
                                                                                  "")
        record = str((temp.find_all('span'))[0])[17:-9]
        debug3.write(username + "\n" + record)
        if not is_right_time(record, Date):
            return False
        record = temp.find_all('a')
        if username not in usr_data:
            usr_data[username] = [1, 0]  # {"username" : [题目数量,总得分数]}
        else:
            usr_data[username][0] += 1
            usr_data[username][1] += 0
    debug3.write("Yes")
    return True


def start_spider():
    usr_data = {}
    data_file = open(dirr + "today_data.txt", "w")
    Date = get_time()[:5]
    debug = open(dirr + "debug.log", "a")
    login(hexctf_admin["username"], hexctf_admin["password"])
    download_url(1)
    html = open(dirr + "page1.html").read()
    page_num = get_page_num(html)
    for page in range(1, page_num + 1):
        download_url(page)
        html = open(dirr + "page{}.html".format(page)).read()
        if not html_parser(html, Date, usr_data):
            break
    for i, j in enumerate(usr_data):
        data_file.writelines(
            j.replace("							", "").replace("\n,", ",").replace("\n", "") + "," + str(usr_data[j][0]) + "\n")
    data_file.close()
