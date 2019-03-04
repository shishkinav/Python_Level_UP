__author__ = 'Шишкин Анатолий Васильевич'

'''
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку
файла по умолчанию. Принудительно открыть файл в формате Unicode и
вывести его содержимое.
'''

import locale
from chardet.universaldetector import UniversalDetector

str_set = ('сетевое программирование',
           'сокет',
           'декоратор')

print(f'Кодировка системы по умолчанию - {locale.getpreferredencoding()}\n')

pathF = 'test_file.txt' # путь до нашего файла

# создаем файл и записываем в него исходные данные
file = open(pathF, 'w')
for line in str_set:
    file.write(f'{line}\n')
file.close()

# выясняем кодировку созданного файла
detector = UniversalDetector()
with open(pathF, 'rb') as file:
    for line in file:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(f'Кодировка созданного файла {pathF} - {detector.result["encoding"]}\n')

# насильно открываем файл в юникоде и читаем
print('читаем файл в UTF-8')
with open(pathF, encoding='utf-8') as file:
    for line in file:
        print(f'\t{line}')

# насильно открываем файл в cp866 и читаем
print('дополнительно хотим прочитать файл в cp866, чтобы посмотреть как это будет выглядеть')
with open(pathF, encoding='cp866') as file:
    for line in file:
        print(f'\t{line}')
