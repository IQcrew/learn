def inter(x):
    for i in x:
        yield i
        
        
m = inter([1, 2, 3, 4])
n = inter([454,8,87,78])

for i in range(4):
    print(next(m))
    print(next(n))