

# class convert to list

from dataclasses import dataclass

@dataclass(kw_only=True)
class idk: 
    name: str
    age: int
    iq: int
    
    
    def __iter__(self):
        return iter([self.name, self.age, self.iq])

x = idk(name="jozo", age="21" , iq="115")
print(list(x))








