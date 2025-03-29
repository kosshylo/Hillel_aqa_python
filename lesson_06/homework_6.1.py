'''Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
інакше - False. Строку отримати за допомогою функції input().'''
print("_" * 100)
print("\n task_6.1:")

entred_str: str = input("Please print your string: ")
str_to_set = set(entred_str)
unic_elements = len(str_to_set)

print(f'Кількість унікальних символів у введеному рядку: "{unic_elements}"' )