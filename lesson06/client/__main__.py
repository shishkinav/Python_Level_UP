from socket import *
from lesson06.config import *
import re, json, time
from lesson06.client_log_config import logger


def sendMessageServer(msg):
    msg_ = re.split('\s+', msg)
    sendMsg = {
        'command': msg_[0],
        'text': msg_[1:]
    }
    sendMsg = json.dumps(sendMsg)
    logger.info(f'Отправка сообщения на сервер: {sendMsg}')
    return str(sendMsg).encode(ENCODING)


def getMessageServer(response):
    return response.decode(ENCODING)


if __name__ == '__main__':
    tcp = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    tcp.connect((SERVER_ADDR, SERVER_PORT))   # Соединиться с сервером

    while True:

        # logger.info(f'Соединение с {SERVER_ADDR} / {SERVER_PORT} - установлено')
        # tcp.send(sendMessageServer(msg))
        # logger.info(f'Сообщение отправлено на сервер ({SERVER_ADDR} / {SERVER_PORT}: {msg}')
        msg = getMessageServer(tcp.recv(1024))
        logger.info(f'Получено сообщение от сервера ({SERVER_ADDR} / {SERVER_PORT}: {msg}')

    tcp.close()
