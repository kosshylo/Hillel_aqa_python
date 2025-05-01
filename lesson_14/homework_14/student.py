class Student:

    def __init__(self, name: str, surname: str, age: int, average_mark: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_mark = average_mark

    def edit_average_mark(self, new_average_mark: int):
        '''
        Change average_mark to new
        :param new_average_mark: new value
        :return: edited average mark
        '''
        self.average_mark = new_average_mark

    def show_info(self):
        print(f' Name:\t             {self.name}')
        print(f' Surname:\t         {self.surname}')
        print(f' Age:\t             {self.age}')
        print(f' Average mark:\t     {self.average_mark}')