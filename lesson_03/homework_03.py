alice_in_wonderland: str = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
print(f'\n task 01:\n{alice_in_wonderland}')
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
selected: list  = []
for  apostrophe in alice_in_wonderland:
    if apostrophe == "'":
        print(apostrophe)
#     if apostrophe == "'":
#         selected += apostrophe
# #        selected.append(apostrophe)
# print(selected)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(f'\n task 03:\n{alice_in_wonderland}')

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_black_sea: int = 436402
square_azov_sea: int = 37800
total_square_both_seas: int = square_black_sea + square_azov_sea
total_square_both_seas: str = str(total_square_both_seas)
print(f'\n task 04:\ntotal_square_both_seas: {total_square_both_seas[:3]} {total_square_both_seas[3:]} km2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# Загальна кількість товарів на трьох складах
total_items: int = 375291
# Кількість товарів на першому та другому складах
first_second: int = 250449
# Кількість товарів на другому та третьому складах
second_third: int = 222950

# Знайдемо кількість товарів на другому складі
second = first_second + second_third - total_items

# Знайдемо кількість товарів на першому складі
first = first_second - second

# Знайдемо кількість товарів на третьому складі
third = second_third - second

# Виведемо результати
print(f"\n task 05:\nНа першому складі: {str(first)[:3]} {str(first)[3:]} товарів")
print(f"На другому складі: {str(second)[:2]} {str(second)[2:]} товарів")
print(f"На третьому складі: {str(third)[:3]} {str(third)[3:]} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthes: int = int(1.5*12)
PC_cost: int = 1179*monthes
print(f'\n task 06:\nВартість комп’ютера: {str(PC_cost)[:2]} {str(PC_cost)[2:]} грн')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f'\n task 07:\nзалишок від ділення {8019%8}')
print(f'залишок від ділення {9907%9}')
print(f'залишок від ділення {2789%5}')
print(f'залишок від ділення {7248%6}')
print(f'залишок від ділення {7128%5}')
print(f'залишок від ділення {19224%9}')


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

list_amount: tuple = 4, 2, 4, 1, 3
list_price: tuple = 274, 218, 35, 350, 21
i = 0
total = 0
while i <= 4: # <len(list_amount)
    total += list_amount[i] * list_price[i]
    i += 1
print(f'\n task 08:\nВсього {total} грн знадобиться для даного замовлення ')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
one_page = 8

if all_photos%one_page==0:
    total_pages_needed = all_photos//one_page
else:    total_pages_needed = all_photos//one_page +1
print(f'\n task 09:\ntotal_pages_needed {total_pages_needed}')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance: int = 1600
count_distance: int = 100
litrs_per_100km: int = 9
tank: int = 48
total_litrs_needed = distance/100*litrs_per_100km
print(f'\n task 10:\n1) {total_litrs_needed} літрів бензину знадобиться для такої подорожі')

#the min will be, if they had full tank before start travel:
if total_litrs_needed%tank==0:
    min_tanks_needed = total_litrs_needed//tank -1 # -1 , as the min will be, if they had full tank before start travel
else:    min_tanks_needed = total_litrs_needed//tank # look comment above
print(f'2) min_tanks_needed {min_tanks_needed}')