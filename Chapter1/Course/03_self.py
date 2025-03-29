class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

    def say_hi2(self, message):
        print(f"Bonjour à tous, {message}")

# Création d'un objet basé la classe Student
stu = Student()
stu.name = "Alex"
stu.age = 18
stu.say_hi()
stu.say_hi2("enchanté.")