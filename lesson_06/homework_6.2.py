'''ДЗ 6.2. Цикл “Дочекайся літери”
Напишіть цикл, який буде вимагати від користувача ввести слово,
 в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''


print("_" * 100)
print("\n task_6.2:")

while True:
    entred_str: str = input("Please enter your sentence."
    " A mandatory condition for accepting your sentence is presence word with the letter h,"
    " regardless of case.: ")
    if "h" in entred_str.lower():
        print("Thank you! You entered word with 'h'")
        break
    else:
        print("Error: Your sentence must includ letter 'h'. Please try again.")
