from faker import Faker
fake = Faker()


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

#test
input_list: list = [1,7,9,3,33]
print(arithmetic_mean(input_list))

print("_" * 100)
print("\n task_7.4:")
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_order_func(input_str: str) -> str:
    '''
    revers order function
    :param input_str: input string
    :return: input string in reversed order
    '''
    return input_str[::-1]

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

input_list: list[str] = fake.words(nb=5)
# input_list: list[str] = ["World", "Hello", "Automation"]
print(f'ínput list of words: {input_list}')
print(f'the longest word from input list: {longest_word(input_list)}')

print("_" * 100)
print("\n task_7.6:")
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1: str, str2: str) -> int:
    '''
    returning index where substring is found,
    :param str1: selected/main string
    :param str2: searched substring
    :return: index where substring is found,
             or Return -1 on failure.
    '''
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(f"{str1 = }")
print(f"{str2 = }")
print(f'index: {find_substring(str1, str2)}\n') # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(f"{str1 = }")
print(f"{str2 = }")
print(f'index: {find_substring(str1, str2)}') # поверне -1

# task 7
'''Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
інакше - False. Строку отримати за допомогою функції input().'''
from pickle import FALSE

print("_" * 100)
print("\n task_7.7: Порахувати кількість унікальних символів в строці")

def unic_symbols_func(input_str: str) -> bool:
    '''
    Returning is unic symbols > 10
    :param input_str: input string
    :return: True or False of unic symbols > 10
    '''
    str_to_set = set(input_str)
    unic_elements = len(str_to_set)
    return unic_elements > 10

input_str: str = input("Please print your string: ")
print(f'"{unic_symbols_func(input_str)}": Унікальних символів > 10')

# task 8
'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті.'''
print("_" * 100)
print("\n task_7.8:")

def sum_even(numbers_list: list[int]) -> int:
    '''
    Returning sum of all EVEN numbers in list
    :param numbers_list: input numbers list
    :return: sum of all EVEN numbers in list
    '''

    result = 0
    for number in numbers_list:
        if number % 2 == 0:
            result += number
    return result

input_list: list = [1, 4, 7, 9, 2, 12, 11]
print(f'Сума усіх ПАРНИХ чисел в цьому лісті: {sum_even(input_list)}')

# task 9
'''Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
 Напишіть код, який свормує новий list (наприклад lst2),
 який містить лише змінні типу стрінг, які присутні в lst1.
 Данні в лісті можуть бути будь якими'''

print("_" * 100)
print("\n task_7.9:")
def select_str_items(data_list: list)->list[str]:
    '''
    Choose only str type of data
    :param array_data: input data
    :return: list of string data
    '''
    lst2 = [element for element in data_list if isinstance(element, str)]
    return lst2


lst1: list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(select_str_items(lst1))

# task 10
'''ДЗ 6.2. Цикл “Дочекайся літери”
Напишіть цикл, який буде вимагати від користувача ввести слово,
 в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''


print("_" * 100)
print("\n task_7.10:")


def wait_letter(letter: str) -> None:
    '''
    Function stops if found the letter
    :param letter: searched element
    :return: nothing
    '''
    while True:
        entered_str: str = input(
            "Please enter your sentence. "
            "A mandatory condition for accepting your sentence is the presence of a word with the letter "
            f"{letter}, regardless of case: "
        )
        if letter.lower() in entered_str.lower():
            print(f'Thank you! You entered a word with the letter "{letter}".')
            break
        else:
            print(f'Error: Your sentence must include the letter "{letter}". Please try again.')

letter1: str = "l"
wait_letter(letter1)




"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""