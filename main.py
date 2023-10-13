class Percon:
    __surname = 'No Family'
    __name = 'No Name'
    __age = 0

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age =age

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        if 2 < len(surname) < 20:
            self.__surname = surname
        else:
            print('Error surname')
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if 2 < len(name) < 20:
            self.__name = name
        else:
            print('Error name')
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age in range(2, 100):
            self.__age = age
        else:
            print('Error age')

    def show_info(self):
        print(f'Surname:{self.__surname} \nName: {self.__name} \nAge: {self.__age}')