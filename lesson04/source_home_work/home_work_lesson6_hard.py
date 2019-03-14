# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os, re

# объявляем общий класс с единым для всех методом
class People():
    def __init__(self, name, sername):
        self.name = name
        self.sername = sername

    def fullName(self):
        '''
        Метод для возврата Имя Фамилии сотрудника в виде одной строковой переменной
        '''
        return self.name + ' ' + self.sername

# объявляем класс с опорой на файл штатного расписания с нормативами, не забываем наследовать базис
class Worker(People):
    def __init__(self, name, sername, salary, position, normalHours):
        People.__init__(self, name, sername)
        self.salary = salary
        self.position = position
        self.normalHours = normalHours

# объявляем класс с опорой на фактическую отработку в расчетном периоде, не забываем наследовать базис
class workedHours(People):
    def __init__(self, name, sername, hours):
        People.__init__(self, name, sername)
        self.hours = hours

def factSalary(salary, normHours, workedHours):
    '''
        Выполняет расчёт ЗП по salary(ставка сотрудника), normHours (установленная норма часов),
        workedHours(фактическое количество отработанных часов за расчетный период)
    '''
    if workedHours / normHours > 1: # если зафиксирована переработка - сотрудник красавец, получит больше
        return round(float(salary + (salary / normHours) * (workedHours - normHours) * 2), 2)
    else: # если норма часов не выполнена, сотрудник - ленивый)) придется немного снизить уровень его дохода за период
        return round(float(salary - (salary / normHours) * (workedHours - normHours)), 2)

listWorker = [] # список для хранения ссылок на экземпляры класса работников по ШЕ
listWorkHours = [] # список для хранения ссылок на экземпляры класса работников с фактически отработанными часами

# формируем путь ссылки на первый файл с ШЕ
path = os.path.join('data', 'workers')
# открываем файл, перебираем строки и переносим их в свой список
with open(path, 'r', encoding='UTF-8') as file:
    for line in file:   # перебираем все строки файла
        spLine = re.findall('\w+', line) # spLine принимает очищенные от пробелов значения в формате списка
        listWorker.append(Worker(spLine[0], spLine[1], spLine[2], spLine[3], spLine[4])) # создаём список ссылок на создаваемые экземпляры класса

# аналогично прошлому файлу, разбираем фактическую отработку и создаём экземпляры класса
path = os.path.join('data', 'hours_of')
# открываем файл, перебираем строки и переносим их в свой список
with open(path, 'r', encoding='UTF-8') as file:
    for line in file:   # перебираем все строки файла
        spLine = re.findall('\w+', line)
        listWorkHours.append(workedHours(spLine[0], spLine[1], spLine[2])) # создаём список ссылок на создаваемые экземпляры класса

# создаём конечный файл с шапкой новой таблицы, если файл существует заменяем его новым
path = os.path.join('data', 'salaryWorkers')
with open(path, 'w', encoding='UTF-8') as file:
    file.write('{:<10}{:<14}{:<10}\n' .format('Имя', 'Фамилия', 'Выручка'))

# любимая часть кода))) - считаем ЗП для каждого сотрудника
for worker in listWorker: # по очереди перебираем сотрудников по штатному расписанию
    for el in listWorkHours: # сверяем наличие штатного сотрудника в листе фактически отработанно времени за период
        if worker.fullName() == 'Имя Фамилия': # исключаем первую строчку из обработки расчёта
            continue
        if worker.fullName() == el.fullName(): # если нашли соответствующего сотрудника в списке отработанного времени
            # дописываем данные в наш файл
            with open(path, 'a', encoding='UTF-8') as file:
                file.write('{:<10}{:<14}{:<10}\n' .format(worker.name, worker.sername, factSalary(float(worker.salary),\
                                                                        float(worker.normalHours), float(el.hours))))
print('Расчёт завершен, файл Вы можете увидеть в {}.' .format(path))