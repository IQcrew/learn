import random


lst = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]



class Human:

    def __init__(self, health, age, x, y):
        self.health = health
        self.age = age
        self.x = x
        self.y = y
    
    def ChangeSide(self):
        return Zombie(self.health, self.age, self.x, self.y)
    
    def move(self):
        lst[self.y-1][self.x-1] = 0
        lst[self.y-random.choice([-2,0])][self.x-1] = 1
        




class Zombie:
    def __init__(self, health, age, x, y):
        self.health = health
        self.age = age
        self.x = x
        self.y = y
    def ChangeSide(self):
        return Human(self.health, self.age, self.x, self.y)
   


jack = Human(1,1,1,1)


jack = jack.ChangeSide()

joe = Zombie(10,10,10,10)

del joe
