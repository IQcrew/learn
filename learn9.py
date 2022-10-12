

def checkNum(func):
    def wrapper(num):
        try:
            print(func(num))
        except:
            print("LOL")
    return wrapper

@checkNum
def convert(num):
    num = float(num)
    return num


convert("a78")



def decor(func):
    def wraaper():
        return func()+2
    return wraaper

def decor2(func):
    def wrapper():
        return func()*2
    return wrapper



@decor
@decor2
def num():
    return 10











print(num())