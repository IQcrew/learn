import datetime

# switch v pythone
x = "da"
match x:
    case "a":
        print("id")
    case _:
        print("xd")
        
point = (2,0) # cool riesenie pre a tuple, listy, classi...
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
  
  
    
class Point:
    x: int = 0
    y: int = 0
idktemp = Point() 
idktemp.x = 4
def location(point):
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x=x, y=0):
            print(f"X={x} and the point is on the x-axis.")
        case Point():
            print("The point is located somewhere else on the plane.")
        case _:
            print("Not a point")
location(idktemp)




#auto __init__ fill
from dataclasses import dataclass

@dataclass(kw_only=True)
class Birthday:
    name: str
    birthday: datetime.date
    
x = Birthday(name="ahoj", birthday=datetime.date(2005,2,3))
# x = Birthday() would raise a error
print(x.name)