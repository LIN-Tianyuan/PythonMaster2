class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

student_list = []
for number in range(1, 3):
    print(f"Actuellement en train de saisir le {number}ème, 2 élèves au total doivent être saisis.")
    name = input("Veuillez saisir le nom de l'élève: ")
    age = int(input("Veuillez saisir l'âge de l'élève: "))
    address = input("Veuillez saisir l'adresse de l'élève: ")
    stu = Student(name, age, address)
    student_list.append(stu)
    print(f"La saisie des informations sur l'étudiant {number} est complète avec les informations suivantes: [Nom : {stu.name}, Age: {stu.age}, Address: {stu.address}]")

for student in student_list:
    print(f"Student: name: {student.name}, age: {student.age}")
