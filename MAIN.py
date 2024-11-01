import os
import datetime


def date_protocool(dp_date_range: str):
    date_start, date_finish = dp_date_range.split(' - ')[0], dp_date_range.split(' - ')[1]
    check_list = []
    n = int(date_start.split('.')[0])
    while n <= int(date_finish.split('.')[0]):
        check_list.append(n)
        n += 1
    return check_list, int(date_start.split('.')[1]), int(date_start.split('.')[2])


def task_check(tc_tasks: list, tc_date_range: str):
    date_protocol, month, year = date_protocool(tc_date_range)
    while True:
        try:
            raw_data = tc_tasks
            well_data = []
            buffer = []
            for string in raw_data:
                buffer.append(string.split(' | '))
            for unpack_task in buffer:
                if (int(unpack_task[1].split('.')[0]) in date_protocol
                        and (int(unpack_task[1].split('.')[1]) == month)
                        and (int(unpack_task[1].split('.')[2]) == year)):
                    well_data.append(unpack_task)
            return well_data
        except Exception as e:
            print(f'Что-то пошло не так, ошибка: {e}')


def filereader(path: str):
    while True:
        try:
            with open(path, 'r', encoding='utf8') as f:
                data = f.readlines()
            return data
        except Exception as e:
            print(e)
            print('Стандартный путь не найден (Выполненая работа.txt)')
            flag = True
            while flag:
                path = str(input('Введите название файла с треком задач(.txt добавляется автоматически): ')) + '.txt'
                files = os.listdir()
                if path in files:
                    print('Файл найден!')
                    flag = False
                else:
                    print(f"Файл с именем '{path}' не найден")


def filewriter(path: str, data: list, fw_date_range: str, fw_summary: str):
    if "EMAIL" not in os.listdir():
        os.makedirs('EMAIL')
    hello_part = (f'Привет! Вот работа выполненная в период {fw_date_range}\n'
                  f'Работа выполненная в период {fw_date_range}:\n'
                  f'\n'
                  f'\n'
                  f'{60 * "-"}\n')
    goodbye_part = (f'\n{60 * "-"}'
                    f'\n{fw_summary}'
                    f'\n'
                    f'\n'
                    f'\n'
                    f'С уважением\n'
                    f'Теребов Максим')
    outdata = [hello_part]
    for task in data:
        outdata.append(str(task[0]) + (' ' * (120 - len(str(task[0])))) + ' | ' + str(task[1]) + ' | ' + str(task[2]))
    if outdata[-1][-1] == "\n":
        outdata[-1] = str(outdata[-1])[:-2]
    outdata.append(goodbye_part)
    with open("EMAIL/" + path, 'w', encoding='utf8') as f:
        for task in outdata:
            f.write(task)


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
                half = int(input('1 или 2 половина месяца (для выбора всего месяца введите "12"): '))
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
                    match str(input(f'Это верная дата: {date}?  (y/n): ')):
                        case 'y':
                            return date
                        case 'n':
                            print('Повторите ввод даты')
                            flag_2 = False
                        case _:
                            print('Попробуй еще раз (y/n)')
            case 2:
                if check_year(year):
                    date = (str('16.') + str(month) + '.' + str(year) + ' - ' + str(ves_year[str(int(month))]) + '.' +
                            str(month) + '.' + str(year))
                    while flag_2:
                        match str(input(f'Это верная дата: {date}?  (y/n): ')):
                            case 'y':
                                return date
                            case 'n':
                                print('Повторите ввод даты')
                                flag_2 = False
                            case _:
                                print('Попробуй еще раз (y/n)')
                else:
                    date = (str('16.') + str(month) + '.' + str(year) + ' - ' + str(unves_year[str(int(month))]) + '.' +
                            str(month) + '.' + str(year))
                    while flag_2:
                        match str(input(f'Это верная дата: {date}?  (y/n): ')):
                            case 'y':
                                return date
                            case 'n':
                                print('Повторите ввод даты')
                                flag_2 = False
                            case _:
                                print('Попробуй еще раз (y/n)')
            case 12:
                if check_year(year):
                    date = (str('01.') + str(month) + '.' + str(year) + ' - ' + str(ves_year[str(int(month))]) + '.' +
                            str(month) + '.' + str(year))
                    while flag_2:
                        match str(input(f'Это верная дата: {date}?  (y/n): ')):
                            case 'y':
                                return date
                            case 'n':
                                print('Повторите ввод даты')
                                flag_2 = False
                            case _:
                                print('Попробуй еще раз (y/n)')
                else:
                    date = (str('01.') + str(month) + '.' + str(year) + ' - ' + str(unves_year[str(int(month))]) + '.' +
                            str(month) + '.' + str(year))
                    while flag_2:
                        match str(input(f'Это верная дата: {date}?  (y/n): ')):
                            case 'y':
                                return date
                            case 'n':
                                print('Повторите ввод даты')
                                flag_2 = False
                            case _:
                                print('Попробуй еще раз (y/n)')


def summary(data: list):
    orig_summary = 0
    for task in data:
        if task[2][-3:] == 'час':
            orig_summary += float(task[2][:-4])
        else:
            orig_summary += float(task[2][:-5])
    return f'Итого: {orig_summary} ({orig_summary * 800})'


'''date_range = date_range()
tasks = task_check(filereader('Выполненая работа.txt'), date_range)
filewriter(f'email {str(datetime.date.today())}.txt', tasks, date_range, summary(tasks))
print(tasks)'''
print(date_protocool("01.09.2024 - 30.09.2024"))
