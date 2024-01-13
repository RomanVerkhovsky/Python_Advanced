def buble_sort(array, service_func, sign) -> list:
    param = {'>': lambda prev_nmb, next_nmb: prev_nmb > next_nmb,
             '<': lambda prev_nmb, next_nmb: prev_nmb < next_nmb}

    if service_func(array, sign) is True:
        return array

    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if param[sign]((array[i], array[i+1])):
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


def check_attribute(array, attribute):
    param = {'>': lambda prev_nmb, next_nmb: True if prev_nmb > next_nmb else False,
             '<': lambda prev_nmb, next_nmb: True if prev_nmb < next_nmb else False}

    for i in range(len(array) - 1):
        if param[attribute](array[i], array[i+1]) is False:
            return False
    return True


array = [3, 2, 1]
print(check_attribute(array, '>'))


slovar = {'hedgehog': 'roman, lidia',
          'human': 'jora, asad',
          }

print(slovar['hedgehog'])

