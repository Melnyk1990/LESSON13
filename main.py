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

##################################################################################################################
class Teacher(Percon):
    __work_experience =0
    def __init__(self, surname, name, age, job_title=None, work_experience=None, direction=None):
        super().__init__(surname, name, age)
        self.job_title = job_title              #должность
        self.work_experience = work_experience  #СТАЖ работы
        self.direction = direction              #направление
    @property
    def work_experience(self):
        return self.__work_experience
    @work_experience.setter
    def work_experience(self, work_experience):
        if work_experience in range(56):
            self.__work_experience = work_experience
        else:
            print('Error Work Experience')

    def show_info(self):
        super().show_info()
        print(f'Job title: {self.job_title} \nWork experience: {self.work_experience} years\nDirection: {self.direction}')
        print()

##############################################################################################################
class TechnicalStaff(Percon):
    def __init__(self, surname, name, age, job_title, work_experience, direction):
        super().__init__(surname, name, age)
        self.job_title =job_title               #должность
        self.work_experience = work_experience  #СТАЖ работы
        self.direction = direction              #направление


    def show_info(self):
        super().show_info()
        print(f'Job title: {self.job_title} \nWork experience: {self.work_experience} years\nDirection: {self.direction}')
        print()


###############################################################################################################
class Student(Percon):
    def __init__(self, surname, name, age, speciality=None, course=None, group=None):
        super().__init__(surname, name, age)
        self.speciality = speciality   #специальность
        self.course = course           #курс
        self.group = group             #Группа
    def show_info(self):
        super().show_info()
        print(f'Speciality: {self.speciality} \nСourse: {self.course}\nGroup: {self.group}')
        print()

class Faculty(Teacher, Student):
    def __init__(self, surname, name, age, job_title, work_experience, direction, speciality, course, group ):
        Teacher.__init__(self, surname, name, age , job_title, work_experience, direction)
        Student.__init__(self, surname, name, age,speciality, course, group)
test = Faculty('Vasiliev', 'Edward', 26, 'Teacher', 40, 'Mathematics', 'Mechanical engineering', 4, 'OOP-23',)
test.show_info()
print(Faculty.mro())

###################################################################################################
class Academy:
    def __init__(self, teachet: list = None, student: list =None, technicalstaf: list = None):
        self.teacher: list[Teacher] = teachet
        self.student: list[Student] = student
        self.techical: list[TechnicalStaff] = technicalstaf

    def show_teacher(self):
        print(f'\t\t\tQuantity {len(self.teacher)} ***** Teacher *****')
        for teacher in self.teacher:
            teacher.show_info()


    def show_student(self):
        print(f'\t\t\tQuantity {len(self.student)} ***** Student *****')
        for student in self.student:
            student.show_info()

    def show_technicalstaf(self):
        print(f'\t\t\tQuantity {len(self.techical)} ***** Technical staf *****')
        for techical in self.techical:
            techical.show_info()



teachet = [Teacher('Voloshin', 'Kolya', 55, 'Teacher', 40, 'Mathematics'),
           Teacher('Ivanov', 'Stas', 40, 'Teacher', 32, 'Fizika'), Teacher('Stepanov', 'Evgen', 35, 'Teacher', 18, 'Chemistry')]

student = [Student('Zubko', 'Koly', 20, 'Programs', 1, 'PP-08'), Student('Nazarov', 'Alex', 25, 'Programs', 4, 'PP-04')]
technicalstaf = [TechnicalStaff('Polosa', 'Valentin', 55, 'electrician', 40, 'wiring')]

test = Academy(teachet, student, technicalstaf)

test.show_student()
test.show_teacher()
test.show_technicalstaf()
