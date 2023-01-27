





velkost = 4

def vypisMaticu():
    for i in range(velkost):
        print("|", end=" ")
        for j in range(velkost):
            print(matica[i][j], end=" ")
    print("|")

matica = [  ["-"] * velkost for d in range(velkost)]

#matica = ["-"] * velkost
#matica = [matica] * velkost


#matica = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]



vypisMaticu()

for i in range(velkost):
    for j in range(velkost):
        idk = input("Zadaj hodnotu v " + str(i+1) + ". stĺpci a " + str(j+1) + ".riadku:")
        matica[i][j] = int(idk)
vypisMaticu()