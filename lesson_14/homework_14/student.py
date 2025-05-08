class Student:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.__settings_average_mark_to_0()

    def return_average_mark(self):
        return self.__average_mark

    def __settings_average_mark_to_0(self):
        self.__average_mark = 0

    def edit_average_mark(self, new_average_mark: int):
        '''
        Change average_mark to new
        :param new_average_mark: new value
        :return: edited average mark
        '''
        self.__average_mark = new_average_mark

    def show_info(self):
        print(f' Name:\t             {self.name}')
        print(f' Surname:\t         {self.surname}')
        print(f' Age:\t             {self.age}')
        print(f' Average mark:\t     {self.__average_mark}')