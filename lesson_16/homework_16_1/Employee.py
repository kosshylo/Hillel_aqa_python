class Employee:
    def __init__(self, name, salary):
        self.name: str = name
        self.salary: int = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department: str = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language: str = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.__list_of_developers: list[Developer] = []
        self.__settings_team_size_to_0()

    def __settings_team_size_to_0(self) -> None:
        '''
        Inizialization setup team size to 0
        :return: None
        '''
        self.__team_size = 0

    def return_team_size(self) -> int:
        '''
        Returning amount of developers managed by TeamLead
        :return: amount of developers managed by TeamLead
        '''
        return self.__team_size

    def get_team_size(self):
        '''
        Returning updated amount of developers in team
        :return: updated amount of developers in team
        '''
        self.__team_size = len(self.__list_of_developers)


    def add_developer(self, developer: Developer) -> None:
        '''
        Add developer to team and update team size
        :param developer: Developer element
        :return: None
        '''
        self.__list_of_developers.append(developer)
        self.get_team_size()