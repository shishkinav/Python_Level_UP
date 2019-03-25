from socket import *
from lesson06.config import *
import json
from lesson06.LOG import Log
from lesson06.server_log_config import logger


@Log(logger)
def sendMessageClient(msg):
    return msg.encode(ENCODING)


@Log(logger)
def getMessageClient(msg):
    try:
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
    except:
        logger.error('Ошибка выполнения функции getMessageClient')
        logger.critical('Критическая ошибка выполнения функции getMessageClient')


if __name__ == '__main__':
    tcp = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    tcp.bind(('', SERVER_PORT))                # Присваивает порт 7777
    tcp.listen(5)                       # Переходит в режим ожидания запросов;
                                      # одновременно обслуживает не более
                                      # 5 запросов.
    while True:
        try:
            client, addr = tcp.accept()
            if client:
                logger.info(f'Соединение с {addr[0]} - {addr[1]} установлено')
                logger.debug(f'Соединение с {addr[0]} - {addr[1]} установлено')
                logger.warning(f'Соединение с {addr[0]} - {addr[1]} установлено')


            result = getMessageClient(client.recv(1024))
            client.send(sendMessageClient(result))
            client.close()
        except:
            logger.critical('Критическая ошибка исполнения программы')
            client.send(sendMessageClient('Ошибка на стороне сервера'))
            client.close()
