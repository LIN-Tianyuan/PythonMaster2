class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    # def __str__(self):
    #     return f"name = {self.name}, age = {self.age}, tel = {self.tel}"

    # less than
    def __lt__(self, other):
        return self.age < other.age

    # greater than
    def __gt__(self, other):
        return self.age > other.age

    # less equal than
    def __le__(self, other):
        return self.age <= other.age

    # greater equal than
    def __ge__(self, other):
        return self.age >= other.age

    # equal
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.tel == other.tel

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

stu1 = Student("Michael", 14, "110")
stu2 = Student("Lucas", 13, "120")
stu3 = Student("Alex", 13, "130")
stu4 = Student("Alex", 13, "130")
print(stu1 < stu2)
print(stu1 > stu2)
print(stu2 <= stu3)
print(stu2 >= stu3)
print('----------')
print(stu3 == stu4)
print(stu3)
print(stu4)
print('----------')
a = 1
b = 1
print(a == b)


