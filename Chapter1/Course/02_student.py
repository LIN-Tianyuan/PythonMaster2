class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

stu_1 = Student()
stu_1.name = "Alex"
stu_1.age = 14
stu_1.say_hi()

stu_2 = Student()
stu_2.name = "Mika"
stu_2.age = 15
stu_2.say_hi()