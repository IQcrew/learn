

x =[1,1,1,1,1]

print(all(element == 1 for element in x))



x= "ab"
y = "a"

print(x[:([i if x[i]==y[i] else -1 for i in range(min(len(x),len(y)))]+[-1]).index(-1)])
print(min(x,y))
print(min(x,y) if min(x,y).startswith(min(x,y)) else x[:([i if x[i]==y[i] else -1 for i in range(min(len(x),len(y)))]+[-1]).index(-1)] if x !="" and y !="" and x[0] == y[0] else "")



