duration = 10

def generator(num):
    for i in range(num):
        yield "A"


x = "".join(list(generator(10)))


user_input =  input("zadaj cosi: ")


try:
    user_input = float(user_input)
except:
    raise "NEVIESTO"


print(x)