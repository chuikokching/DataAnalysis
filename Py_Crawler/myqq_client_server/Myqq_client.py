import socket
import json
import threading

client = socket.socket()
client.connect(("127.0.0.1",8888))

user = "ckc1"

#1. Login
login_template = {
    "action":"login",
    "user":user
}
client.send(json.dumps(login_template).encode("utf8"))
res = client.recv(1024)
print(res.decode("utf8"))

#2. 获取在线用户
get_user_template= {
    "action":"list_user"
}
client.send(json.dumps(get_user_template).encode("utf8"))
res = client.recv(1024)
print("当前在线用户：{}".format(res.decode("utf8")))

#3. 获取历史记录
offline_msg_template={
    "action":"history_msg",
    "user":user
}

exit = False
def handle_send():
    while True:
        #1. 随时发送消息
        #2. 有新消息随时接收
        type = input("请输入操作：1. 发送消息 2. Exit 3. 获取在线用户")
        if type not in ["1","2","3"]:
            print("不支持该操作!!")
            type = input("请输入操作：1. 发送消息 2. Exit 3. 获取在线用户")
        elif type == "1":
            to_user = input("请输入发送的用户")
            msg = input("请输入消息：")
            send_data_template={
                "action":"send_msg",
                "to":to_user,
                "from":user,
                "data":msg
            }
            client.send(json.dumps(send_data_template).encode("utf8"))
        elif type == "2":
            exit_template = {
                "action":"exit",
                "user": user
            }
            client.send(json.dumps(exit_template).encode("utf8"))
            exit = True
            client.close()
            break
        elif type == "3":
            get_user_template={
                "action":"list_user"
            }
            client.send(json.dumps(get_user_template).encode("utf8"))


def handle_receive():
    # 处理接收请求
    while True:
        if not exit:
            res = client.recv(1024)
            res = res.decode("utf8")
            try:
                res_json = json.loads(res)
                msg = res_json["data"]
                from_user = res_json["from"]
                print("")
                print("收到来自{}的消息：{}".format(from_user, msg))
            except:
                print("")
                print(res)
        else:
            break



if __name__ == '__main__':
    send_thread = threading.Thread(target=handle_send)
    receive_thread = threading.Thread(target=handle_receive)
    send_thread.start()
    receive_thread.start()