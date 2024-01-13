from service_script import *


def get_expenses(array: list) -> list:
    """
    Calculate the total amount of expenses and the average expense for each category;
    :param array: list
    :return: list
    """
    sum_expenses = 0
    for i in range(1, len(array)):
        for j in range(1, len(array[i])):
            sum_expenses += array[i][j]

    array_exp = [['Общие расходы', sum_expenses]]

    for i in range(1, len(array)):
        array_exp.append([])
        array_exp[i].append(array[i][0])
        sum_category = 0
        nmb_months = 0

        for j in range(1, len(array[i])):
            sum_category += array[i][j]
            nmb_months += 1

        average = calculate_ave(sum_category, nmb_months)
        array_exp[i].append(average)

    return array_exp


def get_trand(array: list) -> list:
    array = array[1::]
    array_trend = []

    for i in range(len(array)):
        sum_category = 0
        nmb_months = 0

        for j in range(1, len(array[i])):
            sum_category += array[i][j]
            nmb_months += 1

        average = calculate_ave(sum_category, nmb_months)
        trand = 'нестабильный'
        if average > array[i][11] and average > array[i][12]:
            trand = 'возрастание'
        elif average < array[i][11] and average < array[i][12]:
            trand = 'убывание'
        elif average == array[i][11] and average == array[i][12]:
            trand = 'стабильный'

        array_trend.append([array[i][0], trand])

    return array_trend


def get_predict(array: list) -> float:
    array = array[1::]
    sum_average = 0
    for i in range(len(array)):
        sum_category = 0
        nmb_months = 0

        for j in range(1, len(array[i])):
            sum_category += array[i][j]
            nmb_months += 1

        average = calculate_ave(sum_category, nmb_months)
        sum_average += average

    return round(sum_average, 2)


def report(array_expenses: list, array_trand: list, predict: float) -> str:
    text = (f'Углубленный отчет о расходах кафе за последние 12 месяцев\n'
            f'Общие расходы: {array_expenses[0][1]}\n')

    for i in array_expenses[1:]:
        text += f'Средние расходы по категории "{i[0]}": {i[1]} руб;\n'

    for i in array_trand:
        text += f'Тренд расходов - {i[1]}, по категории "{i[0]}";\n'

    text += f'Прогнозируемые расходы на следующий год: {predict} руб'

    return text


def program():
    data = data_for_analysis(path='cafe_expenses_extended.csv')
    rep = report(get_expenses(data), get_trand(data), get_predict(data))
    write_file(rep)


if __name__ == "__main__":
    program()




