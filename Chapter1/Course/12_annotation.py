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
    
# func([1,2,3])


