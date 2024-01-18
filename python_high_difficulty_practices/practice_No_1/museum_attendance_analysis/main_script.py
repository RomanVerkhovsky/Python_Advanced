from service_script import *


def total_visitors(array: list) -> int:
    sum_visitor = 0
    for i in range(len(array)):
        sum_visitor += int(array[i][1])

    return sum_visitor


def average_months(array: list) -> int:
    ave_months = total_visitors(array) // 12
    return ave_months


def average_day(array: list) -> int:
    ave_day = total_visitors(array) // 365
    return ave_day


def ordinary_days(array) -> list:
    ord_days = []
    for i in range(len(array)):
        if array[i][2] == 0:
            ord_days += array[i][2]

    return ord_days


def holiday_days(array: list) -> list:
    hol_days = []
    for i in range(len(array)):
        if array[i][2] == 1:
            hol_days += array[i][2]

    return hol_days


def peek_days(array: list) -> list:
    peek_d = []
    peek_origin = average_day(array)
    for i in range(len(array)):
        if int(array[i][1]) > peek_origin:
            peek_d.append(array[i][0])

    return peek_d


def low_days(array: list) -> list:
    low_d = []
    peek_origin = average_day(array)
    for i in range(len(array)):
        if int(array[i][1]) < peek_origin:
            low_d.append(array[i][0])

    return low_d


def data_report(total, ave_months, peek, low):
    rep = {'Общее количество посетителей:': total,
           'Среднее количество посетителей:': ave_months,
           'Пиковые дни:': peek,
           'Непиковые дни:': low}
    return rep


def report(array: list) -> str:
    rep = data_report(total_visitors(array), ave_months=average_months(array), peek=', '.join(peek_days(array)),
                      low=', '.join(low_days(array)))
    text_report = 'Детальный отчет о посещаемости музея за год\n'

    # for key in rep:
    #     print(key, rep[key])

    for key in rep:
        text_report += f'{key} {rep[key]}\n'

    return text_report


def program():
    data = data_for_analysis('museum_attendance_extended.csv')
    rep = report(data)
    write_file(rep)


if __name__ == '__main__':
    program()
