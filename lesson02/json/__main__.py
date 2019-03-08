import datetime, json

'''
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON 
с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. 
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — 
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). 
Функция должна предусматривать запись данных в виде словаря в файл orders.json. 
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей 
в нее значений каждого параметра.
'''

def write_order_to_json(pathFile, item, quantity, price, buyer):
    try:
        with open(pathFile, encoding='utf-8') as f_n:
            # print(f_n.read())
            content = f_n.read()

    except FileNotFoundError:
        with open(pathFile, 'w', encoding='utf-8') as f_n:
            json.dump({"orders": []}, f_n)

    with open(pathFile, encoding='utf-8') as f_n:
        # print(f_n.read())
        content = f_n.read()
        dict_to_json = json.loads(content)
    with open(pathFile, 'w', encoding='utf-8') as f_n:
        dict_to_json['orders'].append(
            {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer,
             'date': str(datetime.datetime.today())})
        json.dump(dict_to_json, f_n, sort_keys=True, indent=4)



pathFile = '../source_files/orders.json' # путь корректен для запуска на исполнение этого скрипта
# если запускать через терминал как команду "python json", то нужно путь изменить на 'source_files/orders.json'
# порядок передаваемых переменных товар (item), количество (quantity), цена (price), покупатель (buyer)
write_order_to_json(pathFile, 'Скрепки', 10, 34.70, 'Samsung')
write_order_to_json(pathFile, 'Футболки', 5, 166.30, 'Алгоритмика')
write_order_to_json(pathFile, 'Листовки', 1000, 14.20, 'Комитет образования')

with open(pathFile) as f_n:
    f_n_content = f_n.read()
    print(f_n_content)
    obj = json.loads(f_n_content)
    for order in obj['orders']:
        print(f'Покупатель {order["buyer"]} заказал {order["item"]} в количестве '
              f'{order["quantity"]} по стоимости {order["price"]}. Заказ оформлен {order["date"]}')