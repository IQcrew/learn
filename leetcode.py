from functools import reduce
import time
from tkinter import Y

class Solution: 
    def longestCommonPrefix(self, lst):
        prefix = lst[0]
        for i in lst:
            while not i.startswith(prefix):
                prefix = prefix[:len(prefix)-1]
        return prefix
                
class SolutionB: 
    def longestCommonPrefix(self, lst):
        return reduce(lambda x, y: x if y.startswith(x) else x[:([i if  x[i]==y[i] else -1 for i in range(min(len(y),len(x)))]+[-1]).index(-1)] if x !="" and y !="" and x[0] == y[0] else "" , lst)
                    
idk = SolutionB()
print(idk.longestCommonPrefix(["ab", "a"]))




xt= time.time()
         
for i in range(1000000):
    idk.longestCommonPrefix(["abdsadsad", "abdsaasd", "abaaa"])

print(time.time()-xt)

idk = SolutionB()
xt= time.time()
         
for i in range(1000000):
    idk.longestCommonPrefix(["abdsadsad", "abdsaasd", "abaaa"])

print(time.time()-xt)