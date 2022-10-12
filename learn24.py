from functools import reduce
import math
import random


def correct(bin, list):
    for i,x in enumerate(bin[::-1]):
        if x == "1":
            list[2**i] = 1
    return list

def printBlock(block, error):
    for x,item in enumerate(block):
        print(item, end=' ')    
        if((x+1)%int(math.sqrt(len(block)))==0):
            print('')


def errorFinder(block : list) -> str:
    """
    return binary index of error bit 
    """
    return format(reduce(lambda x, y: x ^ y,[i for i, bit in enumerate(block) if bit]), '04b')

# Main
temp = int(input("zadaj mocninu bitu: "))
bits = [random.randrange(2) for i in range(256)]
for y,bit in enumerate(bits):
    if y & (y - 1) == 0 and y != 0:
        bits[y] = 0
bits = correct(errorFinder(bits), bits)
printBlock(bits, -1)
input = int(input('enter bit to change: '))-1
bits[input] = 1 - bits[input]
error = int(errorFinder(bits),2)
printBlock(bits, error)
print(f'chybny je {error+1} bit')