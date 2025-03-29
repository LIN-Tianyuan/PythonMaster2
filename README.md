# Python Master

## Chapter 1 Programmation Orienté objet
### 1. Classes et objets
```python
# Concevoir la classe Student
class Student:
    name = None # Enregister le nom de l'élève

# Création d'objets basés sur des classes
stu_1 = Student()
stu_2 = Student()

# Affectation des propriétés de l'objet
stu_1.name = "Alex"
stu_2.name = "Mika"
print(stu_1.name)
print(stu_2.name)
```
### 2. Méthodes des membres
 - Définition et utlisation des classes
```python
# class est un mot-clé qui indique qu'une classe doit être définie
class Student:
    # Variables membres
    name = None
    age = None

    # Méthodes membres
    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

stu_1 = Student()
```
### 3. Self
 - Le mot-clé self, bien que figurant dans la liste des arguments, peut être ignoré lors du passage des paramètres.
 - Indique l'objet de la classe lui-même
 - Les variables membres de la classe ne peuvent être accédées par les méthodes membres que par l'intermédiaire de self.
```python
class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

    def say_hi2(self, message):
        print(f"Bonjour à tous, {message}")

# Création d'un objet basé sur la classe Student
stu = Student()
stu.name = "Alex"
stu.age = 18
stu.say_hi()
stu.say_hi2("enchanté.")
```

