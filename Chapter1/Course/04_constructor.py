class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("La class Student crée un objet.")

"""
student1 = Student()
student1.name = "Alex"
student1.age = 13
student1.tel = "110"
"""

# La méthode __init__ est automatiquement exécutée lors de la construction de la classe
student2 = Student("Michael", 15, "120")
print(student2.name)

