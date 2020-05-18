from functools import wraps
import inspect, re


class Log():
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            self.logger.info(f'Функция {func.__name__} вызвана из '
                             f'модуля {func.__module__} с аргументами:\n'
                             f'args: {args}\nkwargs: {kwargs}. Обращение к декорируемой функции'
                             f'было осуществлено со следующим контекстом {inspect.stack()[1][4]}')
            result = func(*args, **kwargs)
            return result
        return wrap


