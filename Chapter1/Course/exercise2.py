class Student:
    name = None
    age = None
    address = None


    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

for number in range(1, 6):
    print(f"Actuellement en train de saisir le {number}ème, 5 élèves au total doivent être saisis.")
    name = input("Veuillez saisir le nom de l'élève: ")
    age = int(input("Veuillez saisir l'âge de l'élève: "))
    address = input("Veuillez saisir l'adresse de l'élève: ")
    stu = Student(name, age, address)
    print(f"La saisie des informations sur l'étudiant {number} est complète avec les informations suivantes: [Nom : {stu.name}, Age: {stu.age}, Address: {stu.address}]")
