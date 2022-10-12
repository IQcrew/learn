
with open("data.txt", "r") as f:
    x = f.readlines()


for i in x:
    for y in range(100):
        if not("0"*y in i or "1"*y in i):
            print(y)
            break