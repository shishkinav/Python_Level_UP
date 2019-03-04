__author__ = 'Шишкин Анатолий Васильевич'
'''
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
результаты из байтового в строковый тип на кириллице.
'''

import subprocess, locale, os, datetime


def pingSite(site):
    '''
    функция по переданному адресу сайта подстраивается под ОС и проводит ping в 4 шага,
    выводит результат в консоль и записывает в лог-файл
    '''
    if os.name == 'nt':
        args = ['ping', site]
    elif os.name == 'posix':
        args = ['ping', '-c', '4', site]
    else:
        print('Извините, но мы ещё не научились работать с вашей операционной системой!')
        return

    with open(f'{pathLog}{site}_log', 'w', encoding='utf-8') as logFile:
        logFile.write(f'Пинг произведен {datetime.datetime.today()}\n\n')
        subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in subproc_ping.stdout:
            if locale.getpreferredencoding() == 'UTF-8':
                print(line.decode('utf-8'))
                logFile.write(line.decode('utf-8'))
            else:
                print(line.decode(locale.getpreferredencoding()).encode('utf-8').decode('utf-8'))
                logFile.write(line.decode(locale.getpreferredencoding()).encode('utf-8').decode('utf-8'))

# список сайтов, которые нужно пропинговать
sites_list = ['yandex.ru',
              'youtube.com',
              'geekbrains.ru']

# путь до папки с хранящимися логами
pathLog = './data/'

print('\n----------\n')
# собственно перебор всех заданных сайтов и проведение пинга
for site in sites_list:
    print(f'Пингуем сайт {site}:\n')
    pingSite(site)
    print('\n----------\n')