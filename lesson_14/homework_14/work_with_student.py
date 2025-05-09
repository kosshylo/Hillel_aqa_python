from lesson_14.homework_14.student import Student

kostia: Student = Student(name='Kostia', surname='Shylo', age=35)
print(f'\nAfter changed avarage mark:')
kostia.show_info()

kostia.edit_average_mark(97)
print(f'\nAfter changed avarage mark:')
kostia.show_info()