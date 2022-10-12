class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    x = 4
    @classmethod
    def bydate(cls,name,date):
        return cls(name, 2022-date)
    

c = Person.bydate("tobo", 2005)

print(c.age)

class Emploeyy:
    def __init__(self, ammo) -> None:
        self.ammo = ammo
    def say_ammo(self):
        return self.ammo + 100


class Sniper(Person, Emploeyy):
    def __init__(self, name, age, ammo) -> None:
        super().__init__(name, age)
        Emploeyy.__init__(self, ammo=ammo)


x = Sniper("tobo", 17,25)
print(x.name, x.ammo, x.say_ammo())