

class XD:
    def __init__(self,name="",age=10, city= "Bratislava") -> None:
        self.name = name
        self.age = age
        self.city = city
        self.temp = ...

    def __getitem__(self, get):
        exec("self.temp = self."+get)
        return self.temp

    def __setitem__(self,get,set):
        exec("self."+get+" = set")

x = XD(name="tobo")


print(x["name"])
x["idk"] = 10

print(x["idk"])

