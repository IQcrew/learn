

def solveSudoku(board: list[list[str]]) -> None:
    shortestPV = [100,0,0]
    MpossibleValues = [[set() for i in range(9)] for i in range(9)]
    freePlaces = 0
    for a in board:
        freePlaces += a.count(".")
    sectors =[[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]
    Msec =[[[set() for y in range(9)] for x in range(3)] for i in range(3)]
    for i in range(9):
        for x in range(9):
            temp = board[i][x]
            if temp != ".":
                sectors[int(i / 3)][int(x / 3)].add(temp)
    while freePlaces > 0:
        try:
            for row in range(9):
                for column in range(9):
                    if board[row][column] != ".":
                        continue
                    possibleValues = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
                    possibleValues -= set(board[row])
                    possibleValues -= set([board[x][column] for x in range(9)])
                    possibleValues -= sectors[int(row/3)][int(column/3)]
                    if len(possibleValues) == 1:
                        Msec[int(row / 3)][int(column/3)][(row % 3 * 3) + column % 3].clear()
                        temp = list(possibleValues)[0]
                        board[row][column] = temp
                        sectors[int(row/3)][int(column/3)].add(temp)
                        freePlaces -= 1
                        raise
                    else:
                        MpossibleValues[row][column] = possibleValues
                        Msec[int(row / 3)][int(column / 3)][(row % 3 * 3) + column % 3] = possibleValues
            
            for row in range(9):
                for column in range(9):
                    if len(MpossibleValues[row][column]) > 1:
                        if len(MpossibleValues[row][column]) < shortestPV[0]:
                            shortestPV = [len(MpossibleValues[row][column]), row, column]
                        for n in MpossibleValues[row][column]:
                            FinalResult = False
                            temp = False
                            for m in MpossibleValues[row]:
                                if n in m:
                                    if temp:
                                        break
                                    temp = True
                            else:
                                FinalResult = True
                            if not FinalResult:
                                for m in range(9):
                                    if n in MpossibleValues[m][column]:
                                        if temp:
                                            break
                                        temp = True
                                else:
                                    FinalResult = True
                                if not FinalResult:
                                    for x in Msec[int(row/3)][int(column/3)]:
                                        if n in x:
                                            if temp:
                                                break
                                            temp = True
                                    else:
                                        FinalResult = True

                            if FinalResult:
                                board[row][column] = n
                                MpossibleValues[row][column].clear()
                                sectors[int(row/3)][int(column/3)].add(n)
                                freePlaces -= 1
                                raise
                            else:
                                ...
            if shortestPV[0] < 2: return Ellipsis
            for i in MpossibleValues[shortestPV[1]][shortestPV[2]]:
                tempBoard = board
                tempBoard[shortestPV[1]][shortestPV[2]] = i
                temp = solveSudoku(tempBoard)
                if temp == Ellipsis:    ...       
                else:  
                    #treba chcecknut ci sa to doplnilo, a je to zabugovane zas
                    return temp
            break

        except: 
            ...
    return board


print("\n\n\n\n") 


def printSudoku(board):
    for i in range(len(board)):
        for x in range(9):
            if x % 3 == 0:
                print("|", end="")
            print(board[i][x]+" ", end="")
        print("\n - - - X- - - X- - - " if (i + 1) % 3 == 0 else "")



assigment2 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

assigment3 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]

assigment = assigment3
printSudoku(assigment)
print("\n###############################################################\n")
printSudoku(solveSudoku(assigment))
