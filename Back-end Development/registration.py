class Person:
    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName

    def sleep(self) -> str:
        return f'{self.first_name} {self.last_name} is now sleeping.'

class Administrator(Person):
    def __int__(self, fName, lName):
        self.Person = Person(fName,lName)

    def register(self, Student) -> str:
        if not Student.is_registered:
            Student.is_registered = True
            return f'Student {Student.student_number} is registered.'
        else:
            return f'Student {Student.student_number} is already registered.'

class Student(Person):
    def __init__(self, fName, lName, studentNum, isRegistered=False):
        self.Person = Person(fName,lName)
        self.student_number = studentNum
        self.is_registered = isRegistered

    def sleep(self) -> str:
        return f'Student {self.student_number} is now sleeping.'

if __name__=='__main__':
    student = Student("First Name", "Last Name", "1234567")
    admin = Administrator("UP", "CRS")
    print(student.sleep())
    print(admin.sleep())
    print(admin.register(student))
    print(admin.register(student))