bin = "0100"
list = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for i,x in enumerate(bin):
    if x == "1":
        list[2**(len(bin)-i-1)] = 1

print(list)