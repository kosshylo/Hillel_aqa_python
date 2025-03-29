'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті.'''
print("_" * 100)
print("\n task_6.4:")


some_list: list = [1, 4, 7, 9, 2, 12, 11]
sum_even = 0
for number in some_list:
    if number % 2 == 0:
        sum_even += number

print(sum_even)