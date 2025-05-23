# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# solution kosshylo:
#______________________________________________________________________________________
# 1-st part
# 1 - Add your new record o the beginning of the given list
your_data_list = []

# name: str = input("Your Name: ")
# surname: str = input("Your Surname: ")
# age: int = input("Your Age: ")
# profession: str = input("Your profession: ")
# city_location: str = input("City of your location: ")
#
# your_data_list.append((name, surname, age, profession, city_location))
# print(f'Your (name, surname, age, profession, City location): {your_data_list}')

your_data_list.append(('Kostia', 'Shylo', '35', 'QA Engineer', 'Cambridge'))
your_people_records = your_data_list + people_records
print("_" * 100)
print("\n task1:")
print(f'Your own list people records list : {your_people_records}')

# 2-nd part
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
print("_" * 100)
print("\n task2:")
# before:
# print("Before:")
# i = 0
# for people in your_people_records:
#     print(f' {i}: {people}')
#     i += 1

your_people_records[1] , your_people_records[5] = your_people_records[5], your_people_records[1]
print("\n After Swap(1<->5):")
i = 0
for people in your_people_records:
    print(f' {i}: {people}')
    i += 1

# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
print("_" * 100)
print("\n task3:")

# index = [6, 10, 13]
#
# result: bool = True
# for i in index:
#     result = result and (your_people_records[i][2] >= 30)
#
# if result == True:
#     print ("All people in modified list are older than 30")
# else:
#     print("Some people is younger than 30")

index = [6, 10, 13]
records_over_30: list[bool] = []

for i in index:
    records_over_30.append(your_people_records[i][2] >= 30)

if len(records_over_30) == len(index):
    print(f'{True}: All people in the modified list are older than 30')
else:
    print(f'{False}: Some people are younger than 30')

print("_" * 100)