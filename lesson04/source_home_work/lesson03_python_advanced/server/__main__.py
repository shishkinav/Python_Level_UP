from socket import *
from lesson03.config import *
import json


def sendMessageClient(msg):
    return msg.encode(ENCODING)

def getMessageClient(msg):
    msg_ = msg.decode(ENCODING)
    msg = json.loads(msg_)
    if msg['command'] == 'сервер':
        return 'туточки я'
    elif msg['command'] == 'погода' and msg['text'] == ['волгоград']:
        return 'сухо и тихо'
    elif msg['command'] == 'help':
        return '''
Доступные команды:
    сервер - чтобы понять откликается ли сервер
    погода волгоград - чтобы узнать погоду в волгограде
    help - получение справки по доступным командам
            '''
    else:
        return 'введите help чтобы получить справку по командам'

if __name__ == '__main__':
    tcp = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    tcp.bind(('', SERVER_PORT))                # Присваивает порт 7777
    tcp.listen(5)                       # Переходит в режим ожидания запросов;
                                      # одновременно обслуживает не более
                                      # 5 запросов.
    while True:
        client, addr = tcp.accept()
        result = getMessageClient(client.recv(1024))
        client.send(sendMessageClient(result))
        client.close()