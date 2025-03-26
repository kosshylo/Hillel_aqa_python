adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("-" * 100)
print(f'\n task1:\n{adwentures_of_tom_sawer}')
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print("-" * 100)
print(f'\n task2:\n{adwentures_of_tom_sawer}')
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print("-" * 100)
print(f'\n task3:\n{adwentures_of_tom_sawer}')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print("-" * 100)
print(f'\n task4:\nЛітера "h" зустрічається {count_h} разів у тексті.')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
i = 0
for word in adwentures_of_tom_sawer.split():
    if word.istitle():
        i += 1
print("-" * 100)
print(f'\n task5:\n"{i}" слів у тексті починається з Великої літери')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index + 1)

if second_index != -1:
    print("-" * 100)
    print(f'\n task7:\nСлово "Tom" вдруге зустрічається на позиції: {second_index}')
else:
    print("-" * 100)
    print('\n task6:\nСлово "Tom" зустрічається менше двох разів.')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
atsk7_adwentures_of_tom_sawer = adwentures_of_tom_sawer.split(".")
#adwentures_of_tom_sawer_sentences = None
print(f'\n task7:\n{atsk7_adwentures_of_tom_sawer}')
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
