def sum_func(a: int | float, b: int | float) -> int | float:
    '''
    returning sum of two numbers rounded to 2 decimal places
    :param a: fisrt number
    :param b: second number
    :return: sum of two numbers
    '''
    return round(a + b, 2)

#__________________________________________________________________________

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(numbers_list: list[int | float]) -> int | float:
    '''
    arithmetic mean function
    :param numbers_list: list of int|float numbers
    :return: arithmetic mean
    '''
    result: float = 0
    for element in numbers_list:
        result += element
    length: int = len(numbers_list)
    return round(result / length, 2)

#______________________________________________________________
def longest_word(args: list[str]) -> str:
    '''
    returning the longest word
    :param args: input list of words
    :return: the longest word
    '''

    result: list[str] = []
    for word in args:
        if len(result) < len(word):
            result=word
    return result
#___________________________________________________________
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

#_____________________________________________________

def unic_symbols_func(input_str: str) -> bool:
    '''
    Returning is unic symbols > 10
    :param input_str: input string
    :return: True or False of unic symbols > 10
    '''
    str_to_set = set(input_str)
    unic_elements = len(str_to_set)
    return unic_elements > 10

