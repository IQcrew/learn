


def solveSudoku(board: list[list[str]]) -> None:
    Mpos = [ [ set() for i in range(9)] for i in range(9)]
    freePlaces = 0
    for a in board:
        freePlaces += a.count(".")
    sectors =[[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    Msec =[[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    for i in range(9):
        for x in range(9):
            temp =  board[i][x]
            if temp != ".":
                sectors[int(i/3)][int(x/3)].add(temp) 
    while freePlaces >0:
        try:
            for row in range(9):
                for column in range(9):
                    if board[row][column] != ".": continue
                    possibleValues = {"1","2","3","4","5","6","7","8","9"}
                    possibleValues -= set(board[row])
                    possibleValues -= set([board[x][column] for x in range(9)])
                    possibleValues -= sectors[int(row/3)][int(column/3)]
                    if len(possibleValues) == 1:
                        temp = list(possibleValues)[0]
                        board[row][column] = temp
                        sectors[int(row/3)][int(column/3)].add(temp)
                        freePlaces -= 1
                        raise
                    else:
                        Mpos[row][column] = possibleValues
                        Msec[int(row/3)][int(column/3)].update(possibleValues)
            for row in range(9):
                for column in range(9):
                    if len(Mpos[row][column]) == 2:
                        for n in Mpos[row][column]:
                            for m in Mpos[row]:    
                                if m==n: continue
                            for m in range(9):    
                                if Mpos[m][column]: continue
                            if m in Msec[int(row/3)][int(column/3)]: continue

                            board[row][column] = n
                            Mpos[row][column].clear()
                            sectors[int(row/3)][int(column/3)].add(n)
                            freePlaces -= 1
                            raise

        except: ...
    return board













print("\n\n\n\n")
def printSudoku(board):
    for i in range(len(board)):
        for x in range(9):
            if x%3==0: print("|", end="")
            print(board[i][x]+" ", end="")
        print("\n - - - X- - - X- - - " if (i+1)%3==0 else "")



assigment2 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

assigment3 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]

assigment = assigment3
printSudoku(assigment)
print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
printSudoku(solveSudoku(assigment))