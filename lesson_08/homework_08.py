input_list: list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def sum_numbers_from_string(arg: str) ->int:
    '''
    the functional return sum for each element of array numbers
    :param arg: str  -  input list
    :return: total: int - sum for each element
    '''

    try:
        numbers: list[str] = arg.split(',')
        total: int = sum(int(num) for num in numbers)
        return total
    except ValueError as e:
        return "Не можу це зробити!"

element: str = ''
for element in input_list:
    result = sum_numbers_from_string(element)
    print(result)