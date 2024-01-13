def read_file(path: str) -> str:
    """
    Reading csv file
    :param path: path to text file (example: path.csv)
    :return: text(str)
    """
    file = open(path, 'r', encoding='utf8')
    text = file.read()
    file.close()
    return text


def write_file(text: str, path: str = 'museum_attendance_extended_report.txt'):
    """
    Writing a report to txt file
    :param path: str (example: path.txt)
    :param text: text (str)
    """
    file = open(path, 'w', encoding='utf8')
    file.write(text)
    file.close()


def calculate_ave(sum: float, nmb_elem: int) -> float:
    """
    Function of calculating average values
    :param sum: sum of all numbers
    :param nmb_elem: numbers of elements
    :return: average values
    """
    average = round(sum / nmb_elem, 2)
    return average


def text_in_array(text: str) -> list:
    """
    Converted str in list
    :param text: str
    :return: list
    """

    array = text.split('\n')

    if len(array[-1]) == 0:
        array = array[:-1:]

    for i in range(len(array)):
        array[i] = array[i].split(',')

    return array


def data_for_analysis(path: str) -> list:
    """
    Preparing a file for analysis
    :param path: path to text file (example: path.csv)
    :return: list (example: [[1, 2, 3], ['f', 3, 3]])
    """
    array = text_in_array(text=read_file(path=path))
    return array

def average_months(array: list):
    pass