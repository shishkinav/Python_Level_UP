from socket import *
from lesson06.config import *
import json
from lesson06.LOG import Log
from lesson06.server_log_config import logger
import select, time


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


def listen_socket(address):
    '''
    функция прослушки порта
    '''
    tcp = socket(AF_INET, SOCK_STREAM)
    tcp.bind(address)
    tcp.listen(5)
    tcp.settimeout(0.2)
    return tcp


def mainloop():
    '''
    Основной цикл обработки запросов
    '''
    address = (SERVER_ADDR, SERVER_PORT)
    clients = []
    tcp = listen_socket(address)
    while True:
        try:
            conn, addr = tcp.accept()
        except OSError as e:
            pass
        else:
            logger.info(f'Получен запрос на соединение с {str(addr)}')
            clients.append(conn)
        finally:
            w = []
            try:
                r, w, e = select.select([], clients, [], 0)
            except Exception as e:
                pass
            for s_client in w:
                timestr = time.ctime(time.time()) + '\n'
                try:
                    s_client.send(sendMessageClient(timestr))
                except:
                    logger.info(f'Клиент {str(s_client)} отключился и был удален.')
                    clients.remove(s_client)


if __name__ == '__main__':

    print('Сервер запущен')
    mainloop()
