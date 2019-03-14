from socket import *
from lesson03.config import *
import re, json, time

def sendMessageServer(msg):
    msg_ = re.split('\s+', msg)
    sendMsg = {
        'command': msg_[0],
        'text': msg_[1:]
    }
    sendMsg = json.dumps(sendMsg)
    return str(sendMsg).encode(ENCODING)

def getMessageServer(response):
    return response.decode(ENCODING)


if __name__ == '__main__':

    messages = [
        'сервер ты меня слушаешь',
        'погода волгоград',
        'забей',
        'help'
    ]
    for msg in messages:
        tcp = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
        tcp.connect((SERVER_ADDR, SERVER_PORT))   # Соединиться с сервером
        tcp.send(sendMessageServer(msg))
        print(getMessageServer(tcp.recv(1024)))
        tcp.close()
        time.sleep(2)