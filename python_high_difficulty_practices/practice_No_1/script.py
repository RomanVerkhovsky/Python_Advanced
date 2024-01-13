# No_1
def find_max_and_id(array: list) -> tuple:
    """
    Finding max number and index it in array
    :param array: list of numbers
    :return: tuple (max numbers, index max numbers)
    """
    if len(array) == 0:
        raise ValueError('Array is avoid!')

    for i in range(len(array)):
        if type(array[i]) is str:
            raise ValueError('Array contain text!')

    id_max = 0
    for i in range(1, len(array)):
        if array[i] > array[id_max]:
            id_max = i

    return array[id_max], id_max


# No_2
def get_inverting(array: list, left_border: int = 0, right_border: int = -1) -> list:
    """
    Inverting an array in specified boundaries
    :param array: list of integer numbers
    :param left_border: integer number
    :param right_border: integer number
    :return: list of numbers
    """
    if len(array) == 0:
        raise ValueError('Array is avoid!')

    for i in range(len(array)):
        if type(array[i]) is str:
            raise ValueError('Array contain text!')

    if right_border == -1:
        right_border = len(array) - 1

    invert_array = []

    for i in range(0, left_border):
        invert_array.append(array[i])

    count_invert_elem = (right_border - left_border) + 1
    for i in range(count_invert_elem):
        invert_array.append(array[right_border - i])

    for i in range(right_border + 1, len(array)):
        invert_array.append(array[i])

    return invert_array


# No_3
def sum_numbers_of_array(array: list, service_func, sign, basic_nmb: float) -> float:
    """
    Calculating the sum of the array numbers corresponding to the condition
    :param array: list of number
    :param service_func: checking a number to match a condition
    :param sign: <, >, <=, >=, ==, !=
    :param basic_nmb: number from a condition
    :return: number
    """
    if len(array) == 0:
        raise ValueError('Array is avoid!')

    for i in range(len(array)):
        if type(array[i]) is str:
            raise ValueError('Array contain text!')

    sum_nmb = 0
    for i in range(len(array)):
        if service_func(array[i], basic_nmb, sign):
            sum_nmb += array[i]

    return sum_nmb


def comparison_nmb(check_nmb: float, basic_nmb: float, sign) -> bool:
    """
    Checking a number to match another number
    :param check_nmb: first number for maching
    :param basic_nmb: second number for comparison
    :return: bool
    """
    param = {'>': lambda check_nmb, basic_nmb: check_nmb > basic_nmb,
          '<': lambda check_nmb, basic_nmb: check_nmb < basic_nmb,
          '>=': lambda check_nmb, basic_nmb: check_nmb >= basic_nmb,
          '<=': lambda check_nmb, basic_nmb: check_nmb <= basic_nmb,
          '==': lambda check_nmb, basic_nmb: check_nmb == basic_nmb,
          '!=': lambda check_nmb, basic_nmb: check_nmb != basic_nmb}

    if param[sign](check_nmb, basic_nmb):
        return True
    else:
        return False
