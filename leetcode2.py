def generateParenthesis( n: int) -> list[str]:
    lst = []
    def temp(item, open, close):
        if open==close==n:
            lst.append(item)
        else:
            if open <n:
                temp(item+"(", open+1, close)
            if open > close:
                temp(item+")", open, close+1)
    temp("", 0,0)
    return lst
        
    
    
    
    
print(generateParenthesis(3))