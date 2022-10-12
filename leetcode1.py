
def minDistance( word1: str, word2: str) -> int:
    if word1==word2: return 0
    moves = 0
    d = []
    lastIndex = 0
    for  i in word2:
        if i in word1[lastIndex:]:
            lastIndex = word1.index(i,lastIndex)         
            d.append(lastIndex)
        else:
            d.append(-1)
            
    tempDic = {}
    for i, num in enumerate(d):
        if d.count(num)>1 and num!= -1:
            if num in tempDic:
                if num-tempDic[num]>num-i:
                    d[tempDic[num]] = -1
                    tempDic[num] = i
            else:
                tempDic[num] = i
                
    if all(element == -1 for element in d) or word1=="" or word2=="":
        return max(len(word1), len(word2))
    print([i for i in range(len(word1))])
    print(f">>>>>> {d}")
    for num in d:
       if num != -1:
           wi2 = d.index(num)
           if num==wi2:
               ...
           elif num>wi2:
               d.insert(wi2,-2)
               moves+=1
           else:
               del d[wi2-1]
               moves+=1
    moves+=d.count(-1)    
    print(f">>>>>> {d}")
    return moves


print(minDistance("a","ab"))
print(minDistance(word1 = "horse", word2 = "ros"))