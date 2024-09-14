import os
import datetime


def date_protocool(date_range: str):
    date_start, date_finish = date_range.split(' - ')[0], date_range.split(' - ')[1]
    check_list = []
    n = int(date_start.split('.')[0])
    while n <= int(date_finish.split('.')[0]):
        check_list.append(n)
        n += 1
    return check_list,int(date_start.split('.')[1]), int(date_start.split('.')[2])


def task_check(tasks: list, date_range: str):
    date_protocol, month, year = date_protocool(date_range)
    print(month, year)
    while True:
        try:
            add_tasks = str(input(f'Добавить все задачи ТОЛЬКО из диапазона {date_range}? (y/n): '))
            match add_tasks:
                case 'y':
                    raw_data = filereader('Выполненая работа.txt')
                    well_data = []
                    buffer = []
                    for string in raw_data:
                        buffer.append(string.split(' | '))
                    for unpuck_task in buffer:
                        if int(unpuck_task[1].split('.')[0]) in date_protocol and (int(unpuck_task[1].split('.')[1]) == month) and (int(unpuck_task[1].split('.')[2]) == year):
                            well_data.append(unpuck_task)
                    return well_data
                case 'n':
                    diap = str(input('Введите диапазон дат в формате "ДД.ММ.ГГГГ"'))
                case _:
                    ...
        except Exception as e:
            print(f'Что-то пошло не так, ошибка: {e}')


def filereader(path: str):
    while True:
        try:
            with open(path, 'r', encoding='utf8') as f:
                data = f.readlines()
            return data
        except Exception as e:
            print('Стандартный путь не найден (Выполненая работа.txt)')
            flag = True
            while flag:
                path = str(input('Введите название файла с треком задач(.txt добавляется ): ')) + '.txt'
                files = os.listdir()
                if path in files:
                    print('Файл найден!')
                    flag = False
                else:
                    print(f"Файл с именем '{path}' не найден")


def filewriter(path: str, data: list):
    with open(path, 'w', encoding='utf8') as f:
        ...


def check_year(year: int):
    try:
        if (year % 4 == 0) and (year % 100 != 0):
            return True
        elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
            return True
        else:
            return False
    except Exception as e:
        print(f'что-то пошло не так, ошибка: {e}')


def date_range():
    ves_year = {
        '1': 31, '2': 29, '3': 13, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31
    }
    unves_year = {
        '1': 31, '2': 28, '3': 13, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31
    }
    flag_1 = True
    while flag_1:
        while True:
            try:
                year = int(input('Год отчета: '))
                month = int(input('Месяц отчета: '))
                half = int(input('1 или 2 половина месяца: '))
                if (year >= 2024) and (12 >= month > 0) and (half == 1 or 2):
                    if month < 10:
                        month = '0' + str(month)
                    break
                else:
                    print('Неправильне днные!')
            except Exception as e:
                print(f'что-то пошло не так - {e}')
        flag_2 = True
        match half:
            case 1:
                date = str('01.') + str(month) + '.' + str(year) + ' - ' + str('15.') + str(month) + '.' + str(year)
                while flag_2:
                    match str(input(f'Это верная дата: {date},  (y/n)?')):
                        case 'y':
                            return date
                        case 'n':
                            print('Повторите ввод даты')
                            flag_2 = False
                        case _:
                            print('Попробуй еще раз (y/n)')
            case 2:
                if check_year(year):
                    date = str('16.') + str(month) + '.' + str(year) + ' - ' + str(ves_year[str(int(month))]) + '.' + str(month) + '.' + str(year)
                    while flag_2:
                        match str(input(f'Это верная дата: {date},  (y/n)?')):
                            case 'y':
                                return date
                            case 'n':
                                print('Повторите ввод даты')
                                flag_2 = False
                            case _:
                                print('Попробуй еще раз (y/n)')
                else:
                    date = str('16.') + str(month) + '.' + str(year) + ' - ' + str(unves_year[str(int(month))]) + '.' + str(month) + '.' + str(year)
                    while flag_2:
                        match str(input(f'Это верная дата: {date},  (y/n)?')):
                            case 'y':
                                return date
                            case 'n':
                                print('Повторите ввод даты')
                                flag_2 = False
                            case _:
                                print('Попробуй еще раз (y/n)')


'''print(date_range())'''
print(task_check(filereader('Выполненая работа.txt'), date_range()))
