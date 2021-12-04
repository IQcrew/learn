from functools import reduce
x = lambda num : reduce(lambda x,y: x*y, [int(i) for i in str(num)])
