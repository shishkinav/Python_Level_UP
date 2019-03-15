__author__ = 'Шишкин Анатолий Васильевич'
'''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode).
'''
print('\n-----Преобразование строковых в байтовые -----\n')

byte_list = []
str_list = ('разработка',
            'администрирование',
            'protocol',
            'standard')
for progr in str_list:
    byte_list.append(progr.encode('utf-8'))
    print(f'{progr} - {type(progr)} - {len(progr)}')
print(f'\nПосле преобразования в байтовое представление элементы выглядят следующим образом:')
for element in byte_list:
    print(element)

print('\n-----из байтового представления в строковое-----\n')

strok_list = []
for progr in byte_list:
    strok_list.append(progr.decode('utf-8'))
    print(f'{progr} - {type(progr)} - {len(progr)}')

print(f'\nПосле преобразования в строковое представление элементы выглядят следующим образом:')
for element in strok_list:
    print(element)