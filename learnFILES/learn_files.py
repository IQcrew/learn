from functools import reduce

numbers = [2, 3, 4, 5, 6]

def reduce_sum(a, b):
    return a + b

print(reduce(reduce_sum, numbers))

