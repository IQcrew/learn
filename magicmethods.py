

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __add__(self, other):
        return Person(self.name+ " " + other.name, self.age + other.age)
    def __repr__(self) -> str:
        return f"hi i am {self.name} and my age is {self.age}"
    def __del__(self):
        print(f"I died {self.age} years old")
    def __call__(self):
        print("lol")
    def __eq__(self, __o: object) -> bool:
        return True  if self.name == __o.name else False

