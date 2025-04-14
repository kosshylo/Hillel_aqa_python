print("_" * 100)
print("\n task_7.1:")
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    '''
    returning multiplication table while product >= 25
    multiplication_table >= 25
    :param number: input value
    :return: multiplication table while product >= 25
    '''
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
    # Complete the while loop condition.

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print("_" * 100)
print("\n task_7.2:")
# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_func(a: int | float, b: int | float) -> int | float:
    '''
    returning sum of two numbers rounded to 2 decimal places
    :param a: fisrt number
    :param b: second number 
    :return: sum of two numbers
    '''
    return round(a + b, 2)

print( sum_func(3.33,4.44))

print("_" * 100)
print("\n task_7.3:")
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean_func(args: list[int | float]) -> int | float:
    '''
    arithmetic mean function
    :param args: list of int|float numbers
    :return: arithmetic mean
    '''
    result: float = 0
    for element in args:
        result += element
    length: int = len(args)
    return round(result / length, 2)

#test
input_list: list = [1,7,9,3,33]
print(arithmetic_mean_func(input_list))

print("_" * 100)
print("\n task_7.4:")
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_order_func(args: str) -> str:
    '''
    revers order function
    :param args: input string
    :return: input string in reversed order
    '''
    return args[::-1]

print(revers_order_func("Hello World!"))

print("_" * 100)
print("\n task_7.5:")
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
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

input_list: list[str] = ["World", "Hello", "Automation"]
print(longest_word(["World", "Hello", "Automation"]))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""