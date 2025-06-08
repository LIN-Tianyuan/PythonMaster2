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
### 4. Class et object
 - Relation:
   - Les classes sont les "dessins de conception" du programme.
   - Les objets sont des entités concrètes produites sur la base des dessins.
 - Programmation orientée objet:
   - Concevoir des classes
   - Créer des objets basés sur ces classes
   - Utiliser pour effectuer des tâches spécifiques
### 5. Méthodes de construction
```python
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
```
 - La construction d'un objet de classe est exécutée automatiquement.
 - Le passage de l'objet de classe est transmis au constructeur, qui permet l'affectation de valeurs aux variables membres.
### 6. Méthodes magique
```bash
__init__
__str__
__lt__
__le__
__eq__
```
```python
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
```
### 7. Encapsulation
 - La description d'éléments du monde réel tels que les propriétés et les méthodes dans une classe est connue sous le nom d'encapsulation.
 - Certaines propriétés et certains comportements de choses réelles ne sont pas accessibles aux utilisateurs. La même exigence doit être respectée lors de la description des propriétés et des méthodes dans les classes, et les membres privés doivent être définis.
 - Les variables et les méthodes membres sont nommées avec __ au début.
 - Les objets de la classe ne peuvent pas accéder aux membres privés.
 - Les autre membres de la classe peuvent accéder aux membres privés.

### 8. Héritage

- L'héritage est une classe qui hérite des variables et des méthodes membres d'une autre classe.

```python
class Phone:
    serial_number = None
    producer = None

    def call_by_4g(self):
        print("4g call.")

class Phone2025(Phone):
    face_id = True

    def call_by_5g(self):
        print("5g call.")

phone = Phone2025()
phone.call_by_5g()
phone.call_by_4g()

phone1 = Phone()
phone1.call_by_4g()
```

- Héritage simple: une classe hérite d'une autre classe.
- Héritage multiple: une classe hérite de plusieurs classe, dans l'ordre de gauche à droites.
- Dans l'héritage multiple, si la classe père possède des méthodes ou des variables portant le même nom, le premier héritage a la priorité sur le second.
- pass est une déclaration de remplacement utilisée pour garantir l'intégrité d'une fonction(méthode) ou d'une définition de classe, ce qui signifie qu'elle n'a pas de contenu, qu'elle est vide ou qu'elle est en cours d'exécution.

### 9. Override

- Redéfinir une propriété ou une méthode membre d'une classe parente.
- Il suffit de réimplémenter la méthode ou la propriété membre du même nom dans la sous-classe.

```python
class Phone:
    serial_number = None
    producer = "HUAWEI"

    def call_by_5g(self):
        print("Father 5g calls.")

class MyPhone(Phone):
    producer = "Apple"

    def call_by_5g(self):
        # La première façon d'appeler un membre de la classe père
        print(f"La marque de la classe père est: {Phone.producer}")
        Phone.call_by_5g(self)

        # La deuxième façon d'appeler un membre de la classe père
        print(f"La marque de la classe père est: {super().producer}")
        super().call_by_5g()

my_phone = MyPhone()
my_phone.call_by_5g()
```

### 10. Annotation de type

- La spécification explicite des types de données lorsque des interactions de données sont impliquées dans le code.

```python
# Variable:Type
# name = "Alex"

# 1. Annotations sur les types de données de base
age:int = 10
money:float = 50.5
is_employee:bool = True
name:str = "Alex"

# 2. Annotations sur les types d'objets de classe
class Student:
    pass

stu:Student = Student()

# 3. Annotations sur les types de conteneur de base
my_list:list = [1, 2, 3]
my_tuple:tuple = (1, 2, 3)
my_set:set = {1, 2, 3}
my_dict:dict = {"age": 18}
my_str:str = "python"

# 4. Annotation détaillée des types de conteneurs
my_list2:list[int] = [1, 2, 3]
my_tuple2:tuple[str, int, bool] = ("age", 18, True)
my_set2: set[int] = {1, 2, 3}
my_dict2: dict[str, int] = {"age": 18}

import random
# Type d'annotation dans les commentaires
var_1 = random.randint(1, 10)   # type: int

# -> return needs type int
def add(x: int, y: int) -> int:
    return x + y

result = add(5, 6)
print(result)

def func(data: list[int]) -> list[int]:
    data.append(666)
    return data
    
# func([1,2,3])

my_list3 = [1, 2, "alex", "luna"]
my_dict3 = {"name": "alex", "age": 18}

from typing import Union

my_list4:list[Union[str, int]] = [1, 2, "alex", "luna"]
my_dict4:dict[str, Union[str, int]] = {"name":"alex", "age": 18}

def func2(data: Union[int, str]) -> Union[int, str]:
    pass

func2("str")
```

### 11. Polymorphisme

- Le polymorphisme signifie que le même comportement, en utilisant des objets différents, permet d'obtenir des états différents. 
- Par exemple, définir une fonction(méthode), déclarer par une annotation de type qu'elle nécessite un objet de la classe parentale et passer en fait un objet de la sous-classe pour effectuer le travail, obtenant ainsi un état de travail différent.
- Une classe qui contient des méthodes abstraites est appelée class abstraite.
- Les méthodes qui n'ont pas d'implémentation concrète(pass) sont appelées méthodes abstraites.
- Principalement utilisé pour la conception de haut niveau(normes de conception) afin que les sous-classes puissent réaliser des implémentations spécifiques.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof woof woof")

class Cat(Animal):
    def speak(self):
        print("Miaou Miaou Miaou")

def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
dog.speak()
cat.speak()

make_noise(cat)
make_noise(dog)
```

