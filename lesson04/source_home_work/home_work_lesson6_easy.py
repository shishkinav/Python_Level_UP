# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы / done
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.") / done
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы) / done
# 4. Узнать ФИО родителей указанного ученика / done
# 5. Получить список всех Учителей, преподающих в указанном классе / done

# создаём полный список классов в школе
listClass_rooms = list(map(lambda x: [str(x) + ' А', str(x) + ' Б', str(x) + ' В'], [el for el in range(1, 12)]))
# объявляем список для хранения данных по учащимся
listStudents = []
# объявляем словарь для хранения информации предмет - преподаватель
dictSubjects_Teacher = {}

# определяем исходные данные в соответствии с учебной программой, в каких классах необходимо проходить какие предметы
dictSubjectsClasses = {
    '1': ['Математика', 'Русский язык', 'Окружающий мир'],
    '2': ['Математика', 'Русский язык', 'Немецкий язык'],
    '3': ['Математика', 'Русский язык', 'Немецкий язык', 'Программирование'],
    '4': ['Математика'],
    '5': ['Математика'],
    '6': ['Математика'],
    '7': ['Математика'],
    '8': ['Математика'],
    '9': ['Математика'],
    '10': ['Математика'],
    '11': ['Математика']
                        }

# создаём базовый класс людей с общими атрибутами и базовыми методами
class People:
    def __init__(self, name, name2, sername):
        self._name = name
        self._name2 = name2
        self._sername = sername

    def full_name(self):
        return self._sername + ' ' + self._name + ' ' + self._name2

# создаём класс для последующего объявления учащихся, предок - класс People
class Student(People):
    def __init__(self, name, name2, sername, class_room, mother, father):
        People.__init__(self, name, name2, sername) # н
        self.class_room = class_room
        self.mother = mother
        self.father = father
        listStudents.append([name, name2, sername, class_room, mother, father]) # при создании новых экземпляров данные будут вносится в общий список

# создаём класс для ввода в программу преподавателей
class Teacher(People):
    def __init__(self, name, name2, sername, subject):
        People.__init__(self, name, name2, sername)
        self.subject = subject
        self.checkSubject(self.subject, self.full_name()) # сразу же проверяем не дублируется ли педагог, а то может и не стоит его брать в штат))


    def checkSubject(self, subject, fullname):
        '''
        метод проверки наличия педагога по рассматриваемому предмету
        '''
        if subject not in dictSubjects_Teacher:
            dictSubjects_Teacher[subject] = fullname # дополняем словарь если такого предмета ещё в списке нет
        else:
            # оповещаем, что преподаватель не принят на работу
            print('Преподавателя {} на работу НЕ ПРИНЯЛИ! Так как основной педагог по предмету {} у нас уже есть.' .format(fullname, subject))

def viewSubject_Teacher(param):
    '''
    Функция вывода на экран информации по имеющимся предметам и закрепленными за ними преподавателями
    В качестве параметра вы можете использовать:
    all - показать всех имеющихся преподавателей и их предметы
    <'указать предмет'> - показать преподавателя по указанному предмету
    '''

    if param == 'all':
        for key, value in dictSubjects_Teacher.items():
            print(key, '-', value)
    elif param in dictSubjects_Teacher:
        print(param, '-', dictSubjects_Teacher[param])
    else:
        print(param, '- учитель отсутствует')


def viewStudensInClass():
    '''
    функция вывода всех учащихся в классе class_r
    '''
    choiceClass = input('\nДля того чтобы узнать учащихся, введите интересующий вас класс:\n')
    number = 0
    print('В классе %s учится:' %choiceClass)
    for el in listStudents:
        if el[3] == choiceClass:
            number += 1
            print('{}. {} {}.{}.' .format(number, el[2], el[0][:1], el[1][:1]))
    if number == 0: print('учащиеся отсутствуют')

def viewAndChoiceInAllSudents():
    '''
    Просмотр всех учащихся и возврат индекса в списке учащегося, которого выберет пользователь
    '''
    for student in listStudents:
        print('{}. {} {} {}' .format(listStudents.index(student) + 1, student[2], student[0], student[1]))
    while True:
        try:
            choice = int(input('Введите порядковый номер учащегося для выбора и нажмите Enter\n'))
            try:
                print('Выбран {} {} {}' .format(listStudents[choice - 1][2], listStudents[choice - 1][0], listStudents[choice - 1][1]))
                return (choice - 1)
            except IndexError:
                print('Учащегося под таким порядковым номером не существует')
        except ValueError:
            print('В качестве порядкового номера вводится только цифра. Например: 1')

def getSubjectStudent():
    '''
    Функция отображает пользователю список всех предметов выбираемого учащегося
    (Ученик --> Класс --> Учителя --> Предметы)
    '''
    # выбираем учащегося
    indexStudent = viewAndChoiceInAllSudents()
    print(indexStudent)
    print('{2} {0} {1} обучается в классе {3} и проходит следующие предметы:' .format(listStudents[indexStudent][0],
                                                                                  listStudents[indexStudent][1],
                                                                                  listStudents[indexStudent][2],
                                                                                  listStudents[indexStudent][3]))
    for subject in lst_subject(listStudents[indexStudent][3]):
        viewSubject_Teacher(subject)

def lst_subject(class_R):
    '''
    Функция возвращает список предметов для указанного класса
    '''
    key = str(int(class_R.split()[0])) # извлекаем цифру класса из принимаемого значения
    return dictSubjectsClasses[key] # из справочника вытаскиваем список предметов, соответствующий цифре класса

def getParentsStudent():
    '''
    функция получения ФИО родителей студента
    '''
    indexStudent = viewAndChoiceInAllSudents()
    print('ФИО родителей учащегося {0}:\nОтец: {2}\nМать: {1}' .format(listStudents[indexStudent][2] + ' '
                + listStudents[indexStudent][0] + ' ' + listStudents[indexStudent][1], listStudents[indexStudent][4],
                                                                       listStudents[indexStudent][5]))

def getTeachersInClass():
    '''
    Функция отображает список предметов и учителей по классу, указанному пользователем
    '''
    choiceClass = input('\nДля того чтобы узнать предметы и учителей, введите интересующий вас класс:\n')
    try:
        for subject in lst_subject(choiceClass):
            viewSubject_Teacher(subject)
    except KeyError:
        print('Такого класса у нас нет )')

student1 = Student('Анатолий', 'Васильевич', 'Шишкин', '1 Б', 'Шишкина Марина Юрьевна', 'Шишкин Василий Михайлович')
student2 = Student('Николай', 'Витальевич', 'Токарев', '1 Б', 'Токарева Елизавета Андреевна', 'Токарев Игорь Семенович')
student3 = Student('Маргарита', 'Ивановна', 'Глухарь', '2 А', 'Глухарь Светлана Николаевна', 'Глухарь Иван Сергеевич')
prepod1 = Teacher('Екатерина', 'Викторовна', 'Хавронина', 'Немецкий язык')
prepod2 = Teacher('Мария', 'Ивановна', 'Звездочкина', 'Окружающий мир')
prepod3 = Teacher('Ольга', 'Юрьевна', 'Козлова', 'Математика')

print('\nСписок учащихся:')
getSubjectStudent() # узнаем предметы конкретного учащегося
viewStudensInClass() # узнаем кто учится в интересующем классе
print('\nУзнать ФИО родителей учащегося:')
getParentsStudent() # узнаём родителей конкретного учащегося
getTeachersInClass() # узнаём учителей в интересующем классе


# Выводим на печать весь список классов школы
print('\nВообще в школе существуют классы:')
for el in listClass_rooms:
    print(el)