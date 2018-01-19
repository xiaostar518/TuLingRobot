# coding: utf-8

import itchat
import time
import requests
import random

nickName = u'肖潇'
userName = ""


def search_all_friends():
    friendList = itchat.get_friends(update=True)[1:]
    for friend in friendList:
        # 如果是演示目的，把下面的方法改为print即可
        print(friend)
        print("DisplayName: " + friend['DisplayName'])
        print("NickName: " + friend['NickName'])
        print("UserName: " + friend['UserName'])
        print("----------------------")
        time.sleep(.5)


def get_special_friend(nickName):
    friendList = itchat.get_friends(update=True)[1:]
    for friend in friendList:
        if friend['NickName'] == nickName:
            print("NickName: " + friend['NickName'])
            print("UserName: " + friend['UserName'])
            return friend['UserName']


def send_special_friend_message(userName, msg=""):
    if msg != "" and userName != "":
        itchat.send(msg, userName)
    elif msg == "" and userName != "":
        print("msg为null")
    elif msg != "" and userName == "":
        print("msg为:" + msg + '\n' + "userName为null")
    else:
        print("msg为null" + '\n' + "userName为null")

    print('already sent')


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': 'c5ad83b34f4c48a6a58b99613563da66',  # Tuling Key
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')


#
# @itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
# def print_content(msg):
#     return get_response(msg['Text'])

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def get_current_chat_nickName(msg):
    # equals to print(msg['FromUserName'])
    print(msg.fromUserName)
    if msg.fromUserName == userName:
        send_msg = get_response(msg['Text'])
        print(send_msg)
        random_time = random.random() * 5 * 5
        time.sleep(random_time)
        send_special_friend_message(userName, send_msg)


itchat.auto_login(True)

# search_all_friends()
userName = get_special_friend(nickName)

itchat.run()
