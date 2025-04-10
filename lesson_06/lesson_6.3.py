'''Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
 Напишіть код, який свормує новий list (наприклад lst2),
 який містить лише змінні типу стрінг, які присутні в lst1.
 Данні в лісті можуть бути будь якими'''

lst1: list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# lst2: list[str] = []
# for element in lst1:
#     if type(element) == str:
#         lst2.append(element)
lst2 = [element for element in lst1 if isinstance(element, str)]
print(lst2)