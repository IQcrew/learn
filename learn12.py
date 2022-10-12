


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self, idk):
        print(f"my name is {self.name} my age  is  {self.age} {idk}")

    def __len__(self):
        return int(self.age)
    

my = Person("tobo", 16)

print(len(my))
