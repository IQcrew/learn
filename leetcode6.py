
counter = 0
def uniquePathsIII(grid: list[list[int]]) -> int:
    def solver(grid):
        rowL,columnL= len(grid),len(grid[0])
        for i in range(rowL):
            if(1 in grid[i]):
                x,y= grid[i].index(1),i
                break
        aroundPos = [ i for i in [[1,0], [0,-1], [0,1], [-1,0]] if columnL>(i[0]+x)>=0 and rowL > (i[1]+y) >=0] 
        for o,g in aroundPos:
            match grid[y+g][x+o]:
                case 0:
                    grid_copy = [i.copy() for i in grid]
                    grid_copy[y+g][x+o] = 1
                    grid_copy[y][x] = -1
                    solver(grid_copy)
                case 2:
                    for i in grid:
                        if(0 in i):
                            break
                    else:
                        global counter
                        counter += 1
    solver(grid)
    return counter




print(uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))