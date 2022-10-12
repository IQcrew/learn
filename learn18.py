grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","1","0"],
  ["1","1","1","1","0"],
  ["0","0","0","0","0"],
  ["0","0","1","1","0"]
]

def findTwoNules(lst : list):
    temp_value, temp_list = 0, []
    for z in range(len(lst)):
        for i in range(len(lst[z])):
            if lst[z][i] == "0":
                temp_value = 0
                for x in [(0,1), (1,0), (-1,0), (0,-1)]:
                    try:
                        if lst[z+x[0]][i+x[1]] == "0":
                            temp_value += 1
                    except: temp_value = 100
                if temp_value == 1:
                    temp_list.append((i+1,z+1))

    return(temp_list)

print(findTwoNules(grid))