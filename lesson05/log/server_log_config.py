import logging, os, sys
from logging.handlers import TimedRotatingFileHandler


path = '../log/'

logname = 'server.log'
logger = logging.getLogger(logname) # создаем регистратор верхнего уровня с именем logname

# Определяем формат сообщений для логирования
_format = logging.Formatter('%(asctime)s - %(levelname)-10s - %(module)s - %(message)s')

# ежедневная ротация лог файла
rotate_server_log = TimedRotatingFileHandler(
    os.path.join(path, 'INFO/', logname),
    when='M',
    interval=1,
    encoding='utf-8'
)
rotate_server_log.setLevel(logging.INFO)
rotate_server_log.setFormatter(_format)

server_log_stream = logging.StreamHandler(sys.stdout)
server_log_stream.setLevel(logging.CRITICAL)
server_log_stream.setFormatter(_format)

logger.addHandler(server_log_stream)
logger.setLevel(logging.CRITICAL)

logger.addHandler(rotate_server_log)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    logger.info('Тестовый запуск логирования')

