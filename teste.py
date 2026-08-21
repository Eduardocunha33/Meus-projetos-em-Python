class Person: 
    def __init__(self, name, age, higth, weigth, gender):
        self.name = name
        self.age = age
        self.higth = higth
        self.weigth = weigth
        self.gender = gender

Jão = Person("João", 21, 1.80, 70, "Masculine")
print(f"My name is {Jão.name}, i'm {Jão.age} years old, I weigh {Jão.weigth} kg end I am {Jão.higth} cm tall.")

Ana = Person("Ana", 23, 1.65, 56, "feminine")
print(f"My name is {Ana.name}, i'm {Ana.age} years old, I weigh {Ana.weigth} kg end I am {Ana.higth} cm tall.")