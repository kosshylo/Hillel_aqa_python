'''Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
інакше - False. Строку отримати за допомогою функції input().'''
from pickle import FALSE

print("_" * 100)
print("\n task_6.1:")

entred_str: str = input("Please print your string: ")
str_to_set = set(entred_str)
unic_elements = len(str_to_set)
answer: bool = unic_elements >10

print(f'"{answer}": Унікальних символів > 10')
