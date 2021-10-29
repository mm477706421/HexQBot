import os
from random import choice
import base64
from hashlib import md5
def hso_pic(msg):
    if msg in ["来张涩图", "来张色图", "涩图", "色图", "setu", "se图", "ghs"]:
        setu_list = os.listdir("go-cqhttp/data/images/setu")
        if len(setu_list) == 0:
            return [True, "啊这，竟然没有库存了"]
        local_img_url = "[CQ:image,file=setu/"+choice(setu_list)+"]"
        return [True, local_img_url]
    if msg in ["色图库存", "涩图库存", "库存涩图", "色图数量", "涩图数量", "有多少张涩图"]:
        setu_list = os.listdir("go-cqhttp/data/images/setu")
        return [True, "现在一共有{}张涩图~".format(len(setu_list))]
    return [False]

def add_setu(msg,img):
    if ("色图" not in msg) and ("涩图" not in msg):
        return [False]
    img=base64.b64decode(img)
    if img.hex()[:6]=="ffd8ff":
        tail=".jpg"
    elif img.hex()[:6]=="474946":
        tail=".gif"
    elif img.hex()[:6]=="49492a":
        tail=".tif"
    elif img.hex()[:6]=="89504e":
        tail=".png"
    else:
        return [True,"不支持这种格式呀~"]
    open("go-cqhttp/data/images/setu/"+md5(img).hexdigest()+tail,"wb").write(img)
    return [True,"涩图添加成功~"]