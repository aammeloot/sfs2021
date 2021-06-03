
class Student(object):
    name = ""
    enrolment = ""
    age = 0

    def __init__(self, aName, aCourse, someAge):
        self.name = aName
        self.enrolment = aCourse
        self.age = someAge

    def describe(self):
        print("-----------------")
        print("Name: ", self.name)
        print("Enrolment: ", self.enrolment)
        print("Age: ", self.age)


s1 = Student("Frank", "Cybersecurity", 20)
s2 = Student("Debbie", "Software Engineering", 19)

s1.describe()
s2.describe()

