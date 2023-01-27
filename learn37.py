

grid = [[421,422], [52,52],[521,532,12]]
copy = grid.copy()

copy[1] = grid[1].copy()
grid[1][1] = 2222222222


print(grid)
print(copy)