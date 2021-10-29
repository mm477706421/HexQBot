
help_base = ""
help_base += "这里是帮助菜单：\n"
help_base += "0.GitHub开源地址\n"
help_base += "1.Python语句执行\n"
help_base += "2.YYCTF近24h提交\n"
help_base += "3.百度AI识图\n"
help_base += "4.私聊调教对话\n"
help_base += "5.获取一张涩图\n"
help_base += "发送“help-x”获取详细信息~"

help_0 = "GitHub\nhttps://github.com/Am473ur/HexQBot"

help_1 = "发送print(xxx)会执行xxx并回复返回值\n类似的还支持md5()，sha256()，sha512()，b64encode()，b64decode()"
help_2 = "群聊发送关键词YYCTF，回复最近24h平台上的正确提交次数排名"

help_3 = "识图可以选择附加的关键词：\n"
help_3 += "动物、植物、logo、果蔬、菜品、红酒、货币、地点、车"

help_4 = "私聊可以调教对话（已开放）：\n"
help_4 += "-添加记录“关键词1+关键词2”\n-删除记录“rm关键词1+关键词2”\n-关键词1是我接收到的消息\n-关键词2是您希望我做出的回答\n别把加号忘了呀~"
help_5 = "发送 涩图、来张涩图 等关键词即可"

menu = [help_0, help_1, help_2, help_3, help_4, help_5]


def help_menu(msg):
    if msg[:4] != "help":
        return [False]
    if msg == "help":
        return [True, help_base]
    if msg[4] != "-":
        return [True, "请发送help-x，x替换成数字~"]
    choi = msg[5:]
    if choi == "x":
        return [True, "x换成数字呀"]
    if (len(choi) != 1) or (choi not in "0123456"):
        return [True, "现在只有0-6这几个选项啊"]
    return [True, menu[int(choi)]]
