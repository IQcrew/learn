import random
import time
ex = [9,7,8,448,84,561,481,51,48,151,484,18,4,15,484,11,584,15,1248,741,3821,265,81,2,6,4,796,1487,793,596,78,10,5]
ex = [random.randint(1,10000) for i in range(100_000)]
def mySort(lst: list):
    length = len(lst)
    if(length<=1): return lst
    lg = round(length/2)
    left = mySort(lst[:lg])
    right = mySort(lst[lg:])
    newlst = []
    for _ in range(length):
        try:
            l = left[0]
        except :
            newlst.extend(right)
            break
        try:
            r = right[0]
        except:
            newlst.extend(left)
            break        
        if(r<l): newlst.append(r); right.pop(0)
        elif(r>l): newlst.append(l); left.pop(0)
        else: newlst.append(l); left.pop(0)
    return newlst
    
op = time.time()
mySort(ex)
print("hotovo")
print(time.time() - op)