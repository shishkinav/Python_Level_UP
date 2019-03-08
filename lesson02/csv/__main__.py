from chardet.universaldetector import UniversalDetector
import re, csv

'''
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий 
выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и 
формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с 
данными, их открытие и считывание данных. В этой функции из считанных данных 
необходимо с помощью регулярных выражений извлечь значения параметров 

«Изготовитель системы», 
«Название ОС», 
«Код продукта», 
«Тип системы». 

Значения каждого параметра 
поместить в соответствующий список. Должно получиться четыре списка — например, 
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать 
главный список для хранения данных отчета — например, main_data — и поместить в 
него названия столбцов отчета в виде списка: «Изготовитель системы», «Название 
ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в 
виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. 
В этой функции реализовать получение данных через вызов функции get_data(), а 
также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
'''

patterns = {
    'Изготовитель системы': 'Изготовитель\sсистемы:\s+(\w+)\n',
    'Название ОС': 'Название\sОС:\s+([a-zA-Z0-9а-яА-Я \.]*)\n',
    'Код продукта': 'Код продукта:\s+(\w+\-\w+\-\w+\-\w+)\n',
    'Тип системы': 'Тип\sсистемы:\s+(\w+\-\w+\s+\w+)\n'
}

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = [
    list(patterns.keys()),
]

def whatFileCoding(pathFile):
    detector = UniversalDetector()
    with open(pathFile, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result["encoding"]

def get_data(pathFile, patterns):
    with open(pathFile, 'r', encoding=whatFileCoding(pathFile)) as file:
        text = file.readlines()
    tmp_dict = {}
    for row in text:
        for key, pattern in patterns.items():
            if re.findall(pattern, row):
                tmp_dict.update({key: str(*re.findall(pattern, row))})
    return tmp_dict


def write_to_CSV(patterns_list, pathCSVfile):
    for number in range(1,4):
        pathSourceFiles = f'../source_files/info_{number}.txt'
        data = get_data(pathSourceFiles, patterns_list)
        tmp_list = []
        for element in patterns_list.keys():
            tmp_list.append(data[element])
        main_data.append(tmp_list)
        os_prod_list.append(data['Изготовитель системы'])
        os_name_list.append(data['Название ОС'])
        os_code_list.append(data['Код продукта'])
        os_type_list.append(data['Тип системы'])
        with open(pathCSVfile, 'w', encoding='UTF-8') as fileCSV:
            file_writer = csv.writer(fileCSV, quoting=csv.QUOTE_NONNUMERIC)
            for row in main_data:
                file_writer.writerow(row)
    return True

pathCSVfile = '../source_files/result.csv'
if write_to_CSV(patterns, pathCSVfile):
    print(f'Файл CSV успешно создан и сохранён в {pathCSVfile}')

print('Дополнительные списки по заданию:')
print(os_prod_list)
print(os_name_list)
print(os_code_list)
print(os_type_list)